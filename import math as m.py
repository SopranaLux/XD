import math as m
class Trojmian():

    def __init__(self):
        print()
        print("Program oblicza pierwiastek drugiego stopnia z ax + bx + c = 0")

    def __del__(self):
        print("Obiekt klasy Trójmian został usnięty")
        print("Zakończenie programu")

    def czytaj_dane_i_przetwój_je(self):
        self.a = float(input("podaj liczbe a "))
        
        if self.a == 0:
            print("Zła wartoś współczynnika a ")
            exit()
        else:
            self.b = float(input("Podaj b: "))
            self.c = float(input("Podaj c: "))
            print(f'a = {self.a}, b = {self.b}, c = {self.c}')
        
            delta = self.b * self.b - 4 * self.a * self.c
            if delta < 0:
                print("Brak pierwiastków rzeczywistych")
            elif delta == 0:
                x1 = -self.b / (2 * self.a)
                print(f'trój mian ma jeden pierwiastek rzeczysity {x1}')
            else:
                x1 = (-self.b - m.sqrt(delta)) / 2 * self.a
                x2 = (-self.b + m.sqrt(delta)) / 2 * self.a
                print("Trójmian ma dwa pierwiastki rzeczywiste")
                print(f'x1 = {x1}, x2 = {x2}')
def main():
    trojmian1 = Trojmian()
    trojmian1.czytaj_dane_i_przetwój_je()

    del trojmian1
main()