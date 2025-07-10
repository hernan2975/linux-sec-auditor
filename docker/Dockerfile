
# 🔧 Imagen base liviana con Python 3
FROM python:3.11-slim

# 🏠 Directorio de trabajo dentro del contenedor
WORKDIR /app

# 📦 Instalar herramientas necesarias (nmap, john, sudo, apt-utils)
RUN apt update && \
    apt install -y nmap john sudo apt-utils && \
    apt clean

# 🐍 Copiar el código del proyecto al contenedor
COPY ./src ./src
COPY ./scripts ./scripts
COPY ./outputs ./outputs
COPY ./config ./config

# 📂 Crear carpeta para logs y reportes si no existe
RUN mkdir -p /app/outputs

# 📜 Copiar el entrypoint
COPY ./scripts/docker_entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 📌 Definir punto de entrada
ENTRYPOINT ["/entrypoint.sh"]
