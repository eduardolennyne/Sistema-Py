def exibir_menu():
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")

def cadastrar_paciente(pacientes):
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome do paciente: ").strip()
    
    # Validação de idade
    while True:
        try:
            idade = int(input("Idade: "))
            if idade <= 0:
                print("A idade deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Idade inválida! Digite apenas números.")

    telefone = input("Telefone: ").strip()

    pacientes.append({
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    })

    print("Paciente cadastrado com sucesso!")

def ver_estatisticas(pacientes):
    if not pacientes:
        print("\nNenhum paciente cadastrado ainda!")
        return

    total = len(pacientes)
    idade_media = sum(p["idade"] for p in pacientes) / total
    paciente_mais_novo = min(pacientes, key=lambda p: p["idade"])
    paciente_mais_velho = max(pacientes, key=lambda p: p["idade"])

    print("\n--- Estatísticas da Clínica ---")
    print(f"Total de pacientes: {total}")
    print(f"Idade média: {idade_media:.2f} anos")
    print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")

def buscar_paciente(pacientes):
    nome_busca = input("\nDigite o nome do paciente para buscar: ").strip().lower()

    encontrados = [p for p in pacientes if nome_busca in p["nome"].lower()]

    if encontrados:
        print("\n--- Pacientes encontrados ---")
        for p in encontrados:
            print(f"Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
    else:
        print("Nenhum paciente encontrado com esse nome.")

def listar_pacientes(pacientes):
    if not pacientes:
        print("\nNenhum paciente cadastrado ainda!")
        return

    print("\n--- Lista de Pacientes ---")
    for p in pacientes:
        print(f"Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")

def main():
    pacientes = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_paciente(pacientes)
        elif opcao == "2":
            ver_estatisticas(pacientes)
        elif opcao == "3":
            buscar_paciente(pacientes)
        elif opcao == "4":
            listar_pacientes(pacientes)
        elif opcao == "5":
            print("Saindo do sistema... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            
def pode_atender_consulta_normal(A, B, C, D):
    # (A AND B AND C) OR (B AND C AND D)
    return (A and B and C) or (B and C and D)

def pode_atender_emergencia(B, C, D):
    # C AND (B OR D)
    return C and (B or D)
    
# Exemplo de uso:
print("=== Sistema de Controle de Atendimento ===")

A = bool(int(input("Tem agendamento? (1=Sim, 0=Não): ")))
B = bool(int(input("Documentos em dia? (1=Sim, 0=Não): ")))
C = bool(int(input("Há médico disponível? (1=Sim, 0=Não): ")))
D = bool(int(input("Pagamentos em dia? (1=Sim, 0=Não): ")))

tipo = input("Tipo de atendimento (N = Normal / E = Emergência): ").upper()

if tipo == "N":
    if pode_atender_consulta_normal(A, B, C, D):
        print("✔ Paciente pode ser atendido na CONSULTA NORMAL.")
    else:
        print("✘ Atendimento NÃO permitido para consulta normal.")

elif tipo == "E":
    if pode_atender_emergencia(B, C, D):
        print("✔ Paciente pode ser atendido na EMERGÊNCIA.")
    else:
        print("✘ Atendimento NÃO permitido em emergência.")

else:
    print("Tipo inválido.")

            
# Executa o programa
main()