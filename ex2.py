busca = 34
num1 = 0
num2 = 1
termo = 0

if busca == 0 or busca == 1:
    print("Numero faz parte da sequencia de Fibonacci")
else: 
    while termo < busca:
        termo = num1 + num2
        if termo > busca:
            print("Numero nao faz parte da sequencia de Fibonacci")
            break    
        elif termo == busca:
            print("Numero faz parte da sequencia de Fibonacci")
            break
        num1 = num2
        num2 = termo
