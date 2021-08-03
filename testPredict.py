import pickle
import pandas as pd

model_file = 'model.sav'
loaded_model = pickle.load(open(model_file, 'rb'))

inputData = {'TempAvgF': 29, 'HumidityAvgPercent': 70, 'SeaLevelPressureAvgInches': 390}
inputDf = pd.DataFrame(inputData, index=[0])

rainPercentage = loaded_model.predict(inputDf)[0]

print(rainPercentage)