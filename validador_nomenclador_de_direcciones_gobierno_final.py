import sys
import easygui
from easygui import *
from urllib.parse import quote
from urllib.request import urlopen
import json
import csv
import os
import time
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
import datetime
from datetime import datetime
#from colorama import init
#from colorama import Fore, Back, Style
#init()

loop = 0
while (loop==0):

    def Salir_programa():
        
            salir = "redcross.png"
            msg = "Confirma que desea salir del programa?"
            title = "Finalizar programa"
            botones_salir = ["Si", "No"]
            menu_salir = buttonbox(msg, title, botones_salir, image=salir)
            if menu_salir == "Si":
                sys.exit(0)
            else:
                mano_ok = "good.png"
                msg = "Se limpio el formulario, presione Ok para volver a completarlo"
                title = "Formulario limpio"
                msgbox(msg, title, image=mano_ok)
                formulario_datos()
            
    def formulario_datos():
        global url
        url = "https://apis.datos.gob.ar/georef/api/direcciones?provincia="
        global notes
        global warning
        warning = "warning.png"
        notes= "notes.png"
        global msg
        comuna1 = "Comuna 1 : Retiro, San Nicolás, Puerto Madero, San Telmo, Monserrat y Constitución"
        comuna2 = "Comuna 2 : Recoleta"
        comuna3 = "Comuna 3 : San Cristóbal y Balvanera"
        comuna4 = "Comuna 4 : Boca, Barracas, Parque Patricios y Nueva Pompeya"
        comuna5 = "Comuna 5 : Almagro, Boedo"
        comuna6 = "Comuna 6 : Caballito"
        comuna7 = "Comuna 7 : Flores, Parque Chacabuco"
        comuna8 = "Comuna 8 : Villa Soldati, Villa Riachuelo, Villa Lugano"
        comuna9 = "Comuna 9 : Parque Avellaneda, Liniers, Mataderos"
        comuna10 = "Comuna 10: Villa Real, Monte Castro, Versalles, Floresta, Vélez Sársfield, Villa Luro"
        comuna11 = "Comuna 11: Villa Gral. Mitre, Villa Devoto, Villa del Parque, Villa Santa Rita"
        comuna12 = "Comuna 12: Coghlan, Saavedra, Villa Urquiza y Villa Pueyrredón"
        comuna13 = "Comuna 13: Belgrano, Núñez y Colegiales"
        comuna14 = "Comuna 14: Palermo"
        comuna15 = "Comuna 15: Chacarita, Villa Crespo, Paternal, Villa Ortúzar, Agronomía, Parque Chas"
        msg = "Validador y nomenclador de direccones de la Provincia y Ciudad de Buenos Aires - API Gobierno de la Nacion\n\nListado de Comunas para referencia:\n\n"+comuna1+'\n'+comuna2+'\n'+comuna3+'\n'+comuna4+'\n'+comuna5+'\n'+comuna6+'\n'+comuna7+'\n'+comuna8+'\n'+comuna9+'\n'+comuna10+'\n'+comuna11+'\n'+comuna12+'\n'+comuna13+'\n'+comuna14+'\n'+comuna15+'\n\n'"* Todos los campos son Obligatorios\n\n* Especifique localidad o Barrio de Provincia o C.A.B.A\n\n* NOTA: Si cancela, se limpiara el formulario\n"
        global title_formulario
        title_formulario = "Nomenclador de Direcciones"
        global fieldNames
        fieldNames = ["Nombre de Calle y numero separados","Localidad o Barrio", "Partido"]
        global fieldValues
        fieldValues = []
        fieldValues = multenterbox(msg, title_formulario, fieldNames)

        while 1:
            errmsg = ""
            if fieldValues == None:
                Salir_programa()
            for i in range(len(fieldNames)):
              if fieldValues[i].strip() == "":
                title = "ATENCION"
                errmsg = errmsg + ('* Atencion, completar "%s". No esta completo y es un campo Obligatorio.\n\n' % fieldNames[i])
            if errmsg == "": break # no problems found
            msgbox(errmsg, title, image=warning)
            fieldValues = multenterbox(msg, title, fieldNames, fieldValues)
                   
        def confirmacion_datos():

            title = "Datos proporcionados"
            lines = "---------------------------------------------"
            msg = "LOS DATOS PORPORCIONADOS SON LOS SIGUIENTES:\n\nNombre de calle y numero: "+fieldValues[0]+'\n'+lines+'\n\n'"Localidad o Barrio: "+fieldValues[1]+'\n'+lines+'\n\n'"Partido: "+fieldValues[2]
            botones_menudatos = ["Confirmar datos -->", "<-- Limpiar formulario", "Salir"]
            menudatos = buttonbox(msg, title,  botones_menudatos, image=notes)
            if menudatos == "Confirmar datos -->":
                def datos_confirmados():
                    
                    msg = "Los datos fueron confirmados"
                    title = "Confirmacion de datos"
                    direccion_actual = "&direccion=" + str(fieldValues[0]) 
                    localidad_actual = "&localidad=" +  str(fieldValues[1])
                    provincia = "Buenos Aires"
                    url_completa = (url + provincia + localidad_actual + direccion_actual).replace(' ', '%20')
                    #print(url_completa)
                    portal = urlopen(url_completa)
                    print("URL armada en base a busqueda: "+url_completa)
                    print(lines)
                    html = portal.read().decode("utf8")
                    #print("------------------------------------------")
                    print("Esperando respuesta de la API en formato json...")
                    print(" ")
                    jason = json.loads(html)
                    print(jason)

                    try:
                        
                        #direcciones = str(jason.get("direcciones")[0]['calle'])
                        nombre_calle = str(jason.get("direcciones")[0]['calle']['nombre'])
                        numero = str(jason.get("direcciones")[0]['altura']['valor'])
                        #nombre_calle_cruce1 = str(jason.get("direcciones")[0]['calle_cruce_1']['nombre'])
                        #nombre_calle_cruce2 = str(jason.get("direcciones")[0]['calle_cruce_2']['nombre'])
                        nombre_localidad = str(jason.get("parametros")['localidad'])
                        nombre_partido = str(jason.get("direcciones")[0]['departamento']['nombre'])
                        nombre_provincia = str(jason.get("direcciones")[0]['provincia']['nombre'])
                        longitud = str(jason.get("direcciones")[0]['ubicacion']['lat'])#.replace('.', ',')
                        latitud = str(jason.get("direcciones")[0]['ubicacion']['lon'])#.replace('.', ',')
                        print(lines)
                        print("Imprimiendo valores de campos en formato texto: ")
                        print(" ")
                        print("Calle/Av: "+nombre_calle+" Altura/Numeracion: "+numero)
                        print(lines)
                        print("Localidad: "+nombre_localidad)
                        print(lines)
                        print("Partido: "+nombre_partido)
                        print(lines)
                        print("Provincia"+nombre_provincia)
                        print(lines)
                        print("Longitud: "+longitud)
                        print(lines)
                        print("Latitud: "+latitud)
                        lineas = "-------------------------------------------------------------"
                        asteriscos = "*************************************************************"
                        title = "Resultado de la API del Gobierno"
                        mensaje = "Los siguientes datos fueron proveidos por la API del Gobierno de la Nacion: "+'\n\n'+"https://apis.datos.gob.ar/georef/api/direcciones?provincia="+'\n\n'+asteriscos+'\n\n'"Calle y altura encontrados: "+ nombre_calle + " " +numero+'\n'+lineas+'\n'"Localidad encontrada: "+nombre_localidad+'\n'+lineas+'\n'"Partido encontrado: "+nombre_partido+'\n'+lineas+'\n'"Provincia encontrada: "+nombre_provincia+'\n'+lineas+'\n'"Datos adicionales encontrados: "+'\n\n'" * Longitud: "+longitud+'\n'" * Latitud: "+latitud+'\n'+lineas+'\n'
                        botones = ["Ver direccion en Google Maps", "Buscar con coordenadas en Google Maps", "Volver a Formulario", "Salir"] 
                        opciones = buttonbox(mensaje ,title, botones, image=notes)
                        if opciones == "Ver direccion en Google Maps":
                            print("Abriendo navegador para buscar direcciones: ")
                            print(" ")
                            print("Calle: "+nombre_calle+" "+"Altura: "+numero)
                            print(lineas)
                            print("Localidad: "+nombre_localidad)
                            print(lineas)
                            print("Partido: "+nombre_partido)
                            print(lineas)
                            print("Provincia: "+nombre_provincia)
                            print(lineas)
                            print("\n")
                            print("Espere por favor...")
                            coma = ","
                            espacio = " "
                            global driver
                            driver = webdriver.Firefox()
                            #driver = webdriver.Chrome()
                            driver.get("https://maps.google.com")
                            driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(nombre_calle+coma+espacio+numero+coma+espacio+nombre_localidad+coma+espacio+nombre_partido+coma+espacio+nombre_provincia)
                            driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
                            print("\n")
                            print(lineas)
                            print("Busqueda finalizada.")
                            

                        elif opciones == "Buscar con coordenadas en Google Maps":
                            print("Abriendo navegador para buscar segun coordenadas: ")
                            print(" ")
                            print("Longitud: "+longitud)
                            print(lineas)
                            print("Latitud: "+latitud)
                            print(lineas)
                            print("\n")
                            print("Espere por favor...")
                            coma = ","
                            espacio = " "
                            driver = webdriver.Firefox()
                            driver.get("https://maps.google.com")
                            driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(longitud+coma+espacio+latitud)
                            driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
                            print("\n")
                            print(lineas)
                            print("Busqueda finalizada.")
                            
                        elif opciones == "Volver a Formulario":
                            formulario_datos()
                            
                        elif opciones == "Salir":
                            salir = "redcross.png"
                            msg = "Confirma que desea salir del programa?"
                            title = "Finalizar programa"
                            botones_salir = ["Si", "No"]
                            menu_salir = buttonbox(msg, title, botones_salir, image=salir)
                            if menu_salir == "Si":
                                sys.exit(0)
                            if menu_salir == "No":
                                datos_confirmados()

                        
                    except IndexError:
                            advertencia = "warning2.png"
                            no_encontrado = "Datos no encontrados"
                            calle_localidad_no_encontrada = "Lamentablemente, la API no encontro datos con los valores proporcionados"+'\n\n'+"Presione Ok para Volver al buscador."
                            msgbox(calle_localidad_no_encontrada, no_encontrado, image=advertencia)
                            formulario_datos()

                datos_confirmados()

            elif menudatos == "<-- Limpiar formulario":
                formulario_datos()
                
            elif menudatos == "Salir":
                salir = "redcross.png"
                msg = "Confirma que desea salir del programa?"
                title = "Finalizar programa"
                botones_salir = ["Si", "No"]
                menu_salir = buttonbox(msg, title, botones_salir, image=salir)
                if menu_salir == "Si":
                    sys.exit(0)
                if menu_salir == "No":
                    confirmacion_datos()

        confirmacion_datos()

    formulario_datos()

    


