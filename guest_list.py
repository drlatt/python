guest_list = ['ken','iyabo','chinonso','margaret']
message = "Hello " + guest_list[0].title() + ", you're invited to my black tie event."
print(message)

guest_not_coming = ['ken']
not_coming = guest_not_coming[0].title() + " decided not to come."
print(not_coming)

guest_list[0] = "cynthia"
print(guest_list)

print("Found a bigger dinner table")
guest_list.insert(0, "tolu")
guest_list.insert(3, "kemi")
guest_list.append("gerald")
print(guest_list)

print("Sorry guys, only 2 people can come for dinner")
removed_guest = "Sorry, " + guest_list.pop() + " can't come anymore"
print(removed_guest)

print(guest_list)

del guest_list[0]

print(guest_list)
