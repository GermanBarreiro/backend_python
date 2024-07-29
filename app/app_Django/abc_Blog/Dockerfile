# Usa una imagen oficial de Python como imagen base
FROM python:3.9

# Establece variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en el contenedor
WORKDIR /code

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de requisitos e instala las dependencias de Python
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el proyecto
COPY . /code/

# Recolecta archivos estáticos
RUN python manage.py collectstatic --noinput

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "abc_Blog.wsgi:application"]