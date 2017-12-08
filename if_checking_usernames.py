current_users = ['Martha', 'BOLA', 'tess', 'tina', 'mary']
new_users = ['ken', 'bolaji', 'kane', 'martha', 'bola']
current_users_lower = []
for user in current_users:
    user = user.lower()
    current_users_lower.append(user)
print(current_users_lower)

for new_user in new_users:
    if new_user in current_users_lower:
        message = "Enter a new username, " + new_user.title() + " has been taken"
        print(message)
    else:
        message = "The username, " + new_user.title() + " is available."
        print(message)
