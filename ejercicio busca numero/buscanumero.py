

lista = []

for numero in range(10):
    valorUsuario = "0"
    valor = 0
    while valorUsuario.isdigit():
        try:
            valor = int(input("Dime un numero: "))
            break
        except:
            print("no puede ser cadena")
            valorUsuario = "0"
            
    lista.append(valor)

print(lista)


NumeroQueBusca = (input("¿Que numero estas bucando? "))
if NumeroQueBusca in lista:
    print("el numero, {} ,se encuentra en la lista".format(NumeroQueBusca))
elif NumeroQueBusca.isnumeric() is not lista:
    print("el numero debe ser un entero")
else:
    print("el numero {} no se encuentra en la lista".format(NumeroQueBusca))
