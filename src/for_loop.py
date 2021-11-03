#
numerot = [5,3,1,2,7,9]
# print(len(numerot))
# print("*************")
for i in range(10, 0, -1): #start, stop,step
   # for(int i=0; i<6; i++) # c versio
    print(i)

    #print(numerot[i])




#
# for i in numerot:
#     print(i)

# for i in  range(0, len(numerot)):
#     #print(numerot[i])
#    print('alkio',i,'on', numerot[i])

# count = 0
# for num in numerot:
#     print('alkio', count, 'on', num)
#     count +=1
#
# for j, num in enumerate(numerot):
#     print('alkio',j,'on', num)





#
user ={'name': 'Pete', 'age':40, 'courses':['math', 'it']}

for key in user.keys():

     print(key)
     value = user[key]
     print(key,':',value)