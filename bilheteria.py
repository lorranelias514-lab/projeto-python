#aluno1: forma do nome do filme
def formatar(nome):
    return nome.upper()
#aluno2:verificação de acesso
def verificador(idade):
    if idade >= 18:
        return "autorizado"
    else:
        return "nao autorizado"
#aluno3:mensagem de retorno
def gerar_mensagem (status):
    if status == "autorizado":
       return "tenha  uma ótima sessão"
    else:
        return "sinto muito,idade não autorizada"
#aluno4:intregor do projeto
nome_filme = input("digite o nome do filme")
idade_filme = int(input("digite sua idade:"))
filme = formatar(nome_filme)
status_final = verificador(idade_filme)
mensagem = gerar_mensagem(status_final)
print(F"\n filme:{filme}")
print(F"status:{status_final}")
print(F"aviso:{mensagem}")