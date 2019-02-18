city = ""
city_list = []

while city[0:8] != "Waterloo":

    city= input()

    city_list += city.split()

coldest_temperature = 200
coldest_city = ""

for x in range(1, len(city_list), 2):

    if int(city_list[x]) < coldest_temperature:

        coldest_temperature = int(city_list[x])
        coldest_city = city_list[x - 1]

print(coldest_city)