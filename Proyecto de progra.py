import os
import getpass

file=open("usuarios.txt","a")
file.write("segundo texto \n")
file.write("escrito en python\n")
file.close()

def usuarioNuevo():
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
    
def usuarioregistrado():
    file=open("usuarios.txt","a")
    file.write(str(usuarioNuevo()))
    file.write("\n")
    file.close()

    import os 
    file=open("usuario.txt","r")
    mensaje=file.read()
    print(mensaje)

#----------PROGRAMA PRINCIPAL-------------
print("Bienvenido a nuestro banco, que desea?")
menu=input("1-Registrar Usuario nuevo\n2-Usuario Registrado\n3-Configuracion Avanzada\n4-Salir\n")
while True:
    if menu==1:
       usuarioNuevo()
    elif menu==2:
         usuarioregistrado()
    elif menu==3:
         print("3")
    elif menu==4:
        print("Gracias por preferirnos")

    else:
        print("Opcion incorrecta intente de nuevo")
