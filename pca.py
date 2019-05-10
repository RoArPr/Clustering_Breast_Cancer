from sklearn.decomposition import PCA
import pandas as pd

#procedure to apply model PCA and visualization of the clusters
def PCA_model(X, components_number):
    #Apply PCA and return pca fit estimator, the reduce data in form of dataframe and the sum explained variance 
    c=components_number
    pca = PCA(n_components=c).fit(X)    
    reduced_data=pca.transform(X)    
    df_reduced_data=pd.DataFrame((reduced_data),columns=[range(1,c+1)])
    sum_vexp_var=sum(pca.explained_variance_ratio_)
    return pca, df_reduced_data, sum_vexp_var