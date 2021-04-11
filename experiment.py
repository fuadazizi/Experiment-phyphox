import pandas as pd

# import dan baca file excel
dfAccel = pd.read_excel('experiment.xlsx', sheetname='Accelerometer')
dfGyro = pd.read_excel('experiment.xlsx', sheetname='Gyroscope')

# variabel penampung data accelerometer dan gyroscope
dataaccel = []
datagyro = []


for i in dfAccel.index:
	data = {}
	data['Time'] = df['Time'][i]
	data['x'] = df['Acceleration x (m/s^2)'][i]
	data['y'] = df['Acceleration y (m/s^2)'][i]
	data['z'] = df['Acceleration z (m/s^2)'][i]
	dataaccel.append(data)
