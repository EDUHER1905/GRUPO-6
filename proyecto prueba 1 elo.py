import getpass
registroUsuario="Registrar usuarios.txt","a+"
def usuarioNuevo():
    file=open("Registrar usuarios.txt","a+")
    intentos=0
    max_intentos=3
    while intentos<3 :
    
        cedula = input("Ingrese su cédula de identidad (debe tener 9 dígitos): ")
        if len(cedula) == 9:
             print("Cédula válida.")
             break
        else:
            intentos+=1
            print("Intente de nuevo\nError: La cedual debe tener (9 digitos)")
    else:
        print("Usted excedió el numero de intentos ")
    nombre=input("Ingrese su nombre: \n")
    while True:
        pin=getpass.getpass("Ingrese el PIN que desea para su cuenta bancaria:\n")
        if len(pin)==4:
            print("PIN valido")
            break
        
        else:
            print("Su PIN debe de ser de 4 digitos,intente de nuevo")
    print("Ingrese nuevamente el PIN para auntenticar")
    while True:
        aunte_Pin=getpass.getpass("Ingrese el PIN para auntenticar:\n")
        if aunte_Pin==pin:
            print("Se auntentico correctamente")
            break
        else:
            print("El PIN no es igual,Intente de nuevo")
    print("Para poder terminar con el registro debe depositar 100.000 colones  o otra moneda pero la equivalencia tiene que ser 100.000 como minimo")
    #Depositdo obligatorio
    tipoCambioDolar=548.48
    tipoCambioBit=14981000.98
    print("Para poder registrarse en el banco se debe realizar el depósito mínimo de 100 000 colones o equivalente en alguna otra moneda(bitcoin o dolares)")
    while True:
            tipoMoneda=input("Que tipo de moneda desea: \n1-colones\n2-Dolares\n3-Bitcoin\n")
            if tipoMoneda=="1":
                while True:
                    colones=float(input("Ingrese el monto a depositar solicitado(Se debe utilizar un punto para separar a los decimales):\n"))
                    if colones>=100.000:
                        print("Monto correcto")
                        break
                    else:
                        print("Monto equivocado,no cumple con el minimo de 100 000 Colones")
                break
            if tipoMoneda=="2":     
                while True:
                    dolares=float(input("Ingrese su monto en dolares(Tiene que ser equivalente a 100.000 Colones):\n"))
                    cambio=dolares*tipoCambioDolar
                    if cambio>=100000:
                        print("Monto correcto")
                        break
                    else:
                        print("Monto equivocado,no cumple con el minimo de 100 000 Colones")
                break
            if tipoMoneda=="3":
                while True:
                    bitcoin=float(input("Ingrese su monto en bitcoin(Tiene que ser equivalente a 100.000 Colones):\n"))
                    cambio=bitcoin*tipoCambioBit
                    if cambio>=100000:
                        print("Monto correcto")
                        break
                    else:
                        print("Monto equivocado,no cumple con el minimo de 100 000 Colones")
                break
            break
    file.write("Cedula: {} , Nombre: {} , saldo: {} \n".format(cedula,nombre,colones))
    file.close()


def usuarioRegistrado():
    
    with open("Registrar usuarios.txt", "r") as file:

    
        datosUsuario=file.readlines()
        datosUsuario= [dato.strip() for dato in datosUsuario]
        cuentas = []

        for dato in datosUsuario:
            cuentas.append(dato)
    
    file.close()
    print(cuentas)
    


def retirarDinero():
    cuentas = [
    {'cuenta': 'Colones', 'saldo': 500000, 'moneda': 'CRC'},
    {'cuenta': 'Dólares', 'saldo': 1000, 'moneda': 'USD'},
    {'cuenta': 'Bitcoin', 'saldo': 2, 'moneda': 'BTC'}
]
    
    for i, cuenta in enumerate(cuentas):
        print(f"{i+1}. {cuenta['cuenta']} ({cuenta['moneda']})")


    opcion = int(input("¿De cual cuenta desea retirar dinero? "))
    cuenta = cuentas[opcion-1]

    print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
    monto = float(input("¿Cuanto dinero desea retirar? "))

    for i in range(3):
        if monto > cuenta['saldo']:
            print("El monto solicitado es mayor al saldo actual.")
            monto = float(input(f"Intente de nuevo ({i+1}/3): "))
        else:
            cuenta['saldo'] -= monto
            print(f"Se retiraron {monto} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
            print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
            break
    else:
        print("Ha excedido el número máximo de intentos. Regresando al menú principal...")


def depositar():
     with open('cuenta.txt', 'r') as file:
          cuenta, saldo = file.readline().strip().split(',')
          montodeposito = float(input('Ingrese el monto del depósito: '))
          nuevosaldo = float(saldo) + montodeposito
with open('cuenta.txt', 'w') as file:
     file.write(f'{"cuenta"},{"nuevosaldo"}')
print(f'Se ha realizado un depósito de ${"montodeposito"}. Su saldo actual es de ${"nuevosaldo"}.')

     

def verSaldo():
    cuentas = [
    {'cuenta': 'Colones', 'saldo': 500000, 'moneda': 'CRC'},
    {'cuenta': 'Dólares', 'saldo': 1000, 'moneda': 'USD'},
    {'cuenta': 'Bitcoin', 'saldo': 2, 'moneda': 'BTC'}
]
    for i, cuenta in enumerate(cuentas):
        print(f"{i+1}. {cuenta['cuenta']} ({cuenta['moneda']})")
    opcion = int(input("¿ cual cuenta desea ver? "))
    cuenta = cuentas[opcion-1]
    print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
        

   


    with open("Registrar usuarios.txt", "r") as file:

    
        datosUsuario=file.readlines()
        datosUsuario= [dato.strip() for dato in datosUsuario]
        

        
       
        file.close()
        print("datos usuarios")
        print(datosUsuario)    
 
def pagar_servicios():
     saldo_colones = 100000
saldo_dolares = 1000
saldo_bitcoin = 0.01
servicios_activos = {
    'Electricidad': True,
    'Agua': False,
    'Telefonía': True,
    'Internet': True,
    'Impuestos': False,
    'Colegios Profesionales': False,
    'Tarjeta de crédito': True
}
precios_servicios = {
    'Electricidad': {
        'colones': 20000,
        'dolares': 40,
        'bitcoin': 0.004
    },
    'Agua': {
        'colones': 15000,
        'dolares': 30,
        'bitcoin': 0.003
    },
    'Telefonía': {
        'colones': 10000,
        'dolares': 20,
        'bitcoin': 0.002
    },
    'Internet': {
        'colones': 25000,
        'dolares': 50,
        'bitcoin': 0.005
    },
    'Impuestos': {
        'colones': 50000,
        'dolares': 100,
        'bitcoin': 0.01
    },
    'Colegios Profesionales': {
        'colones': 75000,
        'dolares': 150,
        'bitcoin': 0.015
    },
    'Tarjeta de crédito': {
        'colones': 30000,
        'dolares': 60,
        'bitcoin': 0.006
    }
}
tipos_cuenta = ['colones', 'dolares', 'bitcoin']
valor_referencia_dolares = 550  
valor_referencia_bitcoin = 50000  

def menu_servicios():
    print('Seleccione un servicio:')
    for servicio, activo in servicios_activos.items():
        if activo:
            print(f'- {servicio}')
    servicio_seleccionado = input('Servicio: ')


def pinEliminar():
    while True:
        pin=getpass.getpass("Ingrese el PIN de su cuenta bancaria:\n")
        if len(pin)==4:
            print("PIN valido")
            break
        
        else:
            print("Su PIN debe de ser de 4 digitos,intente de nuevo")
    print("Ingrese nuevamente el PIN para confirmar la eliminacion de usuario")
   
    while True:
        aunte_Pin=getpass.getpass("Ingrese el PIN para auntenticar:\n")
        if aunte_Pin==pin:
            print("Se auntentico correctamente")
            break
        else:
            print("El PIN no es igual,Intente de nuevo")
    
    
def divisas():
    compraDolar=525.50
    ventaDolar=539.00
    compraColones=570.22
    ventaColones=601.04
    bitcoin=0.0000069
        


    cuentas = [ ['cuenta', 'saldo', 'moneda'],
            ['Colones', 500000, 'CRC'],
            ['Dólares', 10000, 'USD'],
            ['Bitcoin', 29103223, 'BTC']
    ]
        
    opcion=input("¿Qué operación desea realizar?\n1. Compra de colones\n2. Venta de colones\n3. Compra de dólares\n4. Venta de dólares\n5. Compra de bitcoin\n6. Venta de bitcoin\n7. Salir\n")
    if opcion=="1":
        #compra de dolares
            cuentas = [
                    {'cuenta': 'Dólares', 'saldo': 10000, 'moneda': 'USD'},
                {'cuenta': 'Bitcoin', 'saldo': 29103223, 'moneda': 'BTC'}
            ]
            for i, cuenta in enumerate(cuentas):
                print(f"{i+1}. {cuenta['cuenta']} ({cuenta['moneda']})")
            opcion1 = int(input("¿De cual cuenta desea comprar colones? "))
            cuenta = cuentas[opcion1-1]
            if opcion1==1:
                print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                cantidad=int(input(f"Cuantos dolares desea cambiar a colones?\n"))
                if cantidad > cuenta['saldo']:
                        print("El monto solicitado es mayor al saldo actual.")
                else:
                    cuenta['saldo'] -= cantidad
                    print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                    print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                    total=cantidad*compraColones
                    print(f"Se compraron {total} colones\n")
                    resultadoFinal=cuentas[1][1]+total
                    print(f"Su cuenta en colones quedo con {resultadoFinal} colones")
                


            elif opcion1==2:
                cuentas = [ ['cuenta', 'saldo', 'moneda'],
                        ['Colones', 500000, 'CRC'],
                        ['Dólares', 10000, 'USD'],
                        ['Bitcoin', 29103223, 'BTC']
                        ]
                print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                cantidad=float(input(f"Cuantos bitcoins desea cambiar a colones?\n"))
                if cantidad > cuenta['saldo']:
                        print("El monto solicitado es mayor al saldo actual.")
                else:
                    cuenta['saldo'] -= cantidad
                    print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                    print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                    total=cantidad*compraColones
                    print(f"Se compraron {total} colones\n")
                    resultadoFinal=cuentas[1][1]+total
                    print(f"Su cuenta en colones quedo con {resultadoFinal} colones")


        
        

                
    elif opcion=="2":
        #venta de colones
        cuentas = [
                    {'cuenta': 'Dólares', 'saldo': 10000, 'moneda': 'USD'},
                {'cuenta': 'Bitcoin', 'saldo': 29103223, 'moneda': 'BTC'}
            ]
        for i, cuenta in enumerate(cuentas):
                        print(f"{i+1}. {cuenta['cuenta']} ({cuenta['moneda']})")
        opcion1 = int(input("¿a que cuenta iran los fondos? "))
        cuenta = cuentas[opcion1-1]
        if opcion1==1:
                        print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                        cantidad=int(input(f"Cuantos colones desea vender?\n"))
                        if cantidad > cuenta['saldo']:
                                print("El monto solicitado es mayor al saldo actual.")
                        else:
                            cuentas = [ ['cuenta', 'saldo', 'moneda'],
                            ['Colones', 500000, 'CRC'],
                            ['Dólares', 10000, 'USD'],
                            ['Bitcoin', 29103223, 'BTC']
                            ]
                            cuenta['saldo'] -= cantidad
                            print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                            print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                            total=cantidad*ventaColones
                            print(f"Se vendieron {total} colones\n")
                            resultadoFinal=cuentas[1][1]-total
                            print(f"Su cuenta en dolares quedo con {resultadoFinal} colones")
        elif opcion1==2:
                        cuentas = [ ['cuenta', 'saldo', 'moneda'],
                            ['Colones', 500000, 'CRC'],
                            ['Dólares', 10000, 'USD'],
                            ['Bitcoin', 29103223, 'BTC']
                            ]
                        print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                        cantidad=float(input(f"Cuantos colones desea vender?\n"))
                        if cantidad > cuenta['saldo']:
                                print("El monto solicitado es mayor al saldo actual.")
                        else:
                            cuenta['saldo'] -= cantidad
                            print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                            print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                            total=cantidad*ventaColones
                            print(f"Se vendieron {total} colones\n")
                            resultadoFinal=cuentas[1][1]-total
                            print(f"Su cuenta en dolares quedo con {resultadoFinal} colones")        


    #Compra de dolares
    elif opcion=="3":
            cuentas = [
                {'cuenta': 'Colones', 'saldo': 500000, 'moneda': 'CRC'},
                {'cuenta': 'Bitcoin', 'saldo': 29103223, 'moneda': 'BTC'}
            ]
            for i, cuenta in enumerate(cuentas):
                print(f"{i+1}. {cuenta['cuenta']} ({cuenta['moneda']})")
            opcion1 = int(input("¿De cual cuenta desea comprar dolares? "))
            cuenta = cuentas[opcion1-1]
            if opcion1==1:
                print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                cantidad=int(input(f"Cuantos colones desea cambia a dolares?\n"))
                if cantidad > cuenta['saldo']:
                        print("El monto solicitado es mayor al saldo actual.")
                else:
                    cuenta['saldo'] -= cantidad
                    print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                    print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                    total=cantidad*compraDolar
                    print(f"Se compraron {total} dolares\n")


            if opcion1==2:
                print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                cantidad=int(input(f"Cuantos bitcoins desea cambia a dolares?\n"))
                if cantidad > cuenta['saldo']:
                    print("El monto solicitado es mayor al saldo actual.")
                else:
                    cuenta['saldo'] -= cantidad
                    print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                    print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                    total=cantidad*compraDolar
                    print(f"Se compraron {total} dolares\n")

    #venta de dolares
    elif opcion=="4":
            cuentas = [
                {'cuenta': 'Colones', 'saldo': 500000, 'moneda': 'CRC'},
                {'cuenta': 'Bitcoin', 'saldo': 29103223, 'moneda': 'BTC'}
            ]
            for i, cuenta in enumerate(cuentas):
                        print(f"{i+1}. {cuenta['cuenta']} ({cuenta['moneda']})")
            opcion1 = int(input("¿a que cuenta iran los fondos? "))
            cuenta = cuentas[opcion1-1]
            if opcion1==1:
                        print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                        cantidad=int(input(f"Cuantos dolares desea vender?\n"))
                        if cantidad > cuenta['saldo']:
                                print("El monto solicitado es mayor al saldo actual.")
                        else:
                            cuenta['saldo'] -= cantidad
                            print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                            print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                            total=cantidad*ventaDolar
                            print(f"Se vendieron {total} dolares\n")
            if opcion1==2:
                        print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                        cantidad=float(input(f"Cuantos dolares desea vender?\n"))
                        if cantidad > cuenta['saldo']:
                                print("El monto solicitado es mayor al saldo actual.")
                        else:
                            cuenta['saldo'] -= cantidad
                            print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                            print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                            total=cantidad*ventaDolar
                            print(f"Se vendieron {total} dolares\n")
            
            






    #compra de bitcoin
    elif opcion=="5":
            cuentas = [
            {'cuenta': 'Colones', 'saldo': 500000, 'moneda': 'CRC'},
            {'cuenta': 'Dólares', 'saldo': 10000, 'moneda': 'USD'},
            ]
            for i, cuenta in enumerate(cuentas):
                print(f"{i+1}. {cuenta['cuenta']} ({cuenta['moneda']})")
            opcion1 = int(input("¿De cual cuenta desea comprar bitcoin? "))
            cuenta = cuentas[opcion1-1]
            if opcion1==1:
                print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                cantidad=int(input(f"Cuantos colones desea cambia a bitcoin?\n"))
                if cantidad > cuenta['saldo']:
                        print("El monto solicitado es mayor al saldo actual.")
                else:
                    cuenta['saldo'] -= cantidad
                    print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                    print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                    total=cantidad*bitcoin
                    print(f"Se compraron {total} bitcoin\n")


            if opcion1==2:
                print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                cantidad=int(input(f"Cuantos dolares desea cambiar a bitcoin?\n"))
                if cantidad > cuenta['saldo']:
                    print("El monto solicitado es mayor al saldo actual.")
                else:
                    cuenta['saldo'] -= cantidad
                    print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                    print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                    total=cantidad*bitcoin
                    print(f"Se compraron {total} bitcoin\n")
            
    #venta bitcoin
    elif opcion=="6":
            cuentas = [
            {'cuenta': 'Colones', 'saldo': 500000, 'moneda': 'CRC'},
            {'cuenta': 'Dólares', 'saldo': 10000, 'moneda': 'USD'},
            ]
            for i, cuenta in enumerate(cuentas):
                        print(f"{i+1}. {cuenta['cuenta']} ({cuenta['moneda']})")
            opcion1 = int(input("¿a que cuenta iran los fondos? "))
            cuenta = cuentas[opcion1-1]
            if opcion1==1:
                        print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                        cantidad=int(input(f"Cuantos bitcoins desea vender?\n"))
                        if cantidad > cuenta['saldo']:
                                print("El monto solicitado es mayor al saldo actual.")
                        else:
                            cuenta['saldo'] -= cantidad
                            print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                            print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                            total=cantidad*bitcoin
                            print(f"Se vendieron {total} bitcoins\n")
            if opcion1==2:
                        print(f"El saldo actual de la cuenta {cuenta['cuenta']} es {cuenta['saldo']} {cuenta['moneda']}")
                        cantidad=float(input(f"Cuantos bicoins desea vender?\n"))
                        if cantidad > cuenta['saldo']:
                                print("El monto solicitado es mayor al saldo actual.")
                        else:
                            cuenta['saldo'] -= cantidad
                            print(f"Se retiraron {cantidad} {cuenta['moneda']} de la cuenta {cuenta['cuenta']}.")
                            print(f"El saldo actual de la cuenta es {cuenta['saldo']} {cuenta['moneda']}.")
                            total=cantidad*bitcoin
                            print(f"Se vendieron {total} bitcoins\n")
            
    elif opcion=="7":
            print("Saliendo...")



with open("Registrar usuarios.txt", "r") as file:

    
    datosUsuario=file.readlines()
    datosUsuario= [dato.strip() for dato in datosUsuario]
        

        
       
    file.close()
    

datosUsuario=[
    {"nombre": "kevin", "cedula": "123456787"},
    {"nombre": "laura", "cedula": "987654326"},
    {"nombre": "Sebastian", "cedula": "567890129"}
]

def eliminarUsuario(cedula):
    for registro in range(len(datosUsuario)):
            if datosUsuario[registro]["cedula"] == cedula:
                del datosUsuario[registro]
                print("Usuario eliminado")
                return True
    print("Usuario no encontrado")
    return False


def modificar_moneda():
    archivo = open("registrar usuarios.txt", "r")
    conversiones = {}
    for linea in archivo:
         linea = linea.strip()
         llave, valor = linea.split(":")
         conversiones[llave] = float(valor)
         archivo.close()

def mostrar_menu():
  print("¿Qué tipo de cambio desea modificar?")
  print("1. Compra de colones")
  print("2. Venta de colones")
  print("3. Compra de dólares")
  print("4. Venta de dólares")
  print("5. Compra de bitcoin")
  print("6. Venta de bitcoin")
  print("7. Salir")

  opcion = input("Ingrese el número de la opción deseada: ")
  return opcion

def modificar_conversion(opcion):
  if opcion == "1":
    llave = "colon_compra"
    conversion = input("Ingrese el nuevo factor de conversión para compra de colones: ")
  elif opcion == "2":
    llave = "colon_venta"
    conversion = input("Ingrese el nuevo factor de conversión para venta de colones: ")
  elif opcion == "3":
    llave = "dolar_compra"
    conversion = input("Ingrese el nuevo factor de conversión para compra de dólares: ")
  elif opcion == "4":
    llave = "dolar_venta"
    conversion = input("Ingrese el nuevo factor de conversión para venta de dólares: ")
  elif opcion == "5":
    llave = "bitcoin_compra"
    conversion = input("Ingrese el nuevo factor de conversión para compra de bitcoin: ")
  elif opcion == "6":
    llave = "bitcoin_venta"
    conversion = input("Ingrese el nuevo factor de conversión para venta de bitcoin: ")
  else:
    return False
  
    conversiones[llave] = float(conversion)
    return True

opcion = mostrar_menu()

while opcion != "7":
  if modificar_conversion(opcion):
    print("El factor de conversión ha sido actualizado exitosamente.")
  else:
    print("Opción inválida. Por favor ingrese un número del 1 al 7.")
  opcion = mostrar_menu()

archivo = open("conversiones.txt", "w")
for llave, valor in ConnectionResetError.items():
  archivo.write(llave + ":" + str(valor) + "\n")

archivo.close()

print("El archivo ha sido actualizado exitosamente.")
    
def configAvanzada():
    intentos=0
    
    while True:
        pin=getpass.getpass("Ingrese el PIN de su cuenta bancaria:\n")
        if len(pin)==4:
            print("PIN valido")
            break
        
        else:
            print("Su PIN debe de ser de 4 digitos,intente de nuevo")
    print("Ingrese nuevamente el PIN para auntenticar")
    while intentos<3:
        aunte_Pin=getpass.getpass("Ingrese el PIN para auntenticar:\n")
        if aunte_Pin==pin:
            print("Se auntentico correctamente")
            break
        else:
            print("El PIN no es igual,Intente de nuevo")
            intentos+=1
    if intentos==3:
        print("Usted ha alcanzado el maximo de intentos fallidos,intente mas tarde")
    
    while True:
        opcion=input("1-Eliminar usuario\n2-Modificar tipos de cambio\n3-salir\n")
        if opcion=="1":
            eliminarUsuario()
        elif opcion=="2":
            modificar_moneda()
            mostrar_menu()
            modificar_conversion(opcion)


    

        

#----------PROGRAMA PRINCIPAL-------------
print("Bienvenido a nuestro banco, que desea?")
menu=input("1-Registrar Usuario nuevo\n2-Usuario Registrado\n3-Configuracion Avanzada\n4-Salir\n")
while True:
    if menu=="1":
        usuarioNuevo()   
    elif menu=="2":
        opcion=(input("1-Retirar dinero\n2-Depositar dinero\n3-Ver saldo actual\n4-Pagar servicios\n5-Compra/Venta de divisas\n6-Eliminar usuario\n7-Salir\n"))
        while True:
            if opcion=="1":
                retirarDinero()
            elif opcion=="2":
                depositar()
            elif opcion=="3":
                verSaldo()
            elif opcion=="4":
                pagar_servicios()
            elif opcion=="5":
                divisas()
            elif opcion=="6":
                pinEliminar()
                cedula=input("ingrese su cedula:\n")
                eliminarUsuario(cedula)
                print(datosUsuario)
            elif opcion=="7":
                print("ha salido del sistema")
                break
            break 
    elif menu=="3":
         configAvanzada()
    elif menu=="4":
        print("Gracias por preferirnos")
        break
    else:
        print("Opcion incorrecta intente de nuevo")