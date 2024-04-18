import psycopg2

def conectar():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="adaf@#swxdb",
            host="191.101.71.24",
            port="5432",
            database="sistemas"
        )

        return connection
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ao PostgreSQL:", error)

conectar()