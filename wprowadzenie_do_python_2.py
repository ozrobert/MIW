from file_manager import FileManager
from chuck_norris import ChuckNorris

# ĆWICZENIE 1

a_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
b_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ab_list = []


# ab_list powinna zawierać 0,2,4,6,8 z a_list oraz 1,3,5,7,9 z b_list, jeśli chodzi o indeksy


def ćw1(a_list, b_list):
    ab_list = [i for i, j in enumerate(a_list) if i % 2 == 0]
    ab_list += [i for i, j in enumerate(b_list) if i % 2 == 1]
    return print(ab_list)


ćw1(a_list, b_list)


# ĆWICZENIE 2

def ćw2(data_text):
    length = len(data_text)
    letters = list(data_text)
    big_letters = data_text.upper()
    small_letters = data_text.lower()
    dict = {
        'length': length,
        'letters': letters,
        'big_letters': big_letters,
        'small_letters': small_letters
    }
    return print(dict)


ćw2('Dog')


# ĆWICZENIE 3

def ćw3(text, letter):
    wynik = text.replace(letter, '')
    return print(wynik)


ćw3('kajak', 'k')


# ĆWICZENIE 4

def ćw4(stopnie_celsjusza, temperature_type):
    if temperature_type == 'Fahrenheit':
        wynik = (stopnie_celsjusza * 9 / 5) + 32
        return print(wynik)
    elif temperature_type == 'Rankine':
        wynik = (stopnie_celsjusza * 9 / 5) + 491.67
        return print(wynik)
    elif temperature_type == 'Kelvin':
        wynik = stopnie_celsjusza + 273.15
        return print(wynik)
    else:
        return print('Podano błędny typ temperatury! Proszę podać prawdiłowy. Typy: Fahrenheit, Rankine, Kelvin')


ćw4(4, 'Fahrenheit')
ćw4(4, 'Rankine')
ćw4(4, 'Kelvin')
ćw4(4, '???')


# ĆWICZENIE 5

class Calculator:
    def add(a, b):
        wynik = a + b
        return print(wynik)

    def difference(a, b):
        wynik = a - b
        return print(wynik)

    def multiply(a, b):
        wynik = a * b
        return print(wynik)

    def divide(a, b):
        wynik = a / b
        return print(wynik)


Calculator.add(1, 1)
Calculator.difference(6, 2)
Calculator.multiply(3, 2)
Calculator.divide(16, 2)


# ĆWICZENIE 6

class ScienceCalculator(Calculator):
    def exponentiation(a, b):
        wynik = a ** b
        return print(wynik)


ScienceCalculator.exponentiation(2, 4)


# ĆWICZENIE 7

def ćw7(tekst):
    tekst_od_tyłu = tekst[::-1]
    return print(tekst_od_tyłu)


ćw7('koteł')

# ĆWICZENIE 9

ćw8 = FileManager('ćw8')
ćw8.read_file()
ćw8.update_file('\nupdate')

# ĆWICZENIE 10

print(ChuckNorris('Adam'))
