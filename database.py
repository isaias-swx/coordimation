import psycopg2

def conectar():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="123",
            host="localhost",
            port="5432",
            database="sistemas-local"
        )

        return connection
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ao PostgreSQL:", error)

conectar()