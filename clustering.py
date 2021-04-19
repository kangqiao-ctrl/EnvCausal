from sklearn import preprocessing 
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

def pca_clustering(df,components=3,clusters=3):
    pipeline = Pipeline([('scaling', preprocessing.StandardScaler()), ('pca', PCA(n_components=components))])
    df_std = pd.DataFrame(pipeline.fit_transform(df), index=df.index)
    estimator = KMeans(n_clusters=clusters)
    estimator.fit(df_std)
    label_pred = estimator.labels_
    df_std['label'] = label_pred
    return df_std