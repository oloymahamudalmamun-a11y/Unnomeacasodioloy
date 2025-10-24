numero1=int(input("inserisci il tuo numero:"))
numero2=int(input("inserisci il tuo numero:"))
numero3=int(input("inserisci il tuo numero:"))
if numero1<numero2<numero3:
    print(numero3,numero2,numero1)
if numero2>numero1<numero3:
    print(numero3,numero2,numero1)
if numero3>numero2>numero1:
    print(numero3,numero2,numero1)
if numero2<numero3>numero1:
    print(numero3,numero2,numero1)
if numero1<numero3>numero2:
    print(numero3,numero2,numero1)