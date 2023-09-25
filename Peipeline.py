url_data = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
varnames = ['var_preg', 'var_plas', 'var_pres', 'var_skin', 'var_test', 'var_mass', 'var_pedi', 'var_age', 'var_class']
vardataframe = read_csv(url_data, names=varnames)
vararray = vardataframe.values
varX = vararray[:,0:8]
varY = vararray[:,8]
