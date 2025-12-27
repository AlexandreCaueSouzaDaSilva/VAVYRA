import pandas as pd

def view_task(CSV_FILE):
    try:
        df = pd.read_csv(CSV_FILE)
        print(df)
        print('\n') # Tabulação extra para melhor visualização
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")
    