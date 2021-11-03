user ={'name': 'Pete', 'age':40, 'courses':['math', 'it']}
print(type(user))
print(len(user))
#
# print(user.keys())
# print(user.values())
# print(user.items())

#print(user)


#print(user['name'])
#print(user.get('email'))
#
# user["email"]='pete@gmail.com'
# user['name']='Anssi'
# print(user)

#
user.update({'name': 'Juha', 'age': 30, 'email':'juha@mail.fi', 'onko_ajokortti': True})
print(user)

del user['email']
print(user)
#
age = user.pop('age')
print(age)
print(user)
