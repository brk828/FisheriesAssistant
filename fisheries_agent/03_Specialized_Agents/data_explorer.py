import os
import subprocess

def run_multivariate_exploration(csv_path: str, method: str = "PCA", label_col: str = None):
    """
    Automates multi-variate statistical graphics (PCA, MDS, Heatmaps) using R vegan.
    """
    method_upper = method.upper()
    
    r_script_content = f"""
    library(vegan)
    library(ggplot2)
    
    data <- read.csv("{csv_path}")
    
    # Separate numeric data from grouping column
    num_idx <- sapply(data, is.numeric)
    numeric_data <- data[, num_idx]
    
    png("multivariate_plot.png", width=800, height=600)
    
    if ("{method_upper}" == "PCA") {{
        pca_res <- rda(numeric_data, scale = TRUE)
        biplot(pca_res, main="Principal Component Analysis (PCA)")
    }} else if ("{method_upper}" == "MDS") {{
        # Handle community matrices using Bray-Curtis
        dist_matrix <- vegdist(numeric_data, method="bray")
        mds_res <- metaMDS(dist_matrix, trace = FALSE)
        plot(mds_res, type="t", main="Non-metric Multidimensional Scaling (MDS)")
    }} else if ("{method_upper}" == "HEATMAP") {{
        heatmap(as.matrix(numeric_data), main="Data Heatmap Matrix")
    }}
    
    dev.off()
    """
    
    script_path = "temp_explorer.R"
    with open(script_path, "w") as f:
        f.write(r_script_content)
        
    try:
        subprocess.run(["Rscript", script_path], capture_output=True, text=True, check=True)
        return f"Successfully generated {method_upper} plot saved to 'multivariate_plot.png'."
    except subprocess.CalledProcessError as e:
        return f"Exploration failed:\n{e.stderr}"
    finally:
        if os.path.exists(script_path):
            os.remove(script_path)
