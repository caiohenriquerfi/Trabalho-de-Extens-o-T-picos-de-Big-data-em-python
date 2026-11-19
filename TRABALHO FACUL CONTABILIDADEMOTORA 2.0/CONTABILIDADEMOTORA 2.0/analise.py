import pandas as pd

# Link de exportação direta otimizado para o Google Sheets
sheet_id = "1QCm46C3s8jewcUm1QS2eARJCpNlyG2chhWhQOS3sREw"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

print("A descarregar dados da folha...")
df = pd.read_csv(url)

print("\n--- DADOS DA PWA NO PANDAS ---")
print(df)

print("\nAnálise concluída com sucesso!")