import numbers
class PoleProstokonta:
    def __init__(self):
        print("Program oblicza pole prostokata")
    def __del__(self):
        print()
        print("obiekt klasy prostokąta został usunięty")
    def dane(self):
        self.a = float(input("podaj bok a"))
        self.b = float(input("podaj bok b"))
    def przetworz_Dane(self):
        self.pole = self.a * self.b
        return self.pole
    def wynik(self):
        print(f'Pole prostokąta wynosi {self.pole}')
def main():
    pole1 = PoleProstokonta()
    
    pole1.dane()
    pole1.przetworz_Dane()
    pole1.wynik()

    del pole1
main()