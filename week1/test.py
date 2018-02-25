

catalog_1 = {
	"city": "Moscow",
	"temperature": "cold",
	"wind": "10 m/s"
}
catalog_2 = {
	"city": "Milan",
	"temperature": "+15 C",
	"wind": "0 m/s"
}
catalog_3 = {
	"city": "Vilnius",
	"temperature": "0 C",
	"wind": "5 m/s"
}
catalog_4 = {
	"city": "Berlin",
	"temperature": "2 C",
	"wind": "15 m/s"
}

catalog_names = {
	"Misha": catalog_1,
	"Vasya": catalog_2,
	"Mitya": catalog_3,
	"Egor": catalog_4
}

print ("Hello!")
name = input("Please, specify the name? ")

catalog_0 = {
	"We are search": name,
	"Sorry": "We can not find it"
}

parametres = catalog_names.get(name, catalog_0)

for key, value in parametres.items():
	print ('{}: {}'.format(key, value))
