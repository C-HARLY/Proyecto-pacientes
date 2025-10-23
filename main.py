import modules.pacientes
import utils.almacenamiento

pacientes = utils.almacenamiento.cargar_pacientes()

user = {
    
        "carlos": "1432005", #por default tengo estos 2 usuarios 
        "admin": "root"
}

def registrarUsario():
    
    username = input("Ingrese su nombre de usuario: ")
    
    ## quiero validar si el usuario ya existe
    if username in user:
        print("El usuario ya existe por favor intente nuevamente")
    else:
        pasword = input("Ingrese la contraseña: ")
        user[username] = pasword
        print("usuario registrado correctamente")
    
            
    

def menuPrincipal():

    opcion = 0
    while opcion!= 5:
        print("bienvenido al menu principal  ")
        print("1.   Registro de Pacientes  ")
        print("2.   Reporte de Pacientes  ")
        print("3.   editar datos del paciente  ")
        print("4.   elimiar paciente   ")
        print("5.   salir   ")
        
        opcion = int(input("Seleccione una opcion "))
        
        if opcion == 1:
            modules.pacientes.agregarPaciente()
        elif opcion == 2:
            modules.pacientes.mostrarPacientes()
        elif opcion == 3:
            modules.pacientes.editarPaciente()
        elif opcion == 4:
            modules.pacientes.eliminarPaciente()
        elif opcion == 5: 
            print("Saliendo del sistema espere.....")
        else:   
            print("opcion no valida")
            

def login():
    username = input("Ingrese su nombre de usuario:")
    pasword = input("ingrese su contraseña: ")
   
        
    if username in user and user[username] == pasword:
        print("Logeado correctamente....")
        menuPrincipal()
        
    else:
        print("error usuario o contraseña incorrecta")
        




def menuInicial():
    opcion = 0
    while opcion!=3:
        print("Bienvenido al sistema de gestion de pacientes")
        print("1.   Iniciar sesion  ")
        print("2.   Registrar usuario  ")
        
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            login()
        elif opcion == 2:
            registrarUsario()
        else:
            print("opcion no valida")
        
menuInicial()


