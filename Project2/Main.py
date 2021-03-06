#implementation of 2nd project for Statistics
from util import prepare_and_load_data
from hierarchical_cluster_exercise import hierarchical_cluster_analysis
from PCA_exercise import pca_exercise, scree_plot
from PCA_components_comparison_exercise import principal_components_comparison_given_data, principal_components_comparison_3by3
from Kmeans_extraction_exercise import best_k_for_kmeans, best_k_for_kmeans_given_data
from Kmeans_exercise import assignment2_point3, assignment2_point3_top2_eigenvalues, silhouette, original_vars_PCA


def main():
    path = r'./data/wines_properties.csv'
    wine_data = prepare_and_load_data(path, skip_rows=0)

    # point 1: PCA
    pca_exercise()
    # for the report
    scree_plot()

    # point 2: hierarchical cluster analysis
    hierarchical_cluster_analysis()
    
    # point 3: k-means cluster analysis
    assignment2_point3()

    # point 3.1: silhouette
    silhouette()
    
    # point 3.2: Plot on the space of the first two dimensions of the PCA the clusters obtained with K-means
    assignment2_point3_top2_eigenvalues()

    # point 3.3 and 3.4:
    original_vars_PCA()
    
    # point 4:
    best_k = best_k_for_kmeans_given_data(wine_data)
    print("The best number of clusters is :" + str(best_k))

    # point 5:
    # It takes a while for them to load, be patient
    principal_components_comparison_given_data(wine_data, column_id=1)
    principal_components_comparison_3by3(wine_data)
    return None


main()