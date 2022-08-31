# Cliente V.I.P. (Very Important Pet), archivo de recursos.
# Autor: Martín A. García Romano
# Año: 2022
# Curso: Python Inicial de Inove 

import csv

# Función que calcula el Id de cada cliente que se agrega al archivo principal.
def generar_id():
    
    with open('clientevip.csv', 'r') as csvfile:
        # Lee el archivo csv.
        # Almacena todos los registros en la lista lista_clientes.
        lista_clientes = list(csv.DictReader(csvfile))
        # Cuenta los registros del archivo.
        registros = len(lista_clientes)
                 
        # Determina si la lista de registros está vacía.
        # Si está vacía, asigna el id 1 y lo retorna.
        if registros < 1:
            ultimo_id = 1
            return ultimo_id
    
        # Si no está vacía.
        else:
        # Se posiciona en la última fila del csv leído.
            ultimo_cliente = lista_clientes[-1]
        # Obtiene el Id del cliente canino registrado en la última fila.
            ultimo_id = int(ultimo_cliente.get('Id'))
        # Para el nuevo cliente incrementa el último Id en 1 y lo retorna.
            return ultimo_id + 1


if __name__ == '__main__':
    generar_id()