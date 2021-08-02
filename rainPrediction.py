import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle
data = pd.read_csv("austin_weather.csv")

data = data.drop(
    ['TempHighF','TempLowF','HumidityHighPercent','HumidityLowPercent',
     'DewPointHighF', 'DewPointAvgF', 'DewPointLowF',
     'SeaLevelPressureHighInches', 'SeaLevelPressureLowInches',
     'VisibilityHighMiles', 'VisibilityAvgMiles', 'VisibilityLowMiles',
     'WindHighMPH', 'WindAvgMPH', 'WindGustMPH', 'PrecipitationSumInches'], axis = 1)

data = data.replace(' ', 0)
data = data.replace('Fog', 0)
data = data.replace('Fog , Rain', 1)
data = data.replace('Fog , Rain , Thunderstorm', 1)
data = data.replace('Fog , Thunderstorm', 0)
data = data.replace('Rain', 1)
data = data.replace('Rain , Snow', 1)
data = data.replace('Rain , Thunderstorm', 1)
data = data.replace('Thunderstorm', 0)
data = data.replace('-', 0)
data["SeaLevelPressureAvgInches"] = pd.to_numeric(data["SeaLevelPressureAvgInches"], downcast="float")
data["SeaLevelPressureAvgInches"] = 12 * data["SeaLevelPressureAvgInches"]

data.to_csv('weather.csv')
X = data.drop(['Events', 'Date'], axis=1)
Y = data['Events']
X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size = 0.7, test_size = 0.3, random_state = 100)
model = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
model.fit(X_train, y_train)
y_test_predict = model.predict(X_test)

rmse = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2 = round(model.score(X_test, y_test),3)

print("\n\n","The model performance for training set")
print("--------------------------------------")
print("Root Mean Squared Error: {}".format(rmse))
print("R^2: {}".format(r2))
print("\n")

model_file = 'model.sav'
pickle.dump(model, open(model_file, 'wb'))
