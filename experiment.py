# import all the library we need
import pandas as pd
import matplotlib.pyplot as plt
import math

# import and read excel file
dfAccel = pd.read_excel('experiment.xlsx', sheet_name='Accelerometer')
dfGyro = pd.read_excel('experiment.xlsx', sheet_name='Gyroscope')

# variable for accelerometer and gyroscope data
dataAccel = {}
dataGyro = {}

# save with dictionary
# Accelerometer part
time = []
dataX = []
dataY = []
dataZ = []
for i in dfAccel.index:
	time.append(dfAccel['Time (s)'][i])
	dataX.append(dfAccel['Acceleration x (m/s^2)'][i])
	dataY.append(dfAccel['Acceleration y (m/s^2)'][i])
	dataZ.append(dfAccel['Acceleration z (m/s^2)'][i])
dataAccel['t'] = time
dataAccel['x'] = dataX
dataAccel['y'] = dataY
dataAccel['z'] = dataZ

# Gyroscope part
# I want to use deg/s unit instead rad/s, so I convert rad/s unit to deg/s unit
# with using math.degrees()
time = []
dataX = []
dataY = []
dataZ = []
for i in dfGyro.index:
	time.append(dfGyro['Time (s)'][i])
	dataX.append(dfGyro['Gyroscope x (rad/s)'][i])
	dataY.append(dfGyro['Gyroscope y (rad/s)'][i])
	dataZ.append(dfGyro['Gyroscope z (rad/s)'][i])
dataGyro['t'] = time
dataGyro['x'] = dataX
dataGyro['y'] = dataY
dataGyro['z'] = dataZ

# plot Accelerometer
'''
plotX = []
plotY = []
plotZ = []
time = []

for data in dataAccel:
	plotX.append(data['x'])
	plotY.append(data['y'])
	plotZ.append(data['z'])
	time.append(data['t'])
'''
plt.title('Plot Accelerometer')
#plt.subplot(2,1,1)
plt.plot(dataAccel['t'], dataAccel['x'], label = "X", linewidth=0.7, color = 'red')
plt.plot(dataAccel['t'], dataAccel['y'], label = "Y", linewidth=0.7, color = 'green')
plt.plot(dataAccel['t'], dataAccel['z'], label = "Z", linewidth=0.7, color = 'blue')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Accelerometer (m/s^2)')
plt.show()

# plot Gyroscope
'''
plotX = []
plotY = []
plotZ = []
time = []

for data in dataGyro:
	plotX.append(data['x'])
	plotY.append(data['y'])
	plotZ.append(data['z'])
	time.append(data['t'])
'''
plt.title('Plot Gyroscope')
#plt.subplot(2,1,2)
plt.plot(dataGyro['t'], dataGyro['x'], label = "X", linewidth=0.7, color = 'red')
plt.plot(dataGyro['t'], dataGyro['y'], label = "Y", linewidth=0.7, color = 'green')
plt.plot(dataGyro['t'], dataGyro['z'], label = "Z", linewidth=0.7, color = 'blue')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Gyroscope (deg/s)')

# plot show
plt.show()

# Now change accelerometer data to accelerometer angle to know knee flexion
print("Convert accelerometer to accelerometer angle")

def arctan(x,y,z):
	return math.degrees(math.atan(abs(z/math.sqrt(y**2 + z**2))))

newAccel = []
timeAccel = []
for i in range(len(dataAccel['t'])):
	x = dataAccel['x'][i]
	y = dataAccel['y'][i]
	z = dataAccel['z'][i]
	newAccel.append(arctan(x,y,z))
	#timeAccel.append(data['t'])

# plot the new Acceleration data
plt.title('Plot Accelerometer Angle')
plt.plot(dataAccel['t'],newAccel,linewidth=0.7)
plt.xlabel('Time (s)')
plt.ylabel('Accelerometer angle (degree)')
plt.show()

#print(newAccel)

# Now to get angle of gyroscope, we need to integral the gyroscope data

newGyro = []
timeGyro = []
plotX = []
plotY = []
plotZ = []
dt = dataGyro['t'][1] - dataGyro['t'][0]
for i in range(len(dataGyro['t'])):
	plotX.append(dataGyro['x'][i]*dt)
	plotY.append(dataGyro['y'][i]*dt)
	plotZ.append(dataGyro['z'][i]*dt)
	#timeGyro.append(data['t'])

# plot the new Integral gyroscope data
plt.title('Plot Gyroscope Angle')
plt.plot(dataGyro['t'], plotX, label = 'X', linewidth=0.7)
plt.plot(dataGyro['t'], plotY, label = 'Y',linewidth=0.7)
plt.plot(dataGyro['t'], plotZ, label = 'Z',linewidth=0.7)
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Gyroscope angle (degree)')
plt.show()