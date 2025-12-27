import pandas as pd
import src.addtask as at # Importa a função add_task do módulo addtask
import src.viewtask as vt # Importa a função view_task do módulo viewtask
import src.update_task as ut # Importa a função update_task do módulo update_task

CSV_FILE = "teste.csv"


if __name__ == "__main__":

        while True:
            print("\n")
            print("=== Gerenciador de Tarefas === V. B.1.0.0 ===")
            print("1. Adicionar Tarefa")
            print("2. Exibir Tarefas")
            print("3. Atualizar Tarefa")
            print("4. Deletar Tarefa")
            print("5.Exportar Tarefas (indique caminho o será salvo em documents)")
            print("6. Análise com IA (em desenvolvimento)")
            print("7. Sair")
            input_user = input("Escolha sua opção: ")
            print("\t")

            if input_user == "1":
                at.add_task(CSV_FILE)
            elif input_user == "2":
                vt.view_task(CSV_FILE)
            elif input_user == "3":
                ut.update_task(CSV_FILE)
            elif input_user == "4":
                print("Deletar Tarefa")
            elif input_user == "7":
                print("Sair")
                break
        
            else:
              print("Opção inválida. Tente novamente.")
