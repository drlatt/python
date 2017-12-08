age = 410
if age < 2:
    stage = 'baby'
elif age == 2 or age < 4:
    stage = 'toddler'
elif age == 4 or age < 13:
    stage = 'kid'
elif age == 13 or age < 20:
    stage = 'teenager'
elif age == 20 or age < 65:
    stage = 'adult'
elif age > 65:
    stage = 'elder'

#print("You are a " + stage + ".")
if stage in ['baby', 'toddler', 'kid', 'teenager']:
    print("You are a " + stage + ".")
elif stage in ['adult', 'elder']:
    print("You are an " + stage + ".")
