#Importamos las librerías requeridas
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Adquirimos la página web con tiempo máximo de carga de 3 segundos
pagina = requests.get(
    'https://www.msn.com/es-co/deportes/futbol/futbol-colombiano/clasificacion',
    timeout=3)

#Transformamos a BeautifulSoup para identificar diferentes tipos de html y acceder a la información
soup = BeautifulSoup(pagina.content, 'html.parser')
#print(pagina.text)

#Identificamos el código de cada elemnto y lo traemos al código
eq = soup.find_all('td', class_='teamname')
#print(eq)

#Creamos una lista vacía
equipos = list()

#Utilizaremos solo los primeros 8 equipos de la clasificación
#Establecemos el inicio del conteo en 0
count = 0
#Establecemos que para cada i en eq
for i in eq:
    #Si el conteo es menor a 8, que cada item se agregue a la lista
    if count < 8:
        equipos.append(i.text)
#De lo contrario, se detiene
    else:
        break
#Y sumamos 1
    count += 1

#Imprimimos los primeros 8 equipos
print("\nLos equipos que clasificarán son:\n", equipos, "\n")

#Identificamos el código de cada elemnto y lo traemos al código
pt = soup.find_all('td', class_='points')
#print(pt)

#Creamos una lista vacía
puntos = list()

#Utilizaremos solo los primeros 8 resultados de la clasificación
#Establecemos el inicio del conteo en 0
count = 0
#Establecemos que para cada i en eq
for i in pt:
    #Si el conteo es menor a 8, que cada item se agregue a la lista
    if count < 8:
        puntos.append(i.text)
#De lo contrario, se detiene
    else:
        break
    count += 1
#Y sumamos 1

#Imprimimos los primeros 8 puntajes
print("\nLos puntos con los que clasificarán los equipos son:\n", puntos, "\n")

#Creamos un DataFrame en donde relacionaremos los equipos con los puntos
df = pd.DataFrame({
    'Nombre': equipos,
    'Puntos': puntos
},
                  index=list(range(1, 9)))#Declaramos que se haga en una lista con el rago 1-9

#Imprimimos el DataFrame
print("\nLos equipos y los puntos emparejados son:\n\n",df,"\n")

#Guardamos la información en un archivo .csv
df.to_csv('Clasificación.csv', index=False)
