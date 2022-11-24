# Importing
import pandas as pd

# Loading data from excel
Data = pd.read_csv('Data\hly1875.csv', skiprows=18, names=["Date and Time", "Rainfall Indicators", "Precipitation Amount", "Temperature Indicators", "Air Temperature", "Wet Bulb Indicators", "Wet Bulb Temperature","Dew Point Temperature", "Vapour Pressure", "Relative Humidity", "Mean Sea Level Pressure", "Wind Speed Indicators", "Mean Wind Speed", "Wind Direction Indicators", "Predominant Wind Direction"])

# Cleaning data
#Data = Data.drop(['B', 'C'], axis=1)
Data = Data.loc[Data["Rainfall Indicators"] == 0]
Data = Data.loc[Data["Temperature Indicators"] == 0]
Data = Data.loc[Data["Wet Bulb Indicators"] == 0]
Data = Data.loc[Data["Wind Speed Indicators"] == 2]
Data = Data.loc[Data["Wind Direction Indicators"] == 2]

print(Data.head())