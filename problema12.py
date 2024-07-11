# Diccionario con extensiones y tipos MIME
diccionario1 = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}
# Ingresar el nombre del archivo con extensión
nombre_archivo = input("Ingresa el nombre del archivo con extensión: ")

# Obtener la extensión del archivo
# Utilizamos la asignación múltiple para asignar estos dos elementos a las variables _, extension. 
# El guion bajo (_) se utiliza como un marcador para descartar el primer elemento 
# (el nombre del archivo) y solo retener la extensión.
# _, extension = nombre_archivo.split('.', 1) separa el nombre del archivo de su extensión 
# y almacena la extensión en la variable extension.
if '.' in nombre_archivo:
    _, extension = nombre_archivo.split('.', 1)
else:
    extension = ''  # Manejar el caso donde no hay extensión

# Buscar el tipo MIME en el diccionario
tipo_mime = diccionario1.get(extension.lower(), 'application/octet-stream')

print(f"El tipo de archivo MIME para '{nombre_archivo}' es: {tipo_mime}")