url_data = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
varnames = ['var_preg', 'var_plas', 'var_pres', 'var_skin', 'var_test', 'var_mass', 'var_pedi', 'var_age', 'var_class']
vardataframe = read_csv(url_data, names=varnames)
vararray = vardataframe.values
varX = vararray[:,0:8]
varY = vararray[:,8]



urlfeatures = []
urlfeatures.append(('pca', PCA(n_components=3)))
urlfeatures.append(('select_best', SelectKBest(k=6)))
feature_union = FeatureUnion(urlfeatures)
# Here, pipeline is created
estimators = []
estimators.append(('feature_union', feature_union))
estimators.append(('logistic', LogisticRegression()))
model = Pipeline(estimators)
# The pipelie is tested here
seed = 7
varkfold = KFold(n_splits=10)
dataresults = cross_val_score(model, varX, varY, cv=varkfold)
print(dataresults.mean())
