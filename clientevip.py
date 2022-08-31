# Cliente V.I.P. (Very Important Pet), versión 1.1
# Autor: Martín A. García Romano
# Año: 2022
# Curso: Python Inicial de Inove

import os
import csv
import recursos
from datetime import datetime
from dateutil.relativedelta import relativedelta

campos = ['Id', 'Nombre', 'FechaNacimiento', 'Edad', 'Raza', 'Peso',
            'Sexo', 'Esterilizado', 'Responsable', 'DomicilioResponsable',
            'TelResponsable', 'Moquillo', 'Hepatitis', 'Parvovirus', 'Quintuple',
            'Rabia', 'DesparasitadoInterno', 'DesparasitadoExterno']

# Opción 1: Carga de clientes caninos.
# Mediante un condicional if - else verifica si el archivo existe o no.
# La primera vez también crea el archivo.
def registrar_nuevo_cliente_canino():
    
    print('* * * REGISTRO DE UN NUEVO CLIENTE CANINO Y RESPONSABLE A CARGO * * *')
    if os.path.isfile('clientevip.csv'):
        # Si el archivo existe.
        with open('clientevip.csv') as csvcanino:
        
            id_cliente = recursos.generar_id()
    
    else:
        # Si el archivo no existe. 
        with open('clientevip.csv', 'w', newline = '') as csvcanino:
            writer = csv.DictWriter(csvcanino, fieldnames = campos)
            writer.writeheader()
            
            id_cliente = 1 
    
    # Apertura del archivo csv y agregado del nuevo cliente.
    with open('clientevip.csv', 'a', newline = '') as csvcanino:
        
    # Solicitud de datos del canino y del responsable.
        print('''A continuación se solicitan datos del nuevo cliente canino y de su responsable.
        Primero los datos del canino''')

        nombre_canino = str(input('Nombre del nuevo cliente canino: ')).capitalize()
    
    # Ingreso y validación de la fecha de nacimiento del canino.
        while True:
            try:
                fecha_nacimiento_canino = str(input("Fecha de nacimiento (dd/mm/aaaa): "))
                datetime.strptime(fecha_nacimiento_canino, '%d/%m/%Y')
                break
            except:
                print("¡ATENCIÓN! Fecha o formato de fecha incorrecto.")
                continue
    
    # Cálculo de la edad del canino en años, meses y días.
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_canino, '%d/%m/%Y')
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        edad_canino = f"{edad.years} a, {edad.months} m, {edad.days} d"

    # Ingreso y validación de la raza del canino.
        while True:
            raza_canino = str(input('Raza del nuevo cliente: ')).capitalize()
            if any(caracter.isdigit() for caracter in raza_canino) is True:
                print('¡ATENCIÓN! Debe ingresar una raza o mestizo. Vuelva a intentar.')
                continue
            else:
                break

    # Ingreso y validación del peso del canino.
        while True:
            try:
                peso_canino = float(input('Peso del nuevo cliente canino: '))
                if type(peso_canino) == float:
                    break
            except:
                print("¡ATENCIÓN! Ingrese un número con parte entera, punto y parte decimal (Ejemplos: 13.5 ; 9.0).")
                continue    
        
    # Ingreso y validación del sexo del canino.    
        while True:
            try:
                sexo_canino = str(input('¿Macho (M) o Hembra (H)?: ')).capitalize()
                if sexo_canino == 'M' or sexo_canino == 'H':
                    break
            except:
                print("¡ATENCIÓN! Debe ingresar M si es Macho o H si es Hembra.")
                continue

    # Registro y validación de la condición de esterilizado del canino.
        while True:
            try:
                esterilizado = str(input('¿El cliente está esterilizado? S o N: ')).capitalize()
                if esterilizado == 'S' or esterilizado == 'N':
                    break
            except:
                print("¡ATENCIÓN! Debe ingresar S si está esterilizado o N si no lo está.")
                continue

    # Solicitud de los datos del responsable del canino.    
        print('Ahora los datos del responsable...')

        apellidos_responsable = str(input('Apellido/s: ')).title()
        nombres_responsable = str(input('Nombre/s: ')).title()
        responsable = str(apellidos_responsable + ' ' + nombres_responsable)
        calle_y_numero = str(input('Calle y número: ')).title()
        ciudad = str (input('Ciudad: ')).title()
        provincia = str(input('Provincia: ')).title()
        domicilio_responsable = str(calle_y_numero + ', ' + ciudad + ', ' + provincia)
        telefono_responsable = str(input('Teléfono (código de área + número): '))

    # Construcción de la ficha de datos del nuevo cliente canino.
        nuevo_cliente = {"Id": id_cliente,
            "Nombre": nombre_canino,
            "FechaNacimiento": fecha_nacimiento_canino,
            "Edad": edad_canino,
            "Raza": raza_canino,
            "Peso": peso_canino,
            "Sexo": sexo_canino,
            "Esterilizado": esterilizado,
            "Responsable": responsable,
            "DomicilioResponsable": domicilio_responsable,
            "TelResponsable": telefono_responsable,
            "Moquillo": None,
            "Hepatitis": None,
            "Parvovirus": None,
            "Quintuple": None,
            "Rabia": None,
            "DesparasitadoInterno": None,
            "DesparasitadoExterno": None}

    # Construcción del objeto writer que escribirá en el archivo csv.
        writer = csv.DictWriter(csvcanino, campos)

    # Agregar nuevo cliente canino al archivo csv.
        writer.writerow(nuevo_cliente)


# Opción 2: Modifica información de un cliente canino.
# Se actualizan el peso, la condición de esterilización, las vacunas y desparasitaciones.
# La edad del canino se actualiza automáticamente.
def modificar_cliente_canino():

    print('* * * MODIFICACIÓN DE DATOS MÉDICOS DE UN CLIENTE CANINO * * *')
    # Solicitud del nombre del canino y apellido/s y nombre/s del responsanble.
    nombre_canino = str(input('Nombre del cliente canino: ')).capitalize()
    responsable_canino = str(input('Apellido/s y Nombre/s del responsable: ')).title()

    # Apertura del archivo en modo lectura y almacenamiento en una lista de diccionarios.
    with open('clientevip.csv', 'r') as consultacsv:
        consulta_clientes = list(csv.DictReader(consultacsv))

    # Se crea una variable para indicar si el cliente se encuentra en el archivo o no.
    cliente_encontrado = False

    # Recorrer la lista de diccionarios buscando el canino y el responsable ingresados.
    for cliente in consulta_clientes:

    # Encontrado el canino y el responsable:
    # Se crea una variable conteniendo en un diccionario la información del canino.
        if cliente.get('Nombre') == nombre_canino and cliente.get('Responsable') == responsable_canino:
            a_modificar = cliente
            cliente_encontrado = True
                
    # Mostrar mensaje de error y regreso al menú si el canino y el responsable no se encuentran.
    if not cliente_encontrado:
        print(f'El cliente {nombre_canino} con responsable {responsable_canino} no existen.')
        return

    # Menú de opciones de modificación. 
    menu_modificacion= '''\n
        ¿Qué información va a modificar? Escriba la letra correspondiente:
        W - Actualizar peso (W) del cliente canino.
        C - Actualizar si ha sido Esterilizado (C).
        M - Actualizar vacuna contra Moquillo.
        H - Actualizar vacuna contra Hepatitis.
        P - Actualizar vacuna contra Parvovirus.
        Q - Actualizar vacuna Quíntuple.
        R - Actualizar vacuna contra Rabia.
        I - Actualizar Desparasitado Interno.
        E - Actualizar Desparasitado Externo.
        Para cancelar la modificación presione cualquier otra tecla.
        Opcion elegida:'''

    while True:
            opcion_menu = str(input(menu_modificacion)).capitalize()
        
            # Informar al usuario la opción de modificación seleccionada.
            print(f'Usted ha elegido modificar la opción: {opcion_menu}')  
        
            # Rutina de trabajo según el condicional.
            if opcion_menu == 'W':
                peso = float(input("Nuevo peso: "))
                a_modificar.update({'Peso': peso})
            
            elif opcion_menu == 'C':
                a_modificar.update({'Esterilizado': 'S'})

            elif opcion_menu == 'M':
                fecha_moquillo = datetime.today().strftime('%d/%m/%Y')
                a_modificar.update({'Moquillo': fecha_moquillo})
            
            elif opcion_menu == 'H':
                fecha_hepatitis = datetime.today().strftime('%d/%m/%Y')
                a_modificar.update({'Hepatitis': fecha_hepatitis})

            elif opcion_menu == 'P':
                fecha_parvovirus = datetime.today().strftime('%d/%m/%Y')
                a_modificar.update({'Parvovirus': fecha_parvovirus})

            elif opcion_menu == 'Q':
                fecha_quintuple = datetime.today().strftime('%d/%m/%Y')
                a_modificar.update({'Quintuple': fecha_quintuple})

            elif opcion_menu == 'R':
                fecha_rabia = datetime.today().strftime('%d/%m/%Y')
                a_modificar.update({'Rabia': fecha_rabia})

            elif opcion_menu == 'I':
                fecha_desp_interno = datetime.today().strftime('%d/%m/%Y')
                a_modificar.update({'DesparasitadoInterno': fecha_desp_interno})

            elif opcion_menu == 'E':
                fecha_desp_externo = datetime.today().strftime('%d/%m/%Y')
                a_modificar.update({'DesparasitadoExterno': fecha_desp_externo})

            else:
            # Finalizar ejecución del menú de opciones de modificación.
            # En caso de opción incorrecta muestra datos con edad actualizada.
                print('''
                    -----------------------------------------
                    La opción elegida no corresponde al menú.
                    Se muestra cliente con modificaciones.
                    -----------------------------------------''')
                break

    # Actualización automática de la edad del canino.
    fecha_nacimiento = a_modificar['FechaNacimiento']
    nacimiento =datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    edad = relativedelta(datetime.now(), nacimiento)
    edad_canino = f"{edad.years} a, {edad.months} m, {edad.days} d"
    a_modificar.update({'Edad': edad_canino})

    # Presentación de los datos del canino con las modificaciones.
    print("Responsable:", a_modificar['Responsable'], "Contacto:", a_modificar['TelResponsable'])
    print("Id:", a_modificar['Id'], "Nombre:", a_modificar['Nombre'])    
    print("Edad:", a_modificar['Edad'], "Sexo:", a_modificar['Sexo'])
    print("Peso", a_modificar["Peso"], "Esterilizado:", a_modificar['Esterilizado'])
    print("- = - = - Vacunas - = - = -")
    print("Moquillo:", a_modificar['Moquillo'])
    print("Hepatitis:", a_modificar['Hepatitis'])
    print("Parvovirus:", a_modificar['Parvovirus'])
    print("Quíntuple:", a_modificar['Quintuple'])
    print("Rabia:", a_modificar['Rabia'])
    print("- = - = - Desparasitado - = - = -")
    print("Desparasitado Interno:", a_modificar['DesparasitadoInterno'])
    print("Desparasitado Externo:", a_modificar['DesparasitadoExterno'])
    print("- = - = - = - = - = - = - = - = -")

    # Almacenar los cambios en clientevip.csv abriendo archivo en modo escritura.
    csvnuevo = open('clientevip.csv', 'w', newline='')

    # Construcción del objeto writer para modificar el archivo.
    writer = csv.DictWriter(csvnuevo, fieldnames=campos)

    # Escribir los nombres de los campos y de los registros.
    writer.writeheader()
    writer.writerows(consulta_clientes)

    # Cerrar el archivo
    csvnuevo.close()


# Opción 3: Consulta de caninos a cargo de un responsable.
# Se actualizan el peso, la condición de esterilización, las vacunas y desparasitaciones.
# La edad del canino se actualiza automáticamente.
def consulta_por_responsable():
    
    print('* * * CONSULTA DE CANINOS A CARGO DE UN RESPONSABLE * * *')
    # Abrir el archivo en modo lectura y creación de una lista de diccionarios.
    with open('clientevip.csv', 'r') as csvconsulta:
        consulta_data = list(csv.DictReader(csvconsulta))

    # Se solicitan apellido/s y nombre/s del responsable.
        busca_responsable = str(input("Apellído/s y Nombre/s del responsable a consultar: ")).title()
        print("------------------------------------------")
        
        total_clientes = len(consulta_data)
        clientes_del_responsable = 0
        print("Id", "Nombre", "Edad (a, m, d)", "Sexo", sep='  |  ')
        print("------------------------------------------")

    # Bucle que busca los caninos a cargo de un responsable en la lista de diccionarios.
    # Se capturan errores.
    # Se muestran resultados.    
        for cliente_canino in range(total_clientes):
            cliente = consulta_data[cliente_canino]
            try:
                responsable = str(cliente.get("Responsable"))
                
                if responsable == busca_responsable:
                    clientes_del_responsable += 1
                    print(cliente.get("Id"), cliente.get("Nombre"), cliente.get ("Edad"),
                        cliente.get("Sexo"), sep="     ")
                    print("------------------------------------------")
        
            except:
                continue
    
    # Se imprime mensaje informando el número de caninos a cargo del responsable.
        print (busca_responsable, 'es responsable de', clientes_del_responsable, "caninos.")


# Opción 4: Baja de cliente canino.
# Incorporación de la baja a un archivo de bajas.
# En la primera baja se crea el archivo de bajas.
def eliminar_cliente_canino():
    
    print('* * * BAJA DE CLIENTE CANINO * * *')
    # Solicitud del nombre del canino y apellido/s y nombre/s del responsanble.
    nombre_canino = str(input('Nombre del cliente canino a dar de baja: ')).capitalize()
    responsable_canino = str(input('Apellido/s y Nombre/s del responsable: ')).title()

    # Abrir el archivo en modo lectura y creación de una lista de diccionarios.
    with open('clientevip.csv', 'r') as consultacsv:
        lista_consulta = list(csv.DictReader(consultacsv))

    # Se crea una variable para indicar si el cliente se encuentra en el archivo o no.
    cliente_encontrado = False

    # Recorrer la lista de diccionarios buscando el canino y el responsable ingresados.
    for cliente in lista_consulta:

    # Encontrado el canino y el responsable:
    # Se crea una variable conteniendo en un diccionario la información del canino.
    # Se elimina al canino de la lista de diccionarios.
        if cliente.get('Nombre') == nombre_canino and cliente.get('Responsable') == responsable_canino:
            cliente_baja = cliente
            lista_consulta.pop(lista_consulta.index(cliente_baja))
            cliente_encontrado = True
            break
    
    # Mostrar mensaje de error y regreso al menú si el canino y el responsable no se encuentran.
    if not cliente_encontrado:
        print(f'El cliente {nombre_canino} con responsable {responsable_canino} no existen.')
        return
    
    # Abrir el archivo en modo escritura para actualizarlo sin el cliente eliminado.
    with open('clientevip.csv', 'w') as nuevocsv:
    
    # Construcción del objeto writer que escribirá en el archivo csv.
        writer = csv.DictWriter(nuevocsv, fieldnames = campos)

    # Escribir los campos y registros en el archivo csv.
        writer.writeheader()
        writer.writerows(lista_consulta)
    
    # Actualización y/o creación del archivo de bajas donde se almacenan
    # los registros eliminados del archivo de clientes.
    # Primero se comprueba la existencia del archivo. Si existe, se agrega la baja.
    # Si el archivo no existe se crea y se escribe un primer registro.
    if os.path.isfile('bajasvip.csv'):
        with open('bajasvip.csv', 'a', newline='') as csvbajas:
            
        # Construcción del objeto writer que escribirá en el archivo csv.
            writer = csv.DictWriter(csvbajas, campos)
        # Agregar la baja al archivo de bajas.
            writer.writerow(cliente_baja)
    else:
        with open('bajasvip.csv', 'w', newline = '') as csvbajas:
        # Construcción del objeto writer que escribirá el archivo csv.
            writer = csv.DictWriter(csvbajas, fieldnames = campos)
        # Escribir los campos y registros en el archivo csv.    
            writer.writeheader()
            writer.writerow(cliente_baja)


if __name__ == '__main__':

    # Mensaje de bienvenida.
    print('Bienvenido a Cliente V.I.P. (Very Important Pet) gestor de clientes caninos.')
    print('Autor: Martín A. García Romano (2022).')
    
    # Presentar opciones del programa.
    menu = '''\n
    ¿Qué desea hacer? Indique el número de la opción elegida:
    1 - Registrar un nuevo cliente canino.
    2 - Modificar datos de un cliente canino o dar de baja un cliente canino.
    3 - Realizar una consultar por apellido/s y nombre/s del responsable.
    4 - Dar de baja un cliente canino.
    Para salir del programa pulse cualquier otro número.
    Opcion elegida:'''

    while True:
        
        try: 
            opcion = int(input(menu))
            # Informar al usuario la opción de trabajo seleccionada.
            print(f'Usted ha elegido la opción: {opcion}')  
        
            # Rutina de trabajo según condicional:
            if opcion == 1:
            # Registro de un nuevo cliente canino.
                registrar_nuevo_cliente_canino()

            elif opcion == 2:
            # Modificar datos de un cliente canino.
                modificar_cliente_canino()
            
            elif opcion == 3:
            # Consulta de caninos a cargo de un responsable.
                consulta_por_responsable()

            elif opcion == 4:
            # Solicitar un outfit
                eliminar_cliente_canino()
            
            else:
            # Aviso de finalización de ejecución.
                print('Ud. ha elegido salir. Fin del programa.')
                break
                
        except:
            print('¡OPCIÓN INVÁLIDA! Vuelva a intentar.')
            continue