# Usa imagen base ligera de Python 3.10
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requisitos y luego instala dependencias
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto de los archivos (app.py, templates, etc)
COPY . .

# Expone el puerto 5000 para acceder a la app
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]

