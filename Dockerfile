# Etapa 1: Base Python
FROM python:3.11-slim

# Etapa 2: Variáveis e dependências básicas
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Atualiza o sistema e instala dependências do sistema
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos do projeto
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos
COPY . .

# Expõe a porta do Flask
EXPOSE 5000

# Roda o app Flask
CMD ["python", "app.py"]
