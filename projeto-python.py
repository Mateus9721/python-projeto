convenios = ["SulAmérica", "Amil", "Unimed", "Bradesco"]
locais = ["Internação", "Pronto Socorro", "Clínica", "Imagem"]

metas_convenio = {
    "SulAmérica": 100000,
    "Amil": 90000,
    "Unimed": 120000,
    "Bradesco": 95000
}

meta_hospital = 350000

valores_fixos = {
    "SulAmérica": {"Internação": 28000, "Pronto Socorro": 22000, "Clínica": 25000, "Imagem": 20000},
    "Amil": {"Internação": 25000, "Pronto Socorro": 20000, "Clínica": 20000, "Imagem": 15000},
    "Unimed": {"Internação": 35000, "Pronto Socorro": 25000, "Clínica": 30000, "Imagem": 20000},
    "Bradesco": {"Internação": 30000, "Pronto Socorro": 20000, "Clínica": 25000, "Imagem": 15000}
}

while True:
    print("\n --- MENU PRINCIPAL ---")
    print("1 - Simular faturamento de UM convênio")
    print("2 - Simular faturamento de TODOS os convênios")
    print("0 - Sair.")

    escolha = int(input("Digite sua opção: "))

    if escolha == 0:
        print("Saindo do programa...")
        break

    elif escolha == 1:
        print("\nEscolha um convênio: ")
        for i in range(len(convenios)):
            print(f"{i + 1} - {convenios[i]}")

        escolha_conv = int(input("Digite o número do convênio: "))