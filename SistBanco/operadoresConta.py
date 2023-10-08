def visualizarConta(cpf, nome, sobrenome, nascimento, senha, saldo):
    from sistemaContas import letreiro
    import datetime

    data = f"{nascimento[:2]}/{nascimento[2:4]}/{nascimento[4:]}"
    anoNascimento = int(nascimento[4:])
    anoAtual = datetime.date.year()
    idade = anoAtual - anoNascimento


    letreiro(f"Usuário: {nome} {sobrenome}", "azul")
    print(f"Data de Nascimento: {data}")
    print(f"Idade: {idade}")
    print(f"Saldo Bancario: R${saldo:.2f}")
    print(f"CPF: {cpf}")
    print(f"Senha: {senha}")