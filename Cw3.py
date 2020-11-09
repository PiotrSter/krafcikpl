import file_manager

#Zad1
def list(a_list = [], b_list = []):
    c_list = []
    for i in a_list:
        if i % 2 == 0:
            c_list.append(i)
    for i in b_list:
        if i % 2 != 0:
            c_list.append(i)
    return print(c_list)
list(a_list = [2,4,6,7,9], b_list = [1,3,10])

#Zad2
def data(data_text):
    lenght = len(data_text)
    letters = []
    letters[:0] = data_text
    big_letters = data_text.upper()
    small_letters = data_text.lower()
    dict_1 = {
        "Text": {
        "Lenght": lenght,
        "Letters": letters,
        "big letters": big_letters,
        "small letters": small_letters,
        }
    }
    return print(dict_1)

data("Fajny Tekst")

#Zad3
def delete(text, letter):
    newstr = text.replace(letter, "")
    return print(newstr)

delete("Tekst", "s")

#Zad4
def TempCalc(celsius):
    #fahrenheit = 33.8
    #kelwin = 274.15
    rankin = 493.47
    if celsius > 0:
        fahrenheit = (celsius * 9/5) + 32
        rankin = (celsius + 273.15) * 9 / 5
        kelvin = celsius + 273.15
    else:
        fahrenheit = 32
        rankin = 491.67
        kelvin = 273.15


    return print(f"{celsius}° Celcjusza to {round(fahrenheit,2)}° Farenhaita, "
                 f"{round(rankin,2)}° Rankina, {round(kelvin,2)}° Kelwina")

TempCalc(31)

#Zad5
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def diff(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

#Zad6
class ScienceCalculator(Calculator):
    def exp(self):
        return self.a ** self.b

#Zad7
def tenet(text):
    return print(f"{text[::-1]}")
tenet("ROTAS OPERA TENET AREPO SATOR") #Kwadrat Sator-Rotas
tenet("Koteł")

#Zad8
class_instance = file_manager.FileManager("Cw3_zad8")
class_instance.update_file("Python")
class_instance.read_file()