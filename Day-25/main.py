with open("weather_data.csv") as weather_data:
    # content=weather_data.read()
    content1=weather_data.readlines()
    print(content1)
import csv
with open("weather_data.csv") as data_file:
    data=csv.reader(data_file)
    temprature=[]
    for row in data:
      if row[1]!="temp":
          temprature.append(row[1])
    print(temprature)         