args <- commandArgs(trailingOnly = TRUE)
csv <- args[1]; outdir <- args[2]; method <- toupper(args[3])

suppressPackageStartupMessages(library(vegan))
data <- read.csv(csv, check.names = FALSE)
numeric_data <- data[, sapply(data, is.numeric), drop = FALSE]
numeric_data <- numeric_data[complete.cases(numeric_data), , drop = FALSE]
if (ncol(numeric_data) < 2 || nrow(numeric_data) < 3) stop("Need at least 2 numeric columns and 3 complete rows.")

png(file.path(outdir, "plot.png"), width = 800, height = 600)
if (method == "PCA") {
  biplot(rda(numeric_data, scale = TRUE), main = "PCA Biplot")
} else if (method == "MDS") {
  plot(metaMDS(vegdist(numeric_data, method = "bray"), trace = FALSE), type = "t", main = "MDS Plot")
} else if (method == "HEATMAP") {
  heatmap(as.matrix(numeric_data), main = "Heatmap")
} else {
  stop("Unsupported method")
}
invisible(dev.off())

writeLines(sprintf("%s plot written (%d rows, %d numeric columns).", method, nrow(numeric_data), ncol(numeric_data)),
           file.path(outdir, "output.txt"))
