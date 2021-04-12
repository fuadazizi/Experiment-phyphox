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

# save with dictionary of list
# Accelerometer part
Ndata = []
dataX = []
dataY = []
dataZ = []
for i in dfAccel.index:
	Ndata.append(i)
	dataX.append(dfAccel['Acceleration x (m/s^2)'][i])
	dataY.append(dfAccel['Acceleration y (m/s^2)'][i])
	dataZ.append(dfAccel['Acceleration z (m/s^2)'][i])
dataAccel['n'] = Ndata
dataAccel['x'] = dataX
dataAccel['y'] = dataY
dataAccel['z'] = dataZ

# Gyroscope part
# I want to use deg/s unit instead rad/s, so I convert rad/s unit to deg/s unit
# with using math.degrees()
Ndata = []
dataX = []
dataY = []
dataZ = []
for i in dfGyro.index:
	Ndata.append(i)
	dataX.append(math.degrees(dfGyro['Gyroscope x (rad/s)'][i]))
	dataY.append(math.degrees(dfGyro['Gyroscope y (rad/s)'][i]))
	dataZ.append(math.degrees(dfGyro['Gyroscope z (rad/s)'][i]))
dataGyro['n'] = Ndata
dataGyro['x'] = dataX
dataGyro['y'] = dataY
dataGyro['z'] = dataZ

# plot Accelerometer

plt.title('Plot Accelerometer')
#plt.subplot(2,1,1)
plt.plot(dataAccel['n'], dataAccel['x'], label = "X", linewidth=0.7, color = 'red')
plt.plot(dataAccel['n'], dataAccel['y'], label = "Y", linewidth=0.7, color = 'green')
plt.plot(dataAccel['n'], dataAccel['z'], label = "Z", linewidth=0.7, color = 'blue')
plt.legend()
plt.xlabel('Number of Data')
plt.ylabel('Accelerometer (m/s^2)')
plt.show()

# plot Gyroscope

plt.title('Plot Gyroscope')
#plt.subplot(2,1,2)
plt.plot(dataGyro['n'], dataGyro['x'], label = "X", linewidth=0.7, color = 'red')
plt.plot(dataGyro['n'], dataGyro['y'], label = "Y", linewidth=0.7, color = 'green')
plt.plot(dataGyro['n'], dataGyro['z'], label = "Z", linewidth=0.7, color = 'blue')
plt.legend()
plt.xlabel('Number of Data')
plt.ylabel('Gyroscope (deg/s)')
plt.show()

# Now change accelerometer data to accelerometer angle to know knee flexion
print("Convert accelerometer to accelerometer angle")

newAccel = []
timeAccel = []
for i in range(len(dataAccel['n'])):
	x = dataAccel['x'][i]
	y = dataAccel['y'][i]
	z = dataAccel['z'][i]
	newAccel.append(math.degrees(math.atan2(z,y)))

# plot the new Acceleration data
plt.title('Plot Accelerometer Angle')
plt.plot(dataAccel['n'],newAccel, label = 'Accelerometer angle', linewidth=0.7)
plt.plot(dataGyro['n'],dataGyro['y'], label = 'Yaw Gyroscope (y-axis)', linewidth=0.7)
plt.legend()
plt.xlabel('Number of Data')
plt.ylabel('Accelerometer angle (degree)')
plt.show()

# Now to get angle of gyroscope, more precisely the yaw, we need to integral the gyroscope data of yaw
print("Complementary Filter Algorithm to know Knee Flexion")
print("Integral yaw of gyroscope. In my case, the y-axis")

yawGyro = []
dt = 0.0147
for i in range(len(dataGyro['n'])):
	yawGyro.append(dataGyro['y'][i]*dt)

def ComplementaryFilter(yawGyro,angleAccel):
	cleanAngle = []
	loop = 0
	num = []
	if len(yawGyro) > len(angleAccel):
		loop = len(angleAccel) 
	else: 
		loop = len(yawGyro)
	for i in range(loop-1):
		GyroAngle = 0.8 * (yawGyro[i-1] + yawGyro[i])
		AccPhiAngle = 0.2 * angleAccel[i]
		cleanAngle.append(GyroAngle + AccPhiAngle)
		num.append(i)
	return cleanAngle, num

# plot complementary filter result

gaitAngle,num = ComplementaryFilter(yawGyro,newAccel)
plt.title('Complementary Filter Result (Knee Flexion)')
plt.plot(num, gaitAngle, label = 'Gait angle (filtered)', linewidth = 0.7)
#plt.plot(dataGyro['n'], yawGyro, label = 'Yaw Gyroscope (y-axis)', linewidth = 0.7)
#plt.plot(dataAccel['n'], newAccel, label = 'Raw Accelerometer', linewidth = 0.7)
plt.legend()
plt.xlabel('Number of data')
plt.ylabel('Angle (degree)')
plt.show()