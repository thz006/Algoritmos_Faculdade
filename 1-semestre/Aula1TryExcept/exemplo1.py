try:
    while True:
        a = int(input("digite uma palavra: "))
except ValueError:
    print("apenas numeros")
except:
    print("erro desconhecido")
finally:
    b = int(input("numero: "))