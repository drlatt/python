fav_languages = {'chichi':'javascript',
                 'excellence':'golang',
                 'joseph':'java',
                 'michael':'php',
                 'bayo':'python',
                 'neymar':'nodejs'}
take_poll = ['bayo','patrick','kene','chukwudi','chichi']

for person in take_poll:
    if person in fav_languages.keys():
        message = str(person.title()) + ", thanks for taking the poll."
        print(message)
    else:
        message = str(person.title()) + ", kindly take the poll."
        print(message)
