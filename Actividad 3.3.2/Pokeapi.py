import tkinter as tk # importando la interfaz grafica 
import requests #para hacer las solicitudes http a la APPI
from io import BytesIO #trabajar con datos binarios 
from PIL import Image, ImageTk #trabajar con imagenes en python


#Proceso de Busqueda
def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    response = requests.get(url) # solicitud a la appi mediante la URL

    if response.status_code==200: #Respuesta fue exitosa
        data = response.json()
        #definir los datos que vamos a obtener del pokemon
        nombre = data["name"]
        numero = data["id"]
        tipos = [tipos["type"]["name"] for tipos in data["types"]] #obtenemos la categoria del pokemon
        resultado =f"nombre: {nombre}\n numero del pokemon: {numero}\n tipo (s) {', '.join(tipos)}"

        imagen_url = data["sprites"]["front_default"]

        response_imagen = requests.get(imagen_url)#solicitud get url
        imagen = Image.open(BytesIO(response_imagen.content))#abrimos la imagen con BytesIO
        imagen = imagen.resize((200,200), Image.Resampling.LANCZOS)
        #redimensionando la imagen
        foto = ImageTk.PhotoImage(imagen)#Convertimos la imagen a un objeto
        label_imagen.config(image=foto)
        label_imagen.image = foto #guardando la referencia de la foto 
    else:
        resultado = "No se encontro el pokemon"
        label_imagen.config(imge=None)#eliminando la imagen en resultados negativoss
    label_resultados.config(text = resultado) #cofigura la etiqueta lable para mostrar la informacion del pokemon .


#Interfaz
window = tk.Tk()#creando la ventana
window.title("buscador de pokemon")
#campo de busqueda
entry_pokemon = tk.Entry(window)
entry_pokemon.pack()#empaqueta el campo para visualizarlo en pantalla
#btn buscar
button_buscar = tk.Button(window, text="buscar", command=buscar_pokemon)
button_buscar.pack()
#espacio o etiqueta vacia para mostrar los datos
label_resultados = tk.Label(window, text="")
label_resultados.pack()
#mostrar imagen
label_imagen =tk.Label(window)
label_imagen.pack()

window.mainloop() #inicia un bucle principal para poder mostrar la aplicacion.

