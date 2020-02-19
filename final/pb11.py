def nom(x):
    if x == 100:
        return 'cent'
    if x >= 10 and x < 20:
        return ['deu', 'onze', 'dotze', 'tretze', 'catorze', 'quinze', 'setze', 'disset', 'divuit', 'dinou'][x - 10]
    
    unitat = ['zero', 'u', 'dos', 'tres', 'quatre', 'cinc', 'sis', 'set', 'vuit', 'nou']
    if x < 10:
        return unitat[x]
    if x == 20:
        return 'vint'

    desenes = ['', '', 'vint-i', 'trenta', 'quaranta', 'cinquanta', 'seixanta', 'setanta', 'vuitanta', 'noranta']
    
    if x % 10 == 0:
        return desenes[x // 10]
    return desenes[x // 10] + '-' + unitat[x % 10]

num = int(input())

for i in range(11):
    print(nom(num), 'x', nom(i), '=', nom(num * i))
