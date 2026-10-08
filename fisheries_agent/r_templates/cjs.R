args <- commandArgs(trailingOnly = TRUE)
csv <- args[1]; outdir <- args[2]; prefix <- args[3]
iters <- as.integer(args[4])

suppressPackageStartupMessages(library(nimble))
raw <- read.csv(csv, check.names = FALSE)
ch <- as.matrix(raw[, startsWith(colnames(raw), prefix), drop = FALSE])
ch[is.na(ch)] <- 0
n_occ <- ncol(ch)

first <- apply(ch, 1, function(x) { w <- which(x == 1); if (length(w)) min(w) else NA })
last <- apply(ch, 1, function(x) { w <- which(x == 1); if (length(w)) max(w) else NA })
# Animals never seen, or first seen on the final occasion, carry no survival information.
keep <- !is.na(first) & first < n_occ
if (sum(keep) < 2) stop("Fewer than two usable capture histories.")
ch <- ch[keep, , drop = FALSE]; first <- first[keep]; last <- last[keep]
n_ind <- nrow(ch)

z_data <- matrix(NA, n_ind, n_occ)
z_init <- matrix(NA, n_ind, n_occ)
for (i in seq_len(n_ind)) {
  if (last[i] > first[i]) z_data[i, (first[i] + 1):last[i]] <- 1
  if (last[i] < n_occ) z_init[i, (last[i] + 1):n_occ] <- 1
}

cjs_code <- nimbleCode({
  phi ~ dunif(0, 1)
  p ~ dunif(0, 1)
  for (i in 1:n_ind) {
    z[i, first[i]] <- 1
    for (t in (first[i] + 1):n_occ) {
      z[i, t] ~ dbern(z[i, t - 1] * phi)
      y[i, t] ~ dbern(z[i, t] * p)
    }
  }
})

model <- nimbleModel(cjs_code,
  constants = list(n_ind = n_ind, n_occ = n_occ, first = first),
  data = list(y = ch, z = z_data),
  inits = list(phi = 0.5, p = 0.5, z = z_init))
cmodel <- compileNimble(model)
mcmc <- buildMCMC(configureMCMC(model, monitors = c("phi", "p"), print = FALSE))
cmcmc <- compileNimble(mcmc, project = model)
samples <- runMCMC(cmcmc, niter = iters, nburnin = floor(iters * 0.1), nchains = 1, progressBar = FALSE)

summ <- t(sapply(as.data.frame(samples), function(x)
  c(mean = mean(x), sd = sd(x), lower95 = unname(quantile(x, 0.025)), upper95 = unname(quantile(x, 0.975)))))
writeLines(
  capture.output({
    cat("CJS model: constant survival (phi) and detection (p)\n")
    cat("Animals used:", n_ind, " Occasions:", n_occ, " Iterations:", iters, "\n\n")
    print(round(summ, 4))
  }),
  file.path(outdir, "output.txt")
)
