def exibir_menu():
    print("\n==== To-Do List ====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")
    print("====================")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ")
    if tarefa:
        tarefas.append({"tarefa": tarefa, "concluida": False})
        print("Tarefa adicionada com sucesso!")
    else:
        print("Você não pode adicionar uma tarefa vazia.")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa na lista.")
        return
    print("\n=== Suas Tarefas ===")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i}. {tarefa['tarefa']} {status}")

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida['tarefa']}' removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()