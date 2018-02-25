# Laba lists
numlist=[1, 2, 3, 4, 5, 6, 7]
print (numlist)
numlist.append("Python")
print (numlist)
print(numlist[0])
print(numlist[len(numlist)-1])
print(numlist[1:4])
print(numlist[1:4])
print(len (numlist))
print(numlist.index(6))
numlist.remove('Python')

#Laba Dictionaries
catalog_weather = {
	"city": "Moscow",
	"temperature": 20,
	"wind": "east"
}
print(catalog_weather.get("city"))
catalog_weather["temperature"] = 15
print(catalog_weather.get("temperature"))
print(catalog_weather.get("country", "Can not find it"))
catalog_weather["date"]='27.05.2017'
list_history = [
{'city': 'Tula', 'wind': 'North', 'temperature': 0, 'date': '27.05.2015'},
{'city': 'Moscow', 'wind': 'country', 'temperature': 20, 'date': '27.05.2017'},
]
len(list_history)
list_history.append({'city': 'Omsk', 'wind': 'North', 'temperature': -20, 'date': '27.11.2017'})
list_history.append({'city': 'Sochi', 'wind': 'South', 'temperature': -2, 'date': '27.01.2017'})
list_history.append({'city': 'Piter', 'wind': 'South', 'temperature': 0, 'date': '02.02.2017'})
len(list_history)
print(list_history)
