# Ferramenta de Conversão Dolar x Real--
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("Conversor dolar x real")
preco = float(input("Digite o preço do produto em dolar:")) 
resultado = converter(preco)
print(F"O valor em reais é : {resultado:.2f}")