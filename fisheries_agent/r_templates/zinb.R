args <- commandArgs(trailingOnly = TRUE)
csv <- args[1]; outdir <- args[2]; response <- args[3]
predictors <- strsplit(args[4], ",")[[1]]
zi_terms <- args[5]

suppressPackageStartupMessages(library(glmmTMB))
data <- read.csv(csv, check.names = FALSE)

bt <- function(x) sprintf("`%s`", x)
main_formula <- as.formula(paste(bt(response), "~", paste(bt(predictors), collapse = " + ")))
zi_formula <- if (zi_terms == "1") ~1 else as.formula(paste("~", paste(bt(strsplit(zi_terms, ",")[[1]]), collapse = " + ")))

model <- glmmTMB(main_formula, ziformula = zi_formula, family = nbinom2, data = data)
ci <- tryCatch(confint(model), error = function(e) paste("confint failed:", conditionMessage(e)))

writeLines(
  capture.output({
    print(summary(model))
    cat("\n--- CONFIDENCE INTERVALS ---\n")
    print(ci)
  }),
  file.path(outdir, "output.txt")
)
