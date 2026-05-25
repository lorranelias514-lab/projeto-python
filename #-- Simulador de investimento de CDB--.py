#-- Simulador de investimento de CDB--
deposito = float(input("Digite o valor do investimento:"))
taxa = float(input("Qual a taxa do CDB em % ? "))
meses = int(input("Quantos meses vai investir ? "))
conversao = taxa / 100
total = 0
for mes in range(1, meses +1):
    total = total + deposito
    total = total + (total * conversao )
print(F"Ao final do período, você terá:R${total:.2f}")

#Lorran elias da conceição