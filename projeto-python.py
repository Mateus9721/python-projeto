convenios = ["SulAmérica", "Amil", "Unimed", "Bradesco"]
locais = ["Internação", "Pronto Socorro", "Clínica", "Imagem"]

metas_convenio = {
    "SulAmérica": 100000,
    "Amil": 90000,
    "Unimed": 105000,
    "Bradesco": 95000
}

meta_hospital = 350000

valores_fixos = {
    "SulAmérica": {"Internação": 28000, "Pronto Socorro": 22000, "Clínica": 25000, "Imagem": 20000},
    "Amil": {"Internação": 25000, "Pronto Socorro": 20000, "Clínica": 20000, "Imagem": 15000},
    "Unimed": {"Internação": 35000, "Pronto Socorro": 25000, "Clínica": 30000, "Imagem": 20000},
    "Bradesco": {"Internação": 30000, "Pronto Socorro": 20000, "Clínica": 25000, "Imagem": 15000}
}

def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Mostrar faturamento de UM convênio")
    print("2 - Mostrar faturamento de TODOS os convênios")
    print("3 - Mostrar faturamento total do hospital")
    print("4 - Sair")

def submenu_locais(convenio):
    while True:
        print(f"\n--- CONVÊNIO: {convenio} ---")
        print("Escolha o local:")
        print("1 - Internação")
        print("2 - Pronto Socorro")
        print("3 - Clínica")
        print("4 - Imagem")
        print("5 - Valor total do convênio")
        print("6 - Voltar")

        try:
            escolha_local = int(input("Digite o número do local: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
            continue

        if 1 <= escolha_local <= 4:
            local_escolhido = locais[escolha_local - 1]
            valor = valores_fixos[convenio][local_escolhido]
            print(f"\n{convenio} - {local_escolhido}")
            print(f"Valor faturado: R$ {valor:.2f}")

        elif escolha_local == 5:
            total_convenio = sum(valores_fixos[convenio][local] for local in locais)
            print(f"\n--- Faturamento total do convênio {convenio} ---")
            for local in locais:
                print(f"  {local}: R$ {valores_fixos[convenio][local]:.2f}")
            print(f"\nTotal faturado pelo convênio: R$ {total_convenio:.2f}")

        elif escolha_local == 6:
            break
        else:
            print("Opção inválida. Tente novamente.")

def simular_um():
    print("\nEscolha um convênio: ")
    for i in range(len(convenios)):
        print(f"{i + 1} - {convenios[i]}")

    try:
        escolha_convenio = int(input("Digite o número do convênio: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    if 1 <= escolha_convenio <= len(convenios):
        convenio = convenios[escolha_convenio - 1]
        submenu_locais(convenio)
    else:
        print("Opção inválida. Tente novamente.")

def simular_todos():
    print("\n=== FATURAMENTO DE TODOS OS CONVÊNIOS ===")
    total_geral = 0  

    for convenio in convenios:
        print(f"\nConvênio: {convenio}")
        total_convenio = 0

        for local in locais:
            valor = valores_fixos[convenio][local]
            print(f"  {local}: R$ {valor:.2f}")
            total_convenio += valor

        print(f"Total faturado pelo convênio: R$ {total_convenio:.2f}")
        total_geral += total_convenio

    print("\n=== RESUMO FINAL ===")
    print(f"Faturamento total do hospital: R$ {total_geral:.2f}")

def meta_total():
    print("\n=== FATURAMENTO TOTAL DO HOSPITAL ===")

    total_geral = 0
    for convenio in convenios:
        total_convenio = 0
        for local in locais:
            total_convenio += valores_fixos[convenio][local]
        total_geral += total_convenio

    print(f"Faturamento total do hospital: R$ {total_geral:.2f}")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        simular_um()
    elif opcao == "2":
        simular_todos()
    elif opcao == "3":
        meta_total()
    elif opcao == "4":
        print("\nSaindo do programa...")
        break
    else:
        print("\nOpção inválida, tente novamente.")
