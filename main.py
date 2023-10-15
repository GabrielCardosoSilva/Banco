def banco():
    from time import sleep
    from SistBanco.sistemaContas import arquivosContas, menu, letreiro, reset, CriarConta, visualizar, login, entrarConta, descompactar

    while True:
        # Sistema para carregar ou criar o arquivos com as contas dos usuario
        arquivo = arquivosContas()
        perfis = descompactar(arquivo)

        # principal
        ordem = " "
        while ordem not in "S":
            ordem = menu(arquivo)

            # reiniciar os arquivos de bancos
            if ordem in "L":
                letreiro("Login", "azul")
                cpf = str(input("Digite Seu CPF: "))
                senha = str(input("Digite Sua Senha: "))
                entrar = login(cpf, senha, arquivo)
                extrato = ''
                if entrar:
                    entrarConta(cpf, arquivo, perfis, extrato)

            elif ordem in "C":
                letreiro("Criando Conta", "verde")
                while True:
                    cpf = str(input("→CPF [11 digitos]\nDigite: "))
                    if len(cpf) == 11:
                        break
                    else:
                        print("\033[31mInválido! Número de Digito tem que ser 11\033[m")

                nome = str(input("→Nome\nDigite: ")).title()
                sobrenome = str(input("→Sobrenome\nDigite: ")).title()
                dataNascimento = str(input("→Data De Nascimento [ dd/mm/aaaa ]\nDigite: "))
                senha_pessoal = str(input("→Crie Uma Senha\nDigite: "))

                CriarConta(cpf, nome, sobrenome, dataNascimento, senha_pessoal, arquivo)
                break

            elif ordem in "V":
                visualizar(arquivo)

            elif ordem in "R":
                reset()
                letreiro("Sistema Resetado Com Sucesso" )
                break
            sleep(1)
        if ordem in "S":
            letreiro("Saindo do Sistema", "vermelho")
            break


banco()