rivers = {'nile':'egypt',
          'sepik':'new guinea',
          'mississippi':'united states of america',
          'volga':'russia',
          'zambezi':'zambia',
          'danube':'germany',
          'yangtze':'china',
          'nile':'egypt',
          'amazon':'brazil',
          }

for river, country in rivers.items():
    message = "The " + str(river.title()) + " runs through " + str(country.title())
    print(message)

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
