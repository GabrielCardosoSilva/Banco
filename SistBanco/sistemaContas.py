def letreiro(texto, cor="padrao"):

    tamanho = 40
    linha = "=" * tamanho

    cores = {
        "padrao": "\033[m",
        "vermelho": "\033[31m",
        "verde": "\033[32m",
        "amarelo": "\033[33m",
        "azul": "\033[34m",
        "roxo": "\033[35m",
        "ciano": "\033[36m",
        "preto": "\033[37m",
    }

    print(cores[cor] + linha)
    print(texto.center(tamanho))
    print(linha + cores["padrao"])


def menu(nomeBanco):
    nome = nomeBanco.split("\\")
    letreiro(f"Banco {nome[-1].title()}")
    print("""
\033[34m[ L ]\033[m → Login
\033[32m[ C ]\033[m → Criar Conta
\033[35m[ V ]\033[m → Visualizar Usuarios
\033[31m[ S ]\033[m → Sair Do Banco
\033[33m[ R ]\033[m → Resetar Sistema Geral
""")

    alternativas = ["L", "C", "S", "R", "V"]
    resposta = ""

    while resposta not in alternativas:
        try:
            resposta = str(input("Opção: ")).upper()[0]
        except IndexError:
            continue
    return resposta


def arquivosContas():
    import os

    arquivo = str(input("Nome do Banco: "))
    destino = f"C:\\Users\\Casa\\PycharmProjects\\Banco\\bancos\\{arquivo}"

    if os.path.exists(destino):
        print(f"Banco {arquivo}, Encontrado!\n\n")
    else:
        open(destino, "a")
        print(f"Banco {arquivo} Criado com Sucesso!")
    return f"C:\\Users\\Casa\\PycharmProjects\\Banco\\bancos\\{arquivo}"


def CriarConta(cpf, nome, sobrenome, dataNascimento, senha_pessoal, arquivo):
    verificar = procurarUsuario(cpf, arquivo)
    if verificar:
        letreiro(f"Esse Usuário Já Existe um conta cadastrada!", "vermelho")
        return
    try:
        novoUsuario = f"{cpf}_{nome}_{sobrenome}_{dataNascimento}_{senha_pessoal}_0 \n"

        with open(arquivo, "a") as file:
            file.write(novoUsuario)
            letreiro(f"Novo Usuário {nome} Cadastrado com Sucesso", "verde")
    except Exception:
        print("\033[31m@@ ERRO!! TENTE NOVAMENTE  @@\033[m")


def procurarUsuario(cpf, arquivo):
    with open(arquivo, "r") as file:
        for i in file:
            dados = i.split("_")
            if dados[0] == cpf:
                return True
            else:
                return None


def reset():
    import shutil
    import os
    destino = "C:\\Users\\Casa\\PycharmProjects\\Banco\\bancos\\"
    shutil.rmtree(destino)
    os.makedirs("bancos")


def visualizar(arquivo):
    nameBanco = arquivo.split("\\")

    with open(arquivo, "r") as file:
        letreiro(f"Visualizar Contas Existente No Banco {nameBanco[-1].title()}", "roxo")
        cont = 1
        print(f"Nº \tNome")
        for i in file:
            dados = i.split("_")
            print(f"\033[35m{cont}º\t{dados[1]} {dados[2]}\033[m")
            cont += 1


def login(cpf, senha, arquivo):

    with open(arquivo, "r") as file:
        for i in file:
            dados = i.split("_")
            if dados[0] == cpf and dados[4] == senha:
                letreiro("Login foi um sucesso!", "verde")
                return True
        letreiro("Login Invalido! tente novamente...", "vermelho")
        return None


def menuConta():
    letreiro("Opções Da Sua Conta")
    print("""
[ V ] → Visualizar Dados
[ D ] → Depositar
[ S ] → Sacar
[ E ] → Extrato
[ Q ] → Sair Da Conta 
""")
    alternativas = ["V", "D", "S", "E", "Q"]
    ordem = " "
    while ordem not in alternativas:
        ordem = str(input("Opção: ")).upper()[0]
    return ordem


def visuCont(nome, sobrenome, nascimento, senha, cpf, saldo):
    import datetime
    from time import sleep

    anoAtual = datetime.date.today().year
    anoNascimento = int(nascimento[4:])
    idade = anoAtual - anoNascimento
    saldo = float(saldo)

    letreiro(f"Usuário: {nome} {sobrenome}", "azul")
    print(f"Idade:   \t{idade}")
    print(f"Nascimento:\t{nascimento[:2]}/{nascimento[2:4]}/{nascimento[4:]}")
    print(f"Saldo:    \tR${saldo:.2f}")
    print(f"CPF:    \t{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    print(f"Senha:   \t{senha}\n\n")
    sleep(1)


def entrarConta(cpf, arquivo, perfis, extrato):
    from time import sleep

    cont = casa = 0
    for c in perfis:
        if c['cpf'] == cpf:
            cpf = c['cpf']
            nome = c['nome']
            sobrenome = c['sobrenome']
            nascimento = c['data']
            senha = c['senha']
            saldo = c['saldo']
            casa = cont
        cont += 1

    ordem = " "

    while ordem not in "Q":
        ordem = menuConta()
        if ordem in "V":
            visuCont(nome, sobrenome, nascimento, senha, cpf, saldo)

        if ordem in "D":
            deposito = float(input("Quantidade que quer depositar: R$"))
            saldo += deposito
            print(f"\033[32mDeposito de R${deposito:.2f} concluido!")
            extrato += f"\033[32m{'Deposito':_<30}R${deposito:.2f}\033[m\n"

        if ordem in "S":
            limite = saldo
            if saldo > 0:
                saque = float(input("Quantidade do Saque: R$"))
                if saque > limite:
                    print("\033[31mO Saque Superou os Limites, Saque Cancelado")
                else:
                    saldo -= saque
                    print(f"\033[31mSaque de R${saque:.2f} concluido!")
                    extrato += f"\033[31m{'Saque':_<30}R${saque:.2f}\033[m\n"

        if ordem in "E":
            letreiro(f"Extrato de {nome}", 'amarelo')
            print(extrato)
            print(f"Saldo: R${saldo:.2f}\n\n")

        if ordem in "Q":
            letreiro("Saindo Da Conta", "vermelho")
            perfis[casa]['saldo'] = saldo

            with open(arquivo, 'w') as file:
                for c in perfis:
                    file.write(f"{c['cpf']}_{c['nome']}_{c['sobrenome']}_{c['data']}_{c['senha']}_{c['saldo']} \n")
                file.close()
            return extrato
        sleep(1)


def descompactar(arquivo):

    pessoas = []
    info = dict()

    with open(arquivo, "r") as file:
        for i in file:
            dados = i.split("_")
            info['cpf'] = dados[0]
            info['nome'] = dados[1]
            info['sobrenome'] = dados[2]
            info['data'] = dados[3]
            info['senha'] = dados[4]
            info['saldo'] = float(dados[5])
            pessoas.append(info.copy())
            info.clear()
    return pessoas.copy()