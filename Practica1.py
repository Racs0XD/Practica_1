from logging import exception
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from django.urls import re_path    
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import sys


def buscador_archivo():
    artemp = ""
    try:
        archivo = filedialog.askopenfilename(title="Selección de archivo data",initialdir="./",filetypes=(("data files","*.data"),("all files","*.*")))
        with open(archivo,encoding='utf-8') as cargado:
            artemp = cargado.read().strip()
    except:
        print('Seleccione un archivo')
        return
    ordenado(artemp)

def ordenado(data):        
    temp = ""
    data = data.lower()
    es_comilla = False
    for caracter in data:
        if caracter != '\"':
            if (caracter != " " and caracter != "\n" and caracter != "\t") or es_comilla:
                temp += caracter
        elif not es_comilla:
            temp += caracter
            es_comilla = True
        else:
            temp += caracter
            es_comilla = False
    print("Archivo .data cargado satisfactoriamente")
    print(temp)
    global cadena
    cadena = temp
    
def data():
    global lista, ltitulo, data_vacio
    ltitulo = []
    lista = []
    cont = 0
    mes = ""
    anio = ""
    nombre = ""
    precio = ""
    vendido = ""    
    data_vacio = False
    mesval = True
    anioval = True
    productoval = True
    nombreval = True
    precioval = True
    vendidoval = True    
    comilla = False
    for letra in cadena:
        if mesval is True:
            if letra !=":":
                mes += letra
            else:
                mesval = False
        elif anioval is True:
            if letra != "=":
                anio += letra
            else:
                anioval = False
        elif productoval is True:
            if letra != "]":
                if letra == "(" or letra == "[" or letra == ")" or letra == "\"":
                    if letra == "\"" and comilla is False:
                        comilla = True
                    elif letra == "\"" and comilla is True:
                        comilla = False         
                else:
                    if nombreval is True:       
                        if letra != ",": 
                            nombre += letra                                          
                        elif comilla is True:
                            nombre += letra 
                        elif comilla is False:
                            nombreval = False  
                    elif precioval is True:
                        if letra != ",":
                            precio += letra    
                        else:
                            precioval = False
                    elif vendidoval is True:
                        if letra != ",":
                            vendido += letra    
                        else:
                            vendidoval = False                                                  
            else:
                productoval = False
        if letra == ";":
            if nombre == "" or nombre == None or precio == "" or precio == None or vendido == "" or vendido == None:
                print("Información falantane en archivo data, no se cargo la información")
                lista.clear()
                data_vacio = True
            else:
                ganancia = float(precio) * int(vendido)
                tem = {
                        "nombre":nombre,
                        "ganancia":ganancia
                                }      
                lista.append(tem)
                nombre = ""
                precio = ""
                vendido = ""  
                productoval = True
                nombreval = True
                precioval = True
                vendidoval = True
    
    titulo_aux = {
                "titulo":mes+" - "+anio
        }
    
    ltitulo.append(titulo_aux)
def buscador_archivo_2():
    artemp = ""
    try:
        archivo = filedialog.askopenfilename(title="Selección de archivo data",initialdir="./",filetypes=(("lfp files","*.lfp"),("all files","*.*")))
        with open(archivo,encoding='utf-8') as cargado:
            artemp = cargado.read().strip()            
    except:
        print('Seleccione un archivo')
        return
    ordenado_2(artemp)

def ordenado_2(data):        
    temp = ""
    data = data.lower()
    es_comilla = False
    for caracter in data:
        if caracter != '\"':
            if (caracter != " " and caracter != "\n" and caracter != "\t") or es_comilla:
                temp += caracter
        elif not es_comilla:
            temp += caracter
            es_comilla = True
        else:
            temp += caracter
            es_comilla = False
    print("Archivo .lfp cargado satisfactoriamente")
    print(temp)
    global lf
    lf = temp

def lfp():
    global instrucciones, lfp_vacio
    instrucciones = {}
    temp = ""
    nombre = ""
    grafica = ""
    titulo = ""
    titulox = ""
    tituloy = ""    
    nombreval = False
    graficaval = False
    tituloval = False
    tituloxval = False
    tituloyval = False    
    comp = True
    lfp_vacio = False
    for letra in lf:
        if letra == "<" or letra == "¿":
                    ""
        else:
            if comp is True:
                if letra != ":":
                    temp +=letra
                    if temp == "nombre" or temp == "nómbre":   
                        nombreval = True
                    elif temp == "gráfica" or temp =="grafica":
                        graficaval = True
                    elif temp == "títulox" or temp =="titulox":
                        tituloxval = True
                    elif temp == "títuloy" or temp =="tituloy":
                        tituloyval = True                 
                    elif temp == "título" or temp =="titulo":
                        tituloval = True
                else:
                    temp = ""
                    comp = False 
            elif nombreval is True:
                if letra != "," and letra != "?":
                    nombre += letra
                else:
                    nomb = nombre.replace("\"","")
                    if nomb == "" or nomb == None:
                        print("Hace falta el nombre de la gráfica")
                        lfp_vacio = True
                    else:
                        instrucciones["nombre"] = nomb
                        nombre = ""
                        nombreval = False
                        comp = True
            elif graficaval is True:
                if letra != "," and letra != "?":
                    grafica += letra
                else:
                    graf = grafica.replace("\"","")
                    if graf == "" or graf == None:
                        print("Hace falta especificar el tipo de gráfica")
                        lfp_vacio = True
                    else:                        
                        instrucciones["grafica"]=graf
                        grafica = ""
                        graficaval = False
                        comp = True
            elif tituloxval is True:
                if letra != "," and letra != "?":
                    titulox += letra
                else:
                    instrucciones["titulox"]=titulox.replace("\"","")
                    tituloxval = False
                    titulox = ""
                    comp = True
            elif tituloyval is True:
                if letra != "," and letra != "?":
                    tituloy += letra
                else:
                    instrucciones["tituloy"]=tituloy.replace("\"","")
                    tituloy = ""
                    tituloyval = False
                    comp = True
            elif tituloval is True:
                if letra != "," and letra != "?":
                    titulo += letra
                else:
                    instrucciones["titulo"]=titulo.replace("\"","")
                    titulo = ""
                    tituloval = False
                    comp = True
    
  



def graph():
    try:
        lfp()
        data()       
    except Exception as e:
        print(e)
    

    if lfp_vacio is True:
        print("Hace falta información para graficar")
    elif data_vacio is True:
        print("Hace falta información para graficar")
    else:
    
        
        x = []
        y = []    
        for rank in range(len(lista)):
            x.append(lista[rank]['nombre'])
            y.append(lista[rank]['ganancia'])

        x1 = list(reversed(x))
        y1 = list(reversed(y))

        if "titulox" in instrucciones:
            titulox = instrucciones["titulox"]
        else:
            titulox = ""

        if "tituloy" in instrucciones:
            tituloy = instrucciones["tituloy"]
        else:
            tituloy = ""
        
        if "titulo" in instrucciones:
            titulo = instrucciones["titulo"]
        else:
            titulo = ltitulo[0]["titulo"]
        
        nombre = instrucciones["nombre"]+".png"

        if instrucciones["grafica"] == "barras":
            x_pos = np.arange(len(x1))    
            plt.bar(x_pos,y1)    
            plt.xlabel(titulox, size=16)
            plt.ylabel(tituloy, size=16)
            plt.title(titulo, fontdict={'family': 'serif', 
                        'color' : 'darkblue',
                        'weight': 'bold',
                        'size': 18})
            plt.xticks(x_pos, x1, rotation=90)
            plt.grid(True)
            plt.savefig(nombre)
            plt.show()            
            plt.close()
        elif instrucciones["grafica"] == "lineas":        
            plt.plot(x1, y1, marker = 'o')
            plt.xlabel(titulox, size=16)
            plt.ylabel(tituloy, size=16)
            plt.title(titulo, fontdict={'family': 'serif', 
                        'color' : 'darkblue',
                        'weight': 'bold',
                        'size': 18})
            plt.grid(True)
            plt.savefig(nombre)
            plt.show()
            plt.close()
        elif instrucciones["grafica"] == "pastel" or instrucciones["grafica"] == "pie": 
            plt.pie(y1, labels= x1) 
            plt.title(titulo, fontdict={'family': 'serif', 
                        'color' : 'darkblue',
                        'weight': 'bold',
                        'size': 18})   
            plt.savefig(nombre)
            plt.show()
            plt.close()
    
    
import webbrowser

def reporte():
    try:
        data()
    except Exception as e:
        print(e)
    
    if data_vacio == False:

        f = open('Reporte.html', 'w')   
        re = lista
        
        for i in range(len(re)):
            for j in range(len(re)-1):
                if (int(re[j]['ganancia']) < int(re[j+1]['ganancia'])):
                    temp = re[j]
                    re[j] = re[j+1]
                    re[j+1] = temp

        for a in range(len(re)):
            menos_vendido = re[a]["nombre"]

        mas_vendido = re[0]["nombre"]

        html_cabeza = """
        <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte</title>
    </head>

    <body>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">



    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand"> &nbsp;&nbsp;&nbsp;Reporte</a>
    </nav>

    """
        html_info = """
        <center>
        <h2>
        Oscar Eduardo Morales Giron
        </h2><br>
        <h2>
        201603028
        </h2>
        </center>
        <br>
        <br>
        """
        html_header = '''
        <center>
        <h3>
        Ganancias Generadas
        </h3>
        </center>
        <table border="1", style="margin: 0 auto;",class="default">
        <tr>
        <th>Nombre del Producto</th>
        <th>Ganancia</th>
        </tr>
        '''
        html_mid = ''
        for a in range(len(re)):
            n = re[a]["nombre"]
            g = re[a]["ganancia"]
            html_mid += '''<tr>
        <td>{}</td>
        <td>{}</td>
        </tr>'''.format(n,g)

        hmtl_end = """</table><br><br>
        <center>
        <h2>
        Producto mas vendido
        </h2>
        <h3>
        {}
        </h3><br>
        <h2>
        Producto menos vendido
        </h2>
        <h3>
        {}
        </h3><br>
        </center>
        """.format(mas_vendido,menos_vendido)


        html_pie="""
    

        <br><br><br><br><br><br>
        <footer>
        </footer>

        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
    </body>
    <style>
        table {
        border: #b2b2b2 1px solid;
        border-collapse: separate;
        
        }
        th {
        border: black 1px solid;
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #357baa;
        color: white;
        }
        td, th {
        border: 1px solid #ddd;
        padding: 8px;
        }
        
        tr:nth-child(even){background-color: #c0c0c0;}
        
        tr:hover {background-color: #ddd;}
        
        
        </style>

    </body>
        """

        html = html_cabeza + html_info + html_header + html_mid + hmtl_end + html_pie
        
        f.write(html)     
        f.close()     
        file = webbrowser.open('Reporte.html')  
    else:
        print("No se a podido generar el reporte debido a la falta de información")
    


Salir = False
opcion = 0

while not Salir:
    print("------------ Sistema--------")
    print("1. Cargar Data")
    print("2. Cargar Instrucciones")
    print("3. Analizar")
    print("4. Reportes")
    print("5. Salir")
    print("--------------------------------------")

    menu = (input("Opcion: "))
    if menu.isdigit():
        menu = int(menu)
        if menu == 1:
            buscador_archivo()
        elif menu == 2:
            buscador_archivo_2()
        elif menu == 3:
            graph()
        elif menu == 4:
            reporte()
        elif menu == 5:
            exit()
    else:
            print("Debe ingresar una opcion valida ")
