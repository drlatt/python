#Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It
#should then accept an arbitrary number of keyword arguments. Call the funcion with the required information and two other name-value pairs, such as a
#color or an optional feature. Your function should work for a call like this one:
#car = make_car('subaru', 'outback', color='blue', tow_package=True)
# use """ for documentation """

#this is a module
def make_car(man_name,mod_name,**other_items):
    """dictionary for a car"""
    car = {}
    car['manufacturer'] = man_name
    car['model'] = mod_name
    for key,value in other_items.items():
        car[key] = value
    return car
