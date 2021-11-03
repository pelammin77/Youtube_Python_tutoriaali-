from collections import defaultdict

user ={'name': 'Pete', 'age':40, 'courses':['math', 'it']}
#print(user['email'])








d_dict = defaultdict(lambda : "Tuntematon arvo", user)

print(d_dict['email'])


d_dict_2 = defaultdict(lambda :"Tuntematon arvo", {'name': 'Pete', 'age':40, 'courses':['math', 'it']})


print(d_dict_2['name'])