# GUI-Validador-De-Direcciones-Gobierno-de-La-Nacion

NOTA: Puede ver una demostracion del programa, dentro de la carpeta: Videos_Tutoriales
----------------------------------------------------------------------------------------------------------------

Version Grafica del Buscador y Validador de direcciones Gobierno Nacional programado en python

Autor: Gustavo Wydler Azuaga - 06/04/2020

----------------------------------------------------------------------------------------------------------------

Modo de setup y Uso:

-Descargar el repositorio Desde github, por linea de comando (Linux): wget 

-Instalar pip3 para python: sudo apt-get install python3-pip (si no esta instalado) 

-Ingresar al directorio, abrir el archivo con un editor de codigo: validador_de_direcciones_nacion.py

-Importar todas las librerias en python (sudo pip3-install <Nombre_de_libreria>) -Una vez que estan todas las librerias, correr el programa: python3.6 validador_de_direcciones_nacion.py

----------------------------------------------------------------------------------------------------------------

Descripcion y funcionalidades:

Este programa de linea de comando (CLI), es un validador/nomenclador de direcciones de Provincia de Buenos Aires y C.A.B.A. Permite buscar y validar direcciones en base a 3 campos que son obligatorios:

-Nombre de calle y Numero separados
-Localidad o barrio
-Partido

Al proveerle los datos al programa, este consume la API del gobierno nacional:

"https://apis.datos.gob.ar/georef/api/direcciones?provincia="

Con esta direccion de base, arma una URL en base a los parametros pasados en el formulario.

Si la API encuentra una direccion con los campos suministrados, devolvera los datos Validados en formato .json con campos extra, los mostrara en la consola y los parseara a formato texto para mostrarlos de manera mas legible para el usuario.

En caso de no obtener datos con los valores suministrados, arroja una advertencia y limpia el formulario.

----------------------------------------------------------------------------------------------------------------

Funcionalidades:

-Los Datos pueden verse tanto en la interfaz grafica como en la consola.

-La direccion validada puede ser visualizada en Google Maps. Los parametros son pasados al navegador a travez de Selenium.

-La operacion anterior puede realizarse tambien a travez de las coordenadas (Longitud y Latitud) devueltas como dato extra por la API.

