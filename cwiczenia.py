def NWD(x, y):
    if x % y == 0:
        return y
    else:
        return NWD(y, x % y)
def main():
    a = int(input("podaj liczbe a "))
    b = int(input("podaj liczbe b "))
    print(f'NWD({a}, {b}) = {NWD(a,b)}')

main()