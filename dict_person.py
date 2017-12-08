ljames = {'first_name':'lebron',
          'last_name':'james',
          'age':'30',
          'location':'cleveland',
          }
scurry = {'first_name':'steph',
          'last_name':'curry',
          'age':'28',
          'location':'golden state',
          }
kirving = {'first_name':'kyrie',
          'last_name':'irving',
          'age':'29',
          'location':'boston',
          }
people = [ljames,scurry,kirving]

for person in people:
    for key,value in person.items():
        fullname = person['first_name'] + " " + person['last_name']
    print("\n" + fullname.title())
    print(person['location'].title())
    print(str(person['age']))
