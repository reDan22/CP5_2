try:
    print("Введите целое положительное число: ")
    chislo = int(input())

    print("Введите целевую систему счисления(2 или 8): ")
    sistema_chislenia = int(input())

    if sistema_chislenia == 2:
        otvet = ""
        while chislo > 0:
            otvet = str(chislo % 2) + otvet
            chislo = chislo // 2
        print("Ваше число в двоичной системе счисления:")
        print(otvet)
    elif sistema_chislenia == 8: 
        otvet = ""
        while chislo > 0:
            otvet = str(chislo % 8) + otvet
            chislo = chislo // 8
        print("Ваше число в восьмеричной системе счисления:")
        print(otvet)
    else:
        print("Введите допустимую систему счисления(2 или 8)")
except ValueError:
    print("Введите целое число")
    quit()