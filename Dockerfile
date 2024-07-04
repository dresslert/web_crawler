FROM python:3.12

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt requirements.txt
COPY scrapy_project news_crawler

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando a ser executado
CMD ["tail", "-f", "/dev/null"]
