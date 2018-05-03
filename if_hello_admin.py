#usernames = ['ken', 'admin', 'eminem', 'mike', 'akon']
#declare list
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            message = "Hello " + username.title() + ", would you like to see a status report."
            print(message)
        else:
            message = "Hello " + username.title() + ", thank you for logging in again."
            print(message)
else:
    print("We need to find some users!")
