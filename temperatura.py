import psutil
data = psutil.sensors_temperatures()
print(data['coretemp'][0])
