quest = "si"
while quest == "si":
    print("bienvenido a calculadora, que desea hacer")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    opcion = int(input("digite una opcion "))
    if opcion == 1:
        num1 = float(input("digite el primer numero a sumar "))
        num2 = float(input("digite el segundo numero a sumar "))
        result = num1 + num2
        if result.is_integer():
            print("resultado: ",int(result))
        else:
            print("resultado: ",result,".")
        quest = input("quiere volver a ejecutar? (si/no)")
    elif opcion == 2:
        num1 = float(input("digite el primer numero a restar "))
        num2 = float(input("digite el segundo numero a restar "))
        result = num1 - num2
        if result.is_integer():
            print("resultado: ",int(result),".")
        else:
            print("resultado: ",result,".")
        quest = input("quiere volver a ejecutar? (si/no)")
    elif opcion == 3:
        num1 = float(input("digite el primer numero a multiplicar "))
        num2 = float(input("digite el segundo numero a multiplicar "))
        result = num1 * num2
        if result.is_integer():
            print("resultado: ",int(result),".")
        else:
            print("resultado: ",result,".")
        quest = input("quiere volver a ejecutar? (si/no)")
    elif opcion == 4:
        num1 = float(input("digite el dividendo "))
        num2 = float(input("digite el divisor "))
        if num1 != 0 or num2 != 0:
            result = num1 / num2
            if result.is_integer():
                result = num1 / num2
                print("resultado: ",int(result),".")
            else:
                print("resultado: ",result,".")
            quest = input("quiere volver a ejecutar? (si/no)")
        else:
            print("no se puede dividir entre cero.")
    else:
        print("opcion invalida")
