class Hospital:
    def __init__(self):
        self.fila_normal = []
        self.fila_prioridade = []

    def cadastrar_paciente(self, nome_paciente, tipo_prioridade):
        try:
            nome_paciente = nome_paciente.strip()

            if not nome_paciente:
                raise ValueError("O nome do paciente não pode ser vazio.")

            if tipo_prioridade not in [0, 1]:
                raise ValueError("Tipo de prioridade inválido. Use 0 para Normal ou 1 para Prioridade.")

            if tipo_prioridade == 1:
                self.fila_prioridade.append(nome_paciente)
                print(f"Paciente '{nome_paciente}' cadastrado na fila de prioridade.")
            else:
                self.fila_normal.append(nome_paciente)
                print(f"Paciente '{nome_paciente}' cadastrado na fila normal.")

        except Exception as e:
            print(f"Erro ao cadastrar paciente: {e}")

    def atender_paciente(self):
        try:
            if self.fila_prioridade:
                return self.fila_prioridade.pop(0)

            if self.fila_normal:
                return self.fila_normal.pop(0)

            raise IndexError("Não há pacientes na fila para atendimento.")

        except Exception as e:
            print(f"Erro ao atender paciente: {e}")
            return None

    def exibir_order_atendimento(self):
        try:
            if not self.fila_prioridade and not self.fila_normal:
                print("Não há pacientes na fila.")
                return

            print("\n--- Ordem de Atendimento ---")

            if self.fila_prioridade:
                print("Fila de Prioridade:")
                for i, paciente in enumerate(self.fila_prioridade, start=1):
                    print(f"{i}. {paciente}")

            if self.fila_normal:
                print("Fila Normal:")
                for i, paciente in enumerate(self.fila_normal, start=1):
                    print(f"{i}. {paciente}")

        except Exception as e:
            print(f"Erro ao exibir ordem de atendimento: {e}")

    def exibir_quantidade_em_fila(self):
        try:
            qtd_prioridade = len(self.fila_prioridade)
            qtd_normal = len(self.fila_normal)
            qtd_total = qtd_prioridade + qtd_normal

            print("\n--- Quantidade em Fila ---")
            print(f"Prioridade: {qtd_prioridade}")
            print(f"Normal: {qtd_normal}")
            print(f"Total: {qtd_total}")

        except Exception as e:
            print(f"Erro ao exibir quantidade em fila: {e}")