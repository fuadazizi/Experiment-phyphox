import pandas as pd
import matplotlib.pyplot as plt

# import and read excel file
dfAccel = pd.read_excel('experiment.xlsx', sheet_name='Accelerometer')
dfGyro = pd.read_excel('experiment.xlsx', sheet_name='Gyroscope')

# variable for accelerometer and gyroscope data
dataaccel = []
datagyro = []

# save with dictionary
# Accelerometer part
for i in dfAccel.index:
	data = {}
	data['Time'] = dfAccel['Time (s)'][i]
	data['x'] = dfAccel['Acceleration x (m/s^2)'][i]
	data['y'] = dfAccel['Acceleration y (m/s^2)'][i]
	data['z'] = dfAccel['Acceleration z (m/s^2)'][i]
	dataaccel.append(data)

# Gyroscope part
# I want to use deg/s unit instead rad/s
# so I convert rad/s unit to deg/s unit
for i in dfGyro.index:
	data = {}
	data['Time'] = dfGyro['Time (s)'][i]
	data['x'] = dfGyro['Gyroscope x (rad/s)'][i] * 57.2958
	data['y'] = dfGyro['Gyroscope y (rad/s)'][i] * 57.2958
	data['z'] = dfGyro['Gyroscope z (rad/s)'][i] * 57.2958
	datagyro.append(data)

#print(dataaccel)
#print(datagyro)

