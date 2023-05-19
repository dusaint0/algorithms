dados = {}

while True:
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    endereco = input("Digite o endereço: ")
    telefone = input("Digite o telefone: ")
    idade = input("Digite a idade: ")

    dados[cpf] = {
        "Nome": nome,
        "Endereço": endereco,
        "Telefone": telefone,
        "Idade": idade
    }

    continuar = input("Deseja continuar adicionando dados? (S/N) ")

    if continuar.lower() == "n":
        break

apagar_dicionario = input("Deseja apagar o dicionário? (S/N) ")

if apagar_dicionario.lower() == "s":
    dados.clear()
    print("Dicionário apagado com sucesso.")

procurar_cpf = input("Deseja procurar um CPF? (S/N) ")

if procurar_cpf.lower() == "s":
    cpf_procurado = input("Digite o CPF procurado: ")

    if cpf_procurado in dados:
        registro = dados[cpf_procurado]
        print("Dados encontrados:")
        print("Nome:", registro["Nome"])
        print("Endereço:", registro["Endereço"])
        print("Idade:", registro["Idade"])
        print("Telefone:", registro["Telefone"])
    else:
        print("CPF não encontrado no dicionário.")

print("Pessoas com idade maior ou igual a 18 anos:")
for cpf, registro in dados.items():
    if int(registro["Idade"]) >= 18:
        print("Nome:", registro["Nome"])
        print("Idade:", registro["Idade"])

apagar_nome = input("Deseja apagar um registro pelo nome? (S/N) ")

if apagar_nome.lower() == "s":
    nome_procurado = input("Digite o nome procurado: ")

    if nome_procurado in [registro["Nome"] for registro in dados.values()]:
        for cpf, registro in dados.items():
            if registro["Nome"] == nome_procurado:
                print("Registro encontrado:")
                print("Nome:", registro["Nome"])
                print("Idade:", registro["Idade"])
                print("Telefone:", registro["Telefone"])

                confirmacao = input("Tem certeza que deseja apagar essas informações? (S/N) ")
                if confirmacao.lower() == "s":
                    del dados[cpf]
                    print("Informações apagadas com sucesso.")
                break
    else:
        print("Nome não encontrado no dicionário.")

