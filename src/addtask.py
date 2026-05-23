import pandas as pd

def add_task( CSV_FILE):
    tarefa = input("Digite a tarefa: ")
    Categoria = input("Digite a categoria (projeto, finanças, TI, vídeos, etc): ")
    progresso = input("Digite o progresso (não inciado, andamento, completo): ")

    novo_registro = {
        "tarefa": tarefa,
        "categoria": Categoria,
        "progresso": progresso
    }

    try:
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([novo_registro])

    df.to_csv(CSV_FILE, index=False)
    print("\nTarefa adicionada com sucesso!\n")

