import pandas as pd
import matplotlib.pyplot as plt

# import and read excel file
dfAccel = pd.read_excel('experiment.xlsx', sheet_name='Accelerometer')
dfGyro = pd.read_excel('experiment.xlsx', sheet_name='Gyroscope')

# variable for accelerometer and gyroscope data
dataAccel = []
dataGyro = []

# save with dictionary
# Accelerometer part
for i in dfAccel.index:
	data = {}
	data['t'] = dfAccel['Time (s)'][i]
	data['x'] = dfAccel['Acceleration x (m/s^2)'][i]
	data['y'] = dfAccel['Acceleration y (m/s^2)'][i]
	data['z'] = dfAccel['Acceleration z (m/s^2)'][i]
	dataAccel.append(data)

# Gyroscope part
# I want to use deg/s unit instead rad/s
# so I convert rad/s unit to deg/s unit
for i in dfGyro.index:
	data = {}
	data['t'] = dfGyro['Time (s)'][i]
	data['x'] = dfGyro['Gyroscope x (rad/s)'][i] * 57.2958
	data['y'] = dfGyro['Gyroscope y (rad/s)'][i] * 57.2958
	data['z'] = dfGyro['Gyroscope z (rad/s)'][i] * 57.2958
	dataGyro.append(data)

#print(dataAccel)
#print(dataGyro)

# plot Accelerometer
plotX = []
plotY = []
plotZ = []
time = []
for data in dataAccel:
	plotX.append(data['x'])
	plotY.append(data['y'])
	plotZ.append(data['z'])
	time.append(data['t'])

plt.subplot(2,1,1)
plt.plot(time, plotX, label = "X", linewidth=0.8)
plt.plot(time, plotY, label = "Y", linewidth=0.8)
plt.plot(time, plotZ, label = "Z", linewidth=0.8)
#plt.title('Plot Accelerometer')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Accelerometer (m/s^2)')

# plot Gyroscope
for data in dataGyro:
	plotX.append(data['x'])
	plotY.append(data['y'])
	plotZ.append(data['z'])
	time.append(data['t'])

plt.subplot(2,1,2)
plt.plot(time, plotX, label = "X", linewidth=0.8)
plt.plot(time, plotY, label = "Y", linewidth=0.8)
plt.plot(time, plotZ, label = "Z", linewidth=0.8)
#plt.title('Plot Gyroscope')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Gyroscope (deg/s)')

# plot show
plt.show()
#keys = dataAccel.keys()
#values = dataAccel.values()
#plt.bar(keys,values)

#plt.plot(dataAccel)
#plt.show