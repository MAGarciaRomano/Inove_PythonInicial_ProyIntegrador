# Cliente V.I.P. (Very Important Pet), archivo de recursos.
# Autor: Martín A. García Romano
# Año: 2022
# Curso: Python Inicial de Inove 

import csv

# Función que calcula el Id de cada cliente que se agrega al archivo principal.
def generar_id():
    
    with open('clientevip.csv', 'r') as csvfile:
        # Lee el archivo csv y almacena los resultados en la lista lista_clientes.
        lista_clientes = list(csv.DictReader(csvfile))
                 
    # Se posiciona en la última fila del csv leído.
        ultimo_cliente = lista_clientes[-1]

    # Obtiene el Id del cliente canino registrado en la última fila.
        ultimo_id = int(ultimo_cliente.get('Id'))
    
    # Para el nuevo cliente aumenta el Id anterior en 1 y lo retorna.
        return ultimo_id + 1


if __name__ == '__main__':
    generar_id()