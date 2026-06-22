#Etapa 1 - calculo do IMC
def calc_imc(imc):
 imc = peso/ (altura*altura)
 retur imc

 #Etapa 2 - classificarção do IMC
 def classificar_imc(resultado):
     if resultado >= 25:
          return "ACIMA DO PESO"
    else:
       return "PESO NORMAL"
#Etapa 3 - Mensagem de Retorno
def mensagem(status):
    if status == "ACIMA DO PESO":
        return "Atenção! Procure um médico"
    else:
        return "Seu peso está Normal! continue Assim"

#Etapa 4 - integração do Código
valor_peso = float(input("Digite o seu peso: "))
valor_altura = float(input("Digite sua altura: "))

valor_imc = calc_imc(valor_peso,valor_altura)
resultado_imc = classificar_imc(valor_imc)
saida = mensagem(resultado_imc)

print("="*50)
print("")