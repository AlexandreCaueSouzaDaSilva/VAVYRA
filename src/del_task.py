import pandas as pd


def del_task(CSV_FILE):
    try:
        df = pd.read_csv(CSV_FILE)
        print(df)
        task_index = int(input("Digite o índice da tarefa que deseja deletar: "))
        
        if 0 <= task_index < len(df):
            df = df.drop(task_index).reset_index(drop=True)
            df.to_csv(CSV_FILE, index=False)
            print("\nTarefa deletada com sucesso!\n")
        else:
            print("Índice inválido.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")