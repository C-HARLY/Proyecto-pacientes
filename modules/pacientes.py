#import utils.almacenamiento
import modules.database



database = modules.database.crear_tabla()

## AGREGAR PACIENTES NUEVO A LA BASE DE DATOS 
def agregarPaciente():
    while True:
        DPI = input("Ingrese el DPI (13 dígitos): ")
        if DPI.isdigit() and len(DPI) == 13:
            break
        else:
            print("Error: el DPI debe tener 13 dígitos.")

    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    genero = input("Ingrese el género: ")
    telefono = input("Ingrese el teléfono: ")
    motivoConsulta = input("Ingrese el motivo de consulta: ")

    database.agregar_paciente(DPI, nombre, apellido, edad, genero, telefono, motivoConsulta)
    print("✅ Paciente agregado correctamente y guardado en la base de datos.")

def mostrarPacientes():
    pacientes = database.obtener_pacientes()
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    for p in pacientes:
        print(f"""
ID: {p[0]}
DPI: {p[1]}
Nombre: {p[2]} {p[3]}
Edad: {p[4]}
Género: {p[5]}
Teléfono: {p[6]}
Motivo: {p[7]}
        """)
        
        
        
        #AGREGAR PACIENTES ANTIGUO A UN DICCIONARIO 
""" agregar pacientes 
def agregarPaciente():
    
    global ID
    
    ID += 1
    # Validamos el DPI que no sea negativo y tenga 13 dígitos
    while True: 
        DPI = input("Ingrese el DPI del paciente (13 dígitos): ")
        
        if DPI.isdigit() and len(DPI) == 13: 
            break
        else:
            print("Error: El DPI debe tener 13 dígitos y contener solo números.")
            
    nombre = input("Ingrese el nombre del paciente:")
    apellido = input("Ingrese el apellido del paciente:")
    
    while True:
        edad = input("Ingrese la edad del paciente:")
        if edad.isdigit() and int(edad) > 0:
            break
        else:
            print("Error la edad es invalida intene nuevamente ")

    genero = input("Ingrese el genero del paciente:")
    telefono = input("Ingrese el numero de telefono del paciente:")
    motivoConsulta = input("Ingrese el motivo de consulta del paciente:")
    
    ##diccionario de paciente con sus atributos
    paciente = {
    ID: ID,
    "DPI" : DPI,
    "nombre" :  nombre,
    "apellido" :  apellido,
    "edad" :  edad,
    "genero" :  genero,
    "telefono" :  telefono,
    "motivoConsulta" :  motivoConsulta
    }   

    print("Paciente agregado correctamente")
    utils.almacenamiento.guardar_pacientes(pacientes)
    
    pacientes.append(paciente)
    print("Paciente agregado y guardado ")


## mostrar los pacientes de la lista 
def mostrarPacientes():
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    for i, paciente in enumerate(pacientes, start=1):
        print(f"paciente {i}:")
        print(f"DPI : {paciente['DPI']}")
        print(f"Nombre : {paciente['nombre']} {paciente['apellido']}")
        print(f"edad : {paciente['edad']}")
        print(f"genero : {paciente['genero']}")
        print(f"telefono : {paciente['telefono']}")
        print(f"motivo de la consulta  : {paciente['motivoConsulta']}")
        
## editar pacientes
def editarPaciente():
    if not pacientes:
        print("De momento no hay registros de pacientes")
        return
    
    try:
        idBuscar = int(input("Ingrese el ID del paciente que desea editar: "))
    except ValueError:
        print("Error: Debe ingresar un número válido para el ID.")
        return
    
    for paciente in pacientes:  # buscamos el paciente por ID
        if paciente['ID'] == idBuscar:
            print("Paciente encontrado:")
            print(paciente)
            
            # Editar DPI
            DPI = input(f"Ingrese el nuevo DPI ({paciente['DPI']}): ")
            if DPI:
                if DPI.isdigit() and len(DPI) == 13:
                    paciente['DPI'] = DPI
                else:
                    print("Error: DPI inválido, no se actualizó.")

            # Editar nombre
            nombre = input(f"Nuevo nombre ({paciente['nombre']}): ")
            if nombre:
                paciente['nombre'] = nombre
            
            # Editar apellido
            apellido = input(f"Nuevo apellido ({paciente['apellido']}): ")
            if apellido:
                paciente['apellido'] = apellido

            # Editar edad
            edad = input(f"Nueva edad ({paciente['edad']}): ")
            if edad:
                if edad.isdigit() and int(edad) > 0:
                    paciente['edad'] = int(edad)
                else:
                    print("Error: Edad inválida, no se actualizó.")

            # Editar género
            genero = input(f"Nuevo género ({paciente['genero']}): ")
            if genero:
                paciente['genero'] = genero

            # Editar teléfono
            telefono = input(f"Ingrese el nuevo teléfono ({paciente['telefono']}): ")
            if telefono:
                if telefono.isdigit():
                    paciente['telefono'] = int(telefono)
                else:
                    print("Error: Teléfono inválido, no se actualizó.")

            # Editar motivo de consulta
            motivoConsulta = input(f"Ingrese el nuevo motivo de consulta ({paciente['motivoConsulta']}): ")
            if motivoConsulta:
                paciente['motivoConsulta'] = motivoConsulta

            print("Paciente actualizado correctamente.")
            return  

    
    print("No se encontró ningún paciente con ese ID.")
    
    
def eliminarPaciente():
    if not pacientes:
        print("No hay pacientes registrados.:")
        return
    
    try:
        idBuscar = int(input("Ingrese el ID del paciente que desea eliminar:"))
    except ValueError:
        print("Ingrese un ID valido")
        return
    
    for paciente in pacientes:
        if paciente['ID'] == idBuscar:
            print("Paciente encontrado:")
            print(paciente)
            
            confirmar = input("Desea eliminar este paciente? si/no:")
            if confirmar == 'si':
                pacientes.remove(paciente)
                print("paciente eliminado correctamente")
            else:
                print("operacion cancelada")
            return
    print("No se encuentra ningun paciente con ese ID")
    
    
    """