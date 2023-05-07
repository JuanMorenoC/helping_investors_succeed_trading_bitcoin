# Library imports
# Data treatment
# ==============================================================================
import numpy as np
import pandas as pd
from sklearn import linear_model

# Dataset reading and obtaining information on dataset size, type of variables and missing data in the dataset
data = pd.read_csv("training_set.csv", sep=",")
print("dataset size")
print(data.shape)
print("dataset information")
print(data.info())
print("check missing data")
print(data.isna().sum().sort_values())

#print(data)

# crear un modelo que use el algoritmo de regresion lineal
# y entrenarlo con los datos de nuestro csv
regression_model = linear_model.LinearRegression()
print ("Training model...")
# entrenamiento del modelo
regression_model.fit(data[['Open']], data.Volume) 
print ("Model trained.")
# pedir al usuario que introduzca un area y calcular
# su precio usando nuestro modelo
input_area = int(3)
proped_price = regression_model.predict([[input_area]])
print ("Proped price:", round(proped_price[0], 2))