import re

"""

    \d = numero
    \D = kaikki paitsi numero 
    \s = välilyönti 
    \S = kaikki paitsi välilyönti 
    \w = mikä tahansa kirjain 
    \W = kaikki muut paitsi kirjain 
    . = kaikki merkit paitsi rivinvaihto(newline)
    \b = tyhjät sanojen välillä 
    \. = piste 
    \?

{1,3} = montako merkkiä numerossa on 0-999
+ = match 1 tai enemmän
? = match 0 tai 1
* = match 0 tai enemmän repetitions
$ = match merkkijonon lopusta 
^ = match merkkijonon alusta 
| = match tai 
[] = joukon pituus [a-h]


"""

#print(re.search("ab?c", "abbbbbc"))


mjono = '''
 Risto on 8. Petri on 43 vuotta vanha ja Keke on 36 vanha. Yrjö on jo 103  
'''

iat = re.findall(r'\d{1,3}', mjono)
nimet = re.findall(r'[A-Z][a-z]*', mjono)
nimet2 = re.findall(r'[A-ZÖÄ][a-zöä]*', mjono, re.UNICODE)

print(nimet2)
print(iat)

# regex = re.compile(r"[^\W\d_]", re.UNICODE)
# m = regex.findall("aäÄA12_")
# print(m)