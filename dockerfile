# Imagem base
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos para o container
COPY requirements.txt .
COPY check_leaks.py .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando padrão
CMD ["python", "check_leaks.py"]
