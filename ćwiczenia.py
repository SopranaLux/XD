def pole(a,b):
    return a * b
def main():
    print('ten program oblicza pole prostokąta')
    a = float(input('Podaj liczbe a '))
    b = float(input('Podaj liczbe b '))
    print(f'{a} * {b} = {pole(a,b)}')
main()