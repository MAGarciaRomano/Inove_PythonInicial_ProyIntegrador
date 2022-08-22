## Inove_PythonInicial_ProyIntegrador
# Proyecto Integrador. Cliente V.I.P. (Very Important Pet)
## Autor: Martín A. García Romano
### Curso Python Inicial de Inove (2022)

#### Objetivos del Proyecto Integrador
Poner en práctica los conceptos aprendidos en el curso:
- Variables
- Condicionales
- Bucles
- Funciones
- Manejo de diccionarios
- Manejo de archivos CSV (Comma Separated Values)

#### El programa
Cliente V.I.P. es un programa pensado para la gestión de clientes caninos de una veterinaria. A través del mismo se pueden llevar adelante las siguientes tareas en sus cuatro módulos:
- Registro de nuevos clientes caninos. La primera vez que se utiliza el programa se crea un archivo CSV en el que se almacenan todos los registros. De cada cliente canino se genera un id automático incremental y se registran los siguientes datos:
  * Nombre, fecha de nacimiento (se calcula la edad al día del registro), raza, peso, sexo, Si está o no esterilizado.
  * Apellido y nombre del responsable, domicilio, teléfono.
  * Fechas de vacunación y desparasitado (externo o interno) del cliente para las enfermedades o parasitosis que puede padecer.
- Modificación de información del cliente canino. A través de un menú de opciones es posible actualizar el peso, la condición de esterilizado o no esterilizado, la fecha de la última vacunación para cada vacuna y la fecha de la última desparasitación ya sea externa o interna. La edad se actualiza automáticamente a la fecha de modificación de alguno de los datos mencionados.
- Baja de clientes caninos: Es posible dar de baja un cliente canino, pero sus datos no se pierden sino que se almacenan en un archivo CSV de bajas, que se crea con la primera baja que se registra. Esta medida es para poder recuperar la información en caso de que el cliente canino vuelva a la veterinaria. Es obvio que en caso de deceso la función del archivo de bajas es sólo de conservación de información.
- Consulta por responsable: Es posible obtener ciertos datos básicos (id, nombre, edad y sexo) de los clientes caninos que pertenecen a un responsable en particular.
En el archivo recursos.py se encuentra el generador de id, basado en una parte del código existente en uno de los archivos de clase del curso.

#### Historia
La presente versión, 1.1, difiere de la versión inicial, 1.0, en que el la modificación de datos y la baja de un cliente canino se realizan en módulos separados y no dentro del mismo módulo como se preveía inicialmente en el diagrama de flujo presentado inicialmente.
El diagrama de flujo del programa en su versión 1.1 es el siguiente.

![GarciaRomano-Integrador-ClienteVIP2](https://user-images.githubusercontent.com/105550751/185957522-76e9196f-fbc4-4334-8e75-0d7dc5a450cd.png)

Cliente V.I.P. que es un proyecto escalable, que podría considerarse como inicio de un programa con más capacidades y funcionalidades que contemple otras especies (gatos, aves, etc.) o que modificado pueda utilizarse en un refugio canino.
