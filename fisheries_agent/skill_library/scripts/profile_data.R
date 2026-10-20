# Data handler profile: writes data_summary.json and data_summary.md next to a data file.
# Usage: Rscript profile_data.R <data file (.csv/.tsv/.txt/.xlsx/.xls)> [sheet name]
# CSV/text files are read with base R; Excel needs the 'readxl' package (not installed by this script).
# Needs 'jsonlite' for the .json output. Raw data is never modified.

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1) stop("usage: Rscript profile_data.R <file> [sheet]")
path <- normalizePath(args[1], mustWork = TRUE)
only_sheet <- if (length(args) >= 2 && nzchar(args[2])) args[2] else NULL
if (!requireNamespace("jsonlite", quietly = TRUE)) stop("R package 'jsonlite' is required (ask the user before installing it).")

MAX_ROWS <- 200000
MAX_SHEETS <- 12
MAX_LEVELS <- 12
NA_STRINGS <- c("", "NA", "N/A", "NULL", "null")

ext <- tolower(tools::file_ext(path))
sheets <- list()
if (ext %in% c("xlsx", "xls")) {
  if (!requireNamespace("readxl", quietly = TRUE)) stop("R package 'readxl' is required for Excel files (ask the user before installing it).")
  names_all <- readxl::excel_sheets(path)
  chosen <- if (is.null(only_sheet)) head(names_all, MAX_SHEETS) else only_sheet
  if (!all(chosen %in% names_all)) stop("sheet not found. Sheets: ", paste(names_all, collapse = ", "))
  for (s in chosen) sheets[[s]] <- as.data.frame(readxl::read_excel(path, sheet = s, n_max = MAX_ROWS, .name_repair = "minimal"))
  skipped <- setdiff(names_all, chosen)
} else if (ext %in% c("csv", "tsv", "txt")) {
  sep <- if (ext == "csv") "," else "\t"
  sheets[["(file)"]] <- utils::read.table(path, header = TRUE, sep = sep, quote = "\"", comment.char = "", na.strings = NA_STRINGS,
                                          stringsAsFactors = FALSE, check.names = FALSE, fill = TRUE, nrows = MAX_ROWS)
  skipped <- character()
} else stop("unsupported file type: .", ext)

profile_col <- function(name, x) {
  n <- length(x)
  if (inherits(x, c("POSIXt", "Date"))) {
    v <- x[!is.na(x)]
    out <- list(name = name, type = "date", missing = n - length(v), unique = length(unique(v)))
    if (length(v)) { out$min <- format(min(v)); out$max <- format(max(v)) }
    return(out)
  }
  if (!is.numeric(x)) {
    x <- trimws(as.character(x)); x[x %in% NA_STRINGS] <- NA
    num <- suppressWarnings(as.numeric(x))
    if (sum(!is.na(x)) > 0 && all(!is.na(num[!is.na(x)]))) x <- num
  }
  v <- x[!is.na(x)]
  if (is.numeric(x)) {
    int <- length(v) > 0 && all(v == round(v))
    out <- list(name = name, type = if (length(v) == 0) "empty" else if (int) "integer" else "numeric", missing = n - length(v), unique = length(unique(v)))
    if (length(v)) out <- c(out, list(min = min(v), max = max(v), mean = round(mean(v), 4), zeros = sum(v == 0), negatives = sum(v < 0)))
    return(out)
  }
  out <- list(name = name, type = if (length(v) == 0) "empty" else "text", missing = n - length(v), unique = length(unique(v)))
  if (length(v) && out$unique <= MAX_LEVELS) out$levels <- as.list(sort(table(v), decreasing = TRUE))
  out
}

hints_for <- function(cols, n_rows) {
  h <- character()
  nm <- vapply(cols, function(c) c$name, "")
  hist <- cols[grepl("^(occ|occasion|pass|session|t|y)[_.]?[0-9]+$", nm, ignore.case = TRUE) &
               vapply(cols, function(c) !is.null(c$max) && c$max %in% c(0, 1) && c$min %in% c(0, 1), TRUE)]
  if (length(hist) >= 3) h <- c(h, sprintf("capture-history matrix (%d occasion columns: %s .. %s)", length(hist), hist[[1]]$name, hist[[length(hist)]]$name))
  for (c in cols) {
    if (grepl("tag|pit|^id$|fish[_ ]?id|individual", c$name, ignore.case = TRUE) && c$unique < n_rows - c$missing)
      h <- c(h, sprintf("repeated individual ids in '%s' (%d unique in %d rows): recaptures or contacts present", c$name, c$unique, n_rows))
    if (c$type == "integer" && grepl("count|catch|abundance|^n$|num_|n_fish", c$name, ignore.case = TRUE) && n_rows > 0 && c$min >= 0) {
      share <- c$zeros / n_rows
      h <- c(h, sprintf("'%s' looks like a count (%.0f%% zeros%s)", c$name, 100 * share, if (share >= 0.3) "; zero-heavy, consider zero-inflated or hurdle models" else ""))
    }
    if (grepl("effort|hours|soak|net[_ ]?(night|set)|distance|area|cpue", c$name, ignore.case = TRUE)) h <- c(h, sprintf("'%s' looks like effort or CPUE", c$name))
    if (!is.null(c$negatives) && c$negatives > 0) h <- c(h, sprintf("'%s' has %d negative value(s): check", c$name, c$negatives))
  }
  dates <- cols[vapply(cols, function(c) c$type == "date", TRUE)]
  if (length(dates)) h <- c(h, sprintf("date column(s): %s", paste(vapply(dates, function(c) c$name, ""), collapse = ", ")))
  h
}

out_sheets <- lapply(names(sheets), function(s) {
  df <- sheets[[s]]
  cols <- lapply(seq_along(df), function(i) profile_col(names(df)[i], df[[i]]))
  list(sheet = s, rows = nrow(df), duplicate_rows = sum(duplicated(df)), columns = cols, hints = as.list(hints_for(cols, nrow(df))))
})
summary <- list(source_file = basename(path), generated = format(Sys.Date()), sheets = out_sheets,
                sheets_not_profiled = as.list(skipped), cleaning_notes = list())

out_dir <- dirname(path)
writeLines(jsonlite::toJSON(summary, auto_unbox = TRUE, pretty = TRUE, null = "null", na = "null"), file.path(out_dir, "data_summary.json"), useBytes = TRUE)

md <- sprintf("# Data summary: %s", basename(path))
for (s in out_sheets) {
  md <- c(md, "", sprintf("## Sheet: %s", s$sheet), "", sprintf("%d rows, %d columns, %d duplicate rows.", s$rows, length(s$columns), s$duplicate_rows), "")
  if (length(s$hints)) md <- c(md, "### Data-type hints", "", paste0("- ", unlist(s$hints)), "")
  md <- c(md, "### Columns", "", "| Column | Type | Missing | Unique | Range / levels |", "| --- | --- | --- | --- | --- |")
  for (c in s$columns) {
    rng <- if (!is.null(c$levels)) paste(sprintf("%s (%d)", names(c$levels), unlist(c$levels)), collapse = ",")
           else if (!is.null(c$min)) sprintf("%s to %s", format(c$min), format(c$max)) else ""
    md <- c(md, sprintf("| %s | %s | %d | %d | %s |", c$name, c$type, c$missing, c$unique, gsub("|", "/", rng, fixed = TRUE)))
  }
}
if (length(skipped)) md <- c(md, "", sprintf("Sheets not profiled (cap %d): %s", MAX_SHEETS, paste(skipped, collapse = ", ")))
md <- c(md, "", "## Cleaning notes", "", "(none recorded)", "")
writeLines(md, file.path(out_dir, "data_summary.md"), useBytes = TRUE)
cat(paste(md, collapse = "\n"), "\n")
cat(sprintf("\nWrote data_summary.json and data_summary.md in %s\n", out_dir))
