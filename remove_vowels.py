# remove all the vowels in the words and return them with the first letter capitalized
states = ['Lagos','Abuja','Kebbi','Ebonyi','Ekiti']
vowels = ['a','e','i','o','u']
output = []

for state in states:
    new_state = list(state.lower())

    for vowel in vowels:
        while True:
            try:
                new_state.remove(vowel)
            except:
                break
    output.append(''.join(new_state).capitalize())

print(output)


import re
states = ['Lagos','Abuja','Kebbi','Ebonyi','Ekiti']
d = [re.sub(r'[aeiou]+','',x.lower()) for x in states]
print(d)
