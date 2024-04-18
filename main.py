from database import conectar
from openpyxl import load_workbook

conn = conectar()
cursor = conn.cursor()

# Carregar a planilha Excel
try:
    workbook = load_workbook(filename='C:/Users/Isaías/Downloads/careiro-coordenadas.xlsx')
    sheet = workbook.active

    print("Planilha: Registros da planilha econtrados:")
    
    # for row in sheet.iter_rows(values_only=True):
    #     codigo_propriedade, latitude, longitude = row
    #     print("Código da Propriedade:", codigo_propriedade)
    #     print("Latitude:", latitude)
    #     print("Longitude:", longitude)
        
except FileNotFoundError:
    print("Arquivo da planilha não encontrado.")


def consulta():
    try:
        query = "select * from agrocomum.inscricaoestadual i where i.id_inscricaoestadual < 500"
        cursor.execute(query)
        
        resultados = cursor.fetchall()
        
        print("DB: Resultados econtrados")
    except Exception as e:
        print("Erro ao executar consulta:", e)

consulta()

cursor.close()
conn.close()