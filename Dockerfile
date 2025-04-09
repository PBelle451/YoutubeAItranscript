# Etapa 1: imagem base com Python 3.11
FROM python:3.11-slim

# Etapa 2: evitar arquivos bytecode e buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Etapa 3: diretório de trabalho
WORKDIR /app

# Etapa 4: instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Etapa 5: copiar apenas o requirements.txt e instalar as libs primeiro
COPY requirements.txt . 
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 6: copiar o restante do projeto
COPY . /app/

# Etapa 7: expor a porta
EXPOSE 5000

# Etapa 8: comando para rodar o app
CMD ["python", "app.py"]
