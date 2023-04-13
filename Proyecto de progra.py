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
    file.write("Cedula: {} , Nombre: {} ".format(cedula,nombre,))
    file.close()

    
def usuarioRegistrado():
    with open("Registrar usuarios.txt", "r") as file:

    
        datosUsuario=file.readlines()
        datosUsuario= [dato.strip() for dato in datosUsuario]
        datos = []
        for dato in datosUsuario:
            datos.append(dato)
        
    file.close()
    print(datos)
    
    

def configAvanzada():
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
    opcion=input("1-Eliminar usuario\n2-Modificar tipos de cambio\n3-salir\n")
    
        

#----------PROGRAMA PRINCIPAL-------------
print("Bienvenido a nuestro banco, que desea?")
menu=input("1-Registrar Usuario nuevo\n2-Usuario Registrado\n3-Configuracion Avanzada\n4-Salir\n")
while True:
    if menu=="1":
       usuarioNuevo()   
    elif menu=="2":
         usuarioRegistrado()
    elif menu=="3":
         print("Hola")
    elif menu=="4":
        print("Gracias por preferirnos")
        break
    else:
        print("Opcion incorrecta intente de nuevo")


    