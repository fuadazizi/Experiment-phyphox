import pandas as pd

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
for i in dfGyro.index:
	data = {}
	data['Time'] = dfGyro['Time (s)'][i]
	data['x'] = dfGyro['Gyroscope x (rad/s)'][i]
	data['y'] = dfGyro['Gyroscope y (rad/s)'][i]
	data['z'] = dfGyro['Gyroscope z (rad/s)'][i]
	datagyro.append(data)

print(dataaccel)
print(datagyro)