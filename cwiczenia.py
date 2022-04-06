def trojka(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    else:
        return n + trojka(n - 1)
def main():
    for i in range(0, 11):
        print(i, "!=", trojka(i))
main()
import tkinter as tk
