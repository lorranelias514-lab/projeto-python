#Simulador de investimento - Poupança--
deposito = float(input("digite o valor do Aporte "))
taxa = float(input("qual a taxa da poupança em %? "))
meses = int(input("quantos meses vai investir? "))
conversao = taxa/100
total = 0
for mes in range(1, meses +1):
    total = total + deposito
    total = total + (total * taxa)
print(f"Ao final do periodo, você terá: R${total/:.2f}")