#Importamos las librerías necesarias
import requests
import bs4
import re

#Solicitamos una página web con tiempo de espera de 2 segudos
ej1 = requests.get("http://www.pythonscraping.com/pages/warandpeace.html",
                   timeout=2)

#Imprimimos la dirección de la página web
print("\nLa página que se analizó es: \n", ej1.url, "\n")

#No imprimimos el contenido completo para facilidad de lectura del archivo
#print("\nEl contenido completo de la página es: \n", ej1.text, "\n")

#Construimos un elemento de bs4
op1 = bs4.BeautifulSoup(ej1.text)

#Extraemos los nombres de los personajes
nom1 = []  #Creamos la lista vacía
op2 = op1.findAll(
    "span", {"class": "green"}
)  #Identificamos las palabras resaltadas en verde que corresponden a los nombres
for name in op2:  #Establecemos que de cada palabra con esta condición, obtenemos el texto y lo agregamos a la lista -nom1-
    print(name.get_text())
    nom1.append(name.get_text())

print("\nLos nombres sin depurar son: \n", nom1, "\n")

#Depuramos los datos
nom2 = []  #Creamos la lista vacía
for nombre in nom1:  #Establecemos que para cada nombre en la lista -nom1-, no se repitan los nombres
    a = re.compile("\w+")
    b = a.findall(nombre)
    nom2.append(b)
print("\nLos nombres depurados son: \n", nom2, "\n")

#Extraemos solo los dialogos
op2 = op1.findAll(
    "span", {"class": "red"}
)  #Identificamos que las palabras resaltadas en rojo corresponden a los diálogos
for texto in op2:  #Establecemos que para cada texto que corresponda a los anterores criterios, se imprime a continuación
    print("\nLos diálogos del texto son: \n", texto.get_text(), "\n")

#Solicitamos una página web con tiempo de espera máximo de 2 segudos
ej2 = requests.get("https://www.py4e.com/code3/", timeout=2)
print("\nLa dirección que se analizó es: \n", ej2.url, "\n")

#No imprimimos el contenido completo para facilidad de lectura del archivo
#print("\nEl contenido completo de la página es: \n",ej1.text,"\n")

#Construimos un elemento de bs4
op3 = bs4.BeautifulSoup(ej2.text)

#Buscamos las etiqutas referentes a archivos de python
op4 = op3.findAll("a", href=re.compile("\.py$"))
print("Las etiquetas para archivos de Pyhton son: \n", op4, "\n")

#Identificamos los nombres de los archivos
arch = []  #Creamos la lista vacía
for contem in op4:  #A la lista le agregamos el tecto identificado
    arch.append(contem.get_text())
print("Los archivos de Python contenidos en ", ej2.url, "son: \n", arch, "\n")

#Profe, pude entender la ejecución de las funciones, sin embargo, no pude comprender los criterios de búsqueda para la página web que se debía utilizar, por lo tanto, utilicé los ejemplos plasmados en el taller. Muchas gracias
