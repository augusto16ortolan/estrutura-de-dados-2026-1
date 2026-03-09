from Hospital import Hospital

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Erro: digite um número inteiro válido.")

hospital = Hospital()

while True:
    try:
        print("\n--- MENU ---")
        print("1 - Cadastrar paciente")
        print("2 - Atender paciente")
        print("3 - Exibir ordem de atendimento")
        print("4 - Exibir quantidade em fila")
        print("5 - Sair")

        opcao = ler_inteiro("Digite a opção desejada: ")

        if opcao == 1:
            nome_paciente = input("Digite o nome do paciente: ").strip()

            if nome_paciente == "":
                print("Erro: o nome do paciente não pode ser vazio.")
                continue

            tipo_prioridade = ler_inteiro(
                "Digite o tipo de prioridade (0 - Normal, 1 - Prioridade): "
            )

            if tipo_prioridade not in [0, 1]:
                print("Erro: prioridade inválida. Use 0 ou 1.")
                continue

            hospital.cadastrar_paciente(nome_paciente, tipo_prioridade)
            print("Paciente cadastrado com sucesso.")

        elif opcao == 2:
            paciente_atendido = hospital.atender_paciente()

            if paciente_atendido is None:
                print("Não há pacientes na fila.")
            else:
                print(f"Paciente atendido: {paciente_atendido}")

        elif opcao == 3:
            hospital.exibir_order_atendimento()

        elif opcao == 4:
            hospital.exibir_quantidade_em_fila()

        elif opcao == 5:
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Erro: opção inválida.")

    except KeyboardInterrupt:
        print("\nSistema encerrado pelo usuário.")
        break
    except Exception as e:
        print(f"Erro inesperado: {e}")