#!/usr/bin/python3
'''
#text = "Je dois faire des sauvegardes régulières de mes fichiers."
#print (text*500)

'''

'''

pair =[]
for a in range (0,1000, 2):
        pair.append(a)
        print(pair)
        impair = [n + 1 for n in  pair ]
        print (impair)

'''


'''
def table(nb, max=10):

    1 * nb
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

if __name__ == "__main__":
    table(13)
'''

'''
name = input('Entrez un mot: ')
a = 0
b = 0

while a < len(name):
    if name[a] == 'e':
        b = b + 1
    a = a + 1

print(a)



'''