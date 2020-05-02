# ĆWICZENIE 1

zmienna = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

# ĆWICZENIE 2

imie = "Robert"
nazwisko = "Ożóg"

litera_1 = imie[2]
litera_2 = nazwisko[3]

liczba_liter_1 = zmienna.count(litera_1)
liczba_liter_2 = zmienna.count(litera_2)

print("W tekście jest {0} liter {1} oraz {2} liter {3}".format(liczba_liter_1, litera_1, liczba_liter_2, litera_2))

# ĆWICZENIE 3

print('{:>20}'.format('przykład 1'))
print('{:_<20}'.format('przykład 2'))
print('{:^20}'.format('przykład 3'))
print('{:.5}'.format('przykład 4'))
print('{:f}'.format(3.141592653589793))

# ĆWICZENIE 4

zmienna_typu_string = "abc"

print(dir(zmienna_typu_string))
# help(zmienna_typu_string.isidentifier())

# ĆWICZENIE 5

print((nazwisko[::-1]).capitalize(), imie[::-1].capitalize())

# ĆWICZENIE 6

lista = list(range(1, 11))

nowa_lista = lista[5:]
lista = lista[:5]

print(lista)
print(nowa_lista)

# ĆWICZENIE 7

lista = lista + nowa_lista
lista.insert(0, 0)

lista_kopia = lista.copy()
lista_kopia.sort(reverse=True)

print(lista_kopia)

# ĆWICZENIE 8

lista_studentów_1 = ((112233, "Andrzej Mróz"),
                     (445566, "Dawid Wiśniewski"),
                     (778899, "Michał Kowalski"))

print(lista_studentów_1)

# ĆWICZENIE 9

lista_studentów_2 = {
    112233: {'imie': "Andrzej",
             'nazwisko': "Mróz",
             'wiek': 23,
             'adres email': "mróz@gmail.com",
             'rok urodzenia': 1997,
             'adres': "10-336 Olsztyn, ul. Reymonta Władysława 24 m. 5"},
    445566: {'imie': "Dawid",
             'nazwisko': "Wiśniewski",
             'wiek': 24,
             'adres email': "wiśniewski@gmail.com",
             'rok urodzenia': 1996,
             'adres': "11-041 Olsztyn, ul. Bociania 2 m. 8"},
    778899: {'imie': "Michał",
             'nazwisko': "Kowalski",
             'wiek': 26,
             'adres email': "kowalski@gmail.com",
             'rok urodzenia': 1994,
             'adres': "10-154 Olsztyn, ul. Bursztynowa 10 m. 21"}}

print(lista_studentów_2.values())

# ĆWICZENIE 10

numery = ["510143255", "500672271", "500672271", "500672271"]
numery = set(numery)

print(numery)

# ĆWICZENIE 11

for x in range(1, 11):
    print(x)

# ĆWICZENIE 12

for x in range(100, 19, -5):
    print(x)

# ĆWICZENIE 13

for student in lista_studentów_2:
    info = lista_studentów_2[student]
    print('Nazywam się', info['imie'], info['nazwisko'] + '.', 'Mój rok urodzenia to', str(info['rok urodzenia']) + ',',
          'więc mam', info['wiek'], 'lat. Mój adres zamieszkania', info['adres'] + '.',
          'W razie kontaktu, proszę pisać na', info['adres email'])
