from Banco import Banco

banco1 = Banco("Banrisul")

banco1.criar_conta("Bruno")
banco1.exibir_contas()

conta1 = banco1.recuperar_conta(1)
conta1.depositar(300)

conta2 = banco1.recuperar_conta(2)
conta2.depositar(700)

banco1.exibir_contas()
banco1.exibir_total_contas()
banco1.exibir_valor_total_contas()

banco1.transferir_valor_entre_contas(2, 1, 200)
banco1.exibir_contas()