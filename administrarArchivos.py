#Importamos los módulos
import os
os.system("cls")
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Url's
from_dir = "C:/Users/User/Documents/Experimento"
mi_dir = "C:/Users/User/Desktop"

diccionario = { # Diccionario se inicicliza con corchetes
    "image_files": [".gif",".png",".jpg",".jfif"],
    "video_files": [".mp3",".mp4",".AV1", ".HEIF"],
    "document_files": [".docx", ".pdf", ".pptx", ".xls"],
    "setup_files": [".exe", ".bin", ".cmd"]
}

class fileMoveHandler (FileSystemEventHandler):
    def OnCreate (self,event):
        nombre, ext = os.path.splitext(event.src_path)
        for key, value in diccionario.items():
            if ext in value:
                file_name = os.path.basename(event.src_path)# Divide la ruta en cabeza y cola y toma solo la cola, funciona bajo la lógica de os.path.splitext
                path1 = from_dir + "/" + file_name
                path2 = mi_dir + "/" + key
                path3 = mi_dir + "/" + key + "/" + file_name
                print("Descargando" + file_name)
                time.sleep(3)
                if os.path.exists(path2):
                    print("El directorio no existe")
                    print("Moviendo"+ file_name + "...")
                    shutil.move(path1,path3)
                else:
                    os.mkdir(path2) 
                    print("Moviendo"+ file_name + "...")
                    shutil.move(path1,path3)


event_handler = fileMoveHandler()
observer = Observer()

observer.schedule(event_handler,from_dir,recursive = True)# Recursive que se ejecutara continuamente
observer.start()
try:
    while True:
        time.sleep(2)
        print("Ejecutando...")
except KeyboardInterrupt:
    print("Detenido")
    observer.stop()

