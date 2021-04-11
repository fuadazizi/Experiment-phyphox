# import all the library we need
import pandas as pd
import matplotlib.pyplot as plt
import math

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
# I want to use deg/s unit instead rad/s, so I convert rad/s unit to deg/s unit
for i in dfGyro.index:
	data = {}
	data['t'] = dfGyro['Time (s)'][i]
	data['x'] = math.degrees(dfGyro['Gyroscope x (rad/s)'][i])
	data['y'] = math.degrees(dfGyro['Gyroscope y (rad/s)'][i])
	data['z'] = math.degrees(dfGyro['Gyroscope z (rad/s)'][i])
	dataGyro.append(data)

# plot Accelerometer
plotX = []
plotY = []
plotZ = []
time = []
'''
for data in dataAccel:
	plotX.append(data['x'])
	plotY.append(data['y'])
	plotZ.append(data['z'])
	time.append(data['t'])
plt.title('Plot Accelerometer')
#plt.subplot(2,1,1)
plt.plot(time, plotX, label = "X", linewidth=0.7, color = 'red')
plt.plot(time, plotY, label = "Y", linewidth=0.7, color = 'green')
plt.plot(time, plotZ, label = "Z", linewidth=0.7, color = 'blue')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Accelerometer (m/s^2)')
plt.show()
'''
# plot Gyroscope
plotX = []
plotY = []
plotZ = []
time = []

for data in dataGyro:
	plotX.append(data['x'])
	plotY.append(data['y'])
	plotZ.append(data['z'])
	time.append(data['t'])

plt.title('Plot Gyroscope')
#plt.subplot(2,1,2)
#plt.plot(time, plotX, label = "X", linewidth=0.7, color = 'red')
plt.plot(time, plotY, label = "Y", linewidth=0.7, color = 'green')
#plt.plot(time, plotZ, label = "Z", linewidth=0.7, color = 'blue')
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
for data in dataAccel:
	x = data['x']
	y = data['y']
	z = data['z']
	newAccel.append(arctan(x,y,z))
	timeAccel.append(data['t'])

# plot the new Acceleration data
plt.title('Plot Accelerometer Angle')
plt.plot(timeAccel,newAccel,linewidth=0.7)
plt.xlabel('Time (s)')
plt.ylabel('Accelerometer angle (degree)')
plt.show()

#print(newAccel)
