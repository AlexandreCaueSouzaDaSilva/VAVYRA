import pandas as pd
import src.addtask as at # Importa a função add_task do módulo addtask
import src.viewtask as vt # Importa a função view_task do módulo viewtask

def update_task(CSV_FILE):
    try:
        df = pd.read_csv(CSV_FILE)
        print(df)
        task_index = int(input("Digite o índice da tarefa que deseja atualizar: "))
        
        if 0 <= task_index < len(df):
            tarefa = input("Digite a nova tarefa (deixe em branco para manter a atual): ")
            categoria = input("Digite a nova categoria (deixe em branco para manter a atual): ")
            progresso = input("Digite o novo progresso (deixe em branco para manter o atual): ")

            if tarefa:
                df.at[task_index, 'tarefa'] = tarefa
            if categoria:
                df.at[task_index, 'categoria'] = categoria
            if progresso:
                df.at[task_index, 'progresso'] = progresso

            df.to_csv(CSV_FILE, index=False)
            print("\nTarefa atualizada com sucesso!\n")
        else:
            print("Índice inválido.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")