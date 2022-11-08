'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
V Pythonu se n-tice píší s kulatými závorkami.

'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# Chcete-li vytvořit n-tici pouze s jednou položkou, musíte za položku přidat čárku, pokud Python nerozpozná proměnnou jako n-tici.
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot
#
# Rozsah indexů můžete určit určením, kde začít a kde ukončit rozsah.
# Při zadávání rozsahu bude vrácená hodnota nová n-tice se zadanými položkami.
print(f'chars[2:5]: {chars[2:5]}')

# Negativní indexování znamená začátek od konce, -1 odkazuje na poslední položku, -2 odkazuje na předposlední položku atd.
# Pokud chcete zahájit hledání od konce n-tice, zadejte záporné indexy:
# Tento příklad vrátí položky z indexu -4 (zahrnuto) do indexu -1 (vyloučeno)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# Chcete-li zjistit, kolik položek má n-tice, použijte metodu len():
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')