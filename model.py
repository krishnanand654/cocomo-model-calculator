# Cocomo model
import os
from msvcrt import getch
# output E, D, No.of Person, Productivity
Kloc = 0
x = 0
while(x != 2):
    print("\n-----------COCOMO CALCULATOR-----------")
    print("\n1. Calculator \n2. Exit")
    x = int(input("\nEnter : "))
    if x == 1:
        # input KLOC
        Kloc = int(input("\nEnter Thousand of lines of estimated code : "))
    if x == 2:
        exit(0)
    # switch
    c = 0
    while(c != 4):
        # Organic
        os.system('cls')
        print("\nGiven KLOC = ", Kloc)
        print("\nSelect Mode\n\n")
        print("1. Orgainc \n2. Semi-Detatched \n3. Embedded \n4. Go back")
        c = int(input("\nEnter mode : "))
        if c == 1:
            os.system('cls')
            print("\nSelected mode is Organic\n")
            print("KLOC = ", Kloc)
            print("\nvariables : a = 2.4 \t b = 1.05 \t c = 2.5 \t d = 0.38\n\n")
            E = 2.4 * pow(Kloc, 1.05)
            D = 2.5 * pow(E, 0.38)
            prsn = E/D
            pty = Kloc/E
            print("Effort = ", E)
            print("Duration = ", D)
            print("No.of Staff = ", prsn)
            print("productivity = ", pty)
            print("\n\nPress any key to go back")
            getch()

        # Semi-Detatched
        if c == 2:
            os.system('cls')
            print("\nSelected mode is Semi-Detached\n")
            print("KLOC = ", Kloc)
            print("\nvariables : a = 3.0 \t b = 1.12 \t c = 2.5 \t d = 0.35\n\n")
            E = 3.0 * pow(Kloc, 1.12)
            D = 2.5 * pow(E, 0.35)
            prsn = E/D
            pty = Kloc/E
            print("Effort = ", E)
            print("Duration = ", D)
            print("No.of Staff = ", prsn)
            print("productivity = ", pty)
            print("\n\nPress any key to go back")
            getch()

        # Embedded
        if c == 3:
            os.system('cls')
            print("\nSelected mode is Semi-Detached\n")
            print("KLOC = ", Kloc)
            print("\nvariables : a = 3.6 \t b = 1.20 \t c = 2.5 \t d = 0.32\n\n")
            E = 3.6 * pow(Kloc, 1.20)
            D = 2.5 * pow(E, 0.32)
            prsn = E/D
            pty = Kloc/E
            print("Effort = ", E)
            print("Duration = ", D)
            print("No.of Staff = ", prsn)
            print("productivity = ", pty)
            print("\n\nPress any key to go back")
            getch()
        if c == 4:
            os.system('cls')
            break
