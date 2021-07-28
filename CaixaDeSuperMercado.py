def texto(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)

texto("Mercado Compre Bem")

valorcompra = float(input('Valor total das compras: R$'))
valorrecebido = float(input('Valor recebido: R$'))
valortroco = float(valorrecebido - valorcompra)

total = valortroco

print('O valor do troco é igual à: R$ %.2f' %(valortroco))

while (total > 0.01):

    if (total / 100 >= 1):
        ced100 = int(total / 100)
        total = total - (ced100 * 100)
        print(ced100, "Cédula(s) de R$100")

    if (total / 50 >= 1):
        ced50 = int(total / 50)
        total = total - (ced50 * 50)
        print(ced50, "Cédula(s) de R$50")

    if (total / 20 >= 1):
        ced20 = int(total / 20)
        total = total - (ced20 * 20)
        print(ced20, "Cédula(s) de R$20")

    if (total / 10 >= 1):
        ced10 = int(total / 10)
        total = total - (ced10 * 10)
        print(ced10, "Cédula(s) de R$10")

    if (total / 5 >= 1):
        ced5 = int(total / 5)
        total = total - (ced5 * 5)
        print(ced5, "Cédula(s) de R$5")

    if (total / 2 >= 1):
        ced2 = int(total / 2)
        total = total - (ced2 * 2)
        print(ced2, "Cédula(s) de R$2")

    if (total / 1 >= 1):
        ced1 = int(total / 1)
        total = total - (ced1 * 1)
        print(ced1, "Moeda(s) de R$1")

    if (total / 0.5 >= 1):
        ced05 = int(total / 0.5)
        total = total - (ced05 * 0.5)
        print(ced05, "Moeda(s) de 50 Centavos")

    if (total / 0.25 >= 1):
        ced025 = int(total / 0.25)
        total = total - (ced025 * 0.25)
        print(ced025, "Moeda(s) de 25 Centavos")

    if (total / 0.10 >= 1):
        ced010 = int(total / 0.10)
        total = total - (ced010 * 0.10)
        print(ced010, "Moeda(s) de 10 Centavos")

    if (total / 0.05 >= 1):
        ced005 = int(total / 0.05)
        total = total - (ced005 * 0.05)
        print(ced005, "Moeda(s) de 5 Centavos")

    if (total / 0.01 >= 1):
        ced001 = int(total / 0.01)
        total = total - (ced001 * 0.01)
        print(ced001, "Moeda(s) de 1 Centavo")

    texto("O Mercado Compre Bem agradece!")
