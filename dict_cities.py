jos = {'country':'nigeria',
       'population':'5,000,000',
       'fact':'home of peace and tourism',
       }
lagos = {'country':'nigeria',
       'population':'25,000,000',
       'fact':'centre of excellence',
       }
abuja = {'country':'nigeria',
       'population':'4,000,000',
       'fact':'centre of unity',
       }
cities = [jos,lagos,abuja]
for city in cities:
    for key,value in city.items():
        country = "Country is " + city['country'].title()
        population = "Population is " + city['population']
        fact = "It is the " + city['fact']
    print("\n" + country + "\n" + population + "\n" + fact)
