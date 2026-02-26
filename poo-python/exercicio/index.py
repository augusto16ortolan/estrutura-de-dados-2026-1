from Banco import Banco

banco1 = Banco("Banrisul")
banco1.criar_conta("Augusto")
banco1.criar_conta("Bruno")
banco1.exibir_contas()

conta1 = banco1.recuperar_conta(1)
conta1.depositar(300)

banco1.exibir_contas()