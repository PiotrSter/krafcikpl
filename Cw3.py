import file_manager
#Zad 1
def list(a_list = [], b_list = []):
    list_ab = []
    for i in a_list:
        if i % 2 == 0:
            list_ab.append(i)
    for i in b_list:
        if i % 2 == 1:
            list_ab.append(i)
    return print(list_ab)
list(a_list = [2,7,8,11,20], b_list = [3,4,9,12,21])
#Zad 2
"""def data(data_text):
    lenght = len(data_text)
    letters = [data_text[1:1]]
    big_letters = data_text.upper()
    small_letters = data_text.lower()
    slownik = {lenght: 1, letters: 2, big_letters:3, small_letters :4}
    return print(slownik)
data('Piotr')"""
#Zad 3
"""def usun(text, letter):
    for letter in text:
        if letter == text:
            text.remove(letter)
    return print(text)"""
#Zad 4
def termometr(temperature_type):
    fahrenheit = 33.8
    kelwin = 274.15
    rankin = 493.47
    if temperature_type > 0:
        for i in range(0, temperature_type):
            celsjusz_fahrenheit = fahrenheit + 1.8 * i
        for i in range(0, temperature_type):
            celsjusz_kelwin = kelwin + 1 * i
        for i in range(0, temperature_type):
            celsjusz_rankin = rankin + 1.8 * i
    else:
        celsjusz_fahrenheit = 32
        celsjusz_kelwin = 273.15
        celsjusz_rankin = 491.67

    return print(f"{temperature_type} Celsjusza to {round(celsjusz_fahrenheit,2)} Fahrenheita, "
                 f"{round(celsjusz_kelwin,2)} Kelwina, {round(celsjusz_rankin,2)} Rankina")
termometr(23)
#Zad 5
class Calculator:
    def __init__(self, liczba1, liczba2):
        self.liczba1 = liczba1
        self.liczba2 = liczba2
    def add(self):
        return self.liczba1 + self.liczba2
    def difference(self):
        return self.liczba1 - self.liczba2
    def multiply(self):
        return  self.liczba1 * self.liczba2
    def divide(self):
        return  self.liczba1 / self.liczba2
#Zad6
class ScienceCalculator(Calculator):
    def exponentiation(self):
        return self.liczba1 * self.liczba1
#Zad7
def backwards(text):
    return print(f"{text[::-1]}")
backwards("kot")









