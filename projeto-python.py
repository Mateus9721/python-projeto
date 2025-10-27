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
    print("1 - Simular faturamento de UM convênio")
    print("2 - Simular faturamento de TODOS os convênios")
    print("3 - Mostrar meta do hospital")
    print("4 - Sair")

def simular_um():
    print("\nEscolha um convênio: ")
    for i in range(len(convenios)):
        print(f"{i + 1} - {convenios[i]}")
    escolha_convenio = int(input("Digite o número do convênio: "))

    if 1 <= escolha_convenio <= len(convenios):
        convenio = convenios[escolha_convenio - 1]
        print(f"\nConvênio seleciona: {convenio}")

        total = 0
        for local in locais:
            valor = valores_fixos[convenio][local]
            print(f"{local}: R$ {valor:.2f}")
            total += valor

        print(f"\nTotal faturado pelo convênio {convenio}: R$ {total:.2f}")
        print(f"Meta do convênio: R$ {metas_convenio[convenio]:.2f}")
        
        if total >= metas_convenio[convenio]:
            print("Meta atingida!")
        else:
            print("Meta não atingida.")
    else:
        print("Opção inválida. Tente novamente.")

def simular_todos():
    print("\n=== SIMULAÇÃO DE TODOS OS CONVÊNIOS ===")
    
    total_geral = 0  

    for convenio in convenios:
        print(f"\nConvênio: {convenio}")
        total_convenio = 0

        for local in locais:
            valor = valores_fixos[convenio][local]
            print(f"  {local}: R$ {valor:.2f}")
            total_convenio += valor

        print(f"Total faturado: R$ {total_convenio:.2f}")
        print(f"Meta do convênio: R$ {metas_convenio[convenio]:.2f}")

        if total_convenio >= metas_convenio[convenio]:
            print("Meta atingida!")
        else:
            print("Meta não atingida.")

        total_geral += total_convenio

    print("\n=== RESUMO FINAL ===")
    print(f"Faturamento total do hospital: R$ {total_geral:.2f}")
    print(f"Meta do hospital: R$ {meta_hospital:.2f}")

    if total_geral >= meta_hospital:
        print("Meta hospitalar atingida!")
    else:
        print("Meta hospitalar não atingida.")

def meta_total():
    print("\n=== META DO HOSPITAL ===")

    total_geral = 0

    for convenio in convenios:
        total_convenio = 0
        for local in locais:
            total_convenio += valores_fixos[convenio][local]
        total_geral += total_convenio

    print(f"\nFaturamento total do hospital: R$ {total_geral:.2f}")
    print(f"Meta do hospital: R$ {meta_hospital:.2f}")

    if total_geral >= meta_hospital:
        print("Meta atingida!")
    else:
        print("Meta não atingida.")
              
while True:
    mostrar_menu()
    opcao = input("\nEscolha um opção: ")

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
