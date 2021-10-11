names = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
import re

def isDEorder1(name):
    e = name.rfind('e')
    d = name.find('d')
    x = e - d
    return x == 2


def digits(i):
    numList = re.findall('[0-9]+', i)
    for j in numList:
        if len(j) >= 3:
            print('8:', i)


for i in names:
    if '5' in i:
        print("1:", i)
    if 'd' in i or 'e' in i:
        print("2:", i)
    if i.find('d') < i.find('e') > -1:
        print("3:", i)
    if isDEorder1(i):
        print("4:", i)
    if i.find('d') and i.find('e') > -1:
        print("5:", i)
    if i.startswith('x') or i.startswith('y'):
        print("6:", i)
    if (i.startswith('x') or i.startswith('y')) and i.endswith('e'):
        print("7:", i)
    if i.endswith('da') or i.endswith('dr') or i.endswith('dp'):
        print("9:", i)
    digits(i)







