def fazer_backup(dicionario_principal, dicionario_backup):
    dicionario_backup.update(dicionario_principal)
    dicionario_principal.clear()

dicionario_principal = {}
dicionario_backup = {}

while True:
    nome = input("Digite a chave (ou 'sair' para encerrar): ")
    if nome == "sair":
        break
    
    idade = input("Digite o valor: ")
    
    dicionario_principal[nome] = idade
    
    if len(dicionario_principal) == 5:
        print("Dicionário principal:")
        print(dicionario_principal)
        fazer_backup(dicionario_principal, dicionario_backup)
        print("Dicionário de backup:")
        print(dicionario_backup)
        
print("Encerrando o programa. ")
