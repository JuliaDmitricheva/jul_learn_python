catalog_fio = {
	"first_name": "Mikhail",
	"last_name": "Korneev"
}
user_info = catalog_fio
print(user_info['first_name'])
catalog_fio['first_name']= input("Please, specify the first name? ")
catalog_fio['last_name']= input("Please, specify the last name? ")
for key, value in catalog_fio.items():
	print ('The {} is {}'.format(key, value))