#Integrante: Jonathan Elias Gamez Larin
from PIL import Image, ImageTk, ImageFilter
from tkinter import Tk, Button, Label, filedialog, messagebox



#Con esta funcion hacemos cargar la imagen de nuestro computador, incluyendo su tamaño
def Load():
    archivo = filedialog.askopenfilename()
    global imagen4
    imagen4 = Image.open(archivo)
    imagenresiz2 = imagen4.resize((600,400),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
    
    



#Esta funciona para cambiar la tonalidad de la imagen a blanco y negro
def Black_And_White():
    global image2
    image2 = imagen4.convert("L")
    imagenresiz2 = image2.resize((600,400),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
     
    




#Esta funciona para desenfocar nuestra imagen y que se vea mas borrosa
def Blur():
    global image2
    image2= imagen4.filter(ImageFilter.BLUR)
    imagenresiz2 = image2.resize((600,400),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
    





#Con esta funcion definimos mas, las lineas de la imagen
def Outline():
    global image2
    image2= imagen4.filter(ImageFilter.CONTOUR)
    imagenresiz2 = image2.resize((600,400),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
    





#Con esta resaltamos mas la calidad de la imagen y hace que se vea mas nitida
def resaltar():
    global image2
    image2= imagen4.filter(ImageFilter.DETAIL)
    imagenresiz2 = image2.resize((600,400),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2




#Por ultimo guardamos la funcion en donde este el archivo, ya sea en descargas o en el escritorio
def Save():
 
    image2.save("guardar.jpg")
    messagebox.showinfo(title="Imagen Guardada",message="Se Ha Guardado La Imagen")
    

#Definimos el tamaño de la imagen    
ventana = Tk()
ventana.geometry("800x600")


#Aqui se mostrara el titulo de la ventana en si, ademas de su color de fondo
ventana.title("Libería Pillow- Filtro y guardado de imagenes")
ventana.configure(bg='#16c7e7')
Label2 = Label(ventana, image="")
#Le asignamos las funciones a cada boton
btnsape = Button(ventana, bg = "Blue",text="Cargar", command=Load)
btn3 = Button(ventana,bg = "white", text="Blanco/Negro", command=Black_And_White)
btn1 = Button(ventana,bg = "#5B4B49", text="Desenfoque", command=Blur)
btn2 = Button(ventana,bg = "#23967F", text="Contorno", command=Outline)
btn3_1 = Button(ventana,bg = "#DFFFD6", text="Resaltar", command=resaltar)
btn_guardar = Button(ventana,bg = "Green", text="Guardar Imagen", command=Save)

btnsape.pack()
btn3.pack()
btn1.pack()
btn2.pack()
btn3_1.pack()

btn_guardar.pack()
Label2.pack()
ventana.mainloop()