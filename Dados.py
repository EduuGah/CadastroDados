# Este script coleta e armazena dados pessoais (nome, CPF e idade) conforme a LGPD (Lei 13.709/18).
# Os dados são usados apenas para fins de cadastro e geração de relatórios internos.
# O usuário pode consultar ou excluir seus dados a qualquer momento.

import json  # Importa a biblioteca Json (Para exportar nesse arquivo mais tarde)

# Verifica se o CPF tem 11 dígitos e se todos são dígitos numéricos (1 ao 9)
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Tira o espaço dos nomes ("Carlos Eduardo" vira "CarlosEduardo") e verifica se só tem letras
def validar_nome(nome):
    return nome.replace(" ", "").isalpha()

# Garantir que o usuário tenha consciência sobre os seus dados
def obter_consentimento():
    print("Seus dados (nome, CPF e idade) serão guardados sob sigilo, não será usado para fins indevidos.")
    print("Você poderá solicitar a explusão a qualquer momento.")
    resposta = input("Você concorda com isso? (s/n): ").strip().lower()
    return resposta == "s"

# Em tese, era pra ser o banco de dados
dados = []

# Função principal pra cadastrar pessoa
def cadastrar_pessoa():
    try:
        # Garante que o consentimento foi dado
        if not obter_consentimento():
            print("Cadastro cancelado. Consentimento não concedido.")
            return
        
        # Strip tira os espaços no fim e no começo, title deixa a primeira letra maiúscula
        nome = input("Nome completo: ").strip().title()

        # Caso o nome seja inválido, raise lança um erro no console
        if not validar_nome(nome):
            raise ValueError("Nome inválido. Use apenas letras.")
        
        # Mesmo com o nome, strip tira os espaços
        cpf = input("CPF (somente números): ").strip()

        # Mesmo que o nome, valida o CPF, caso dê erro, retorna a mensagem
        if not validar_cpf(cpf):
            raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")
        
        idade = int(input("Idade: "))

        # Cria o "Objeto" da pessoa com as informações
        pessoa = {
            "nome": nome,
            "cpf": cpf,
            "idade": idade
        }

        # Adiciona o objeto dentro de Dados
        dados.append(pessoa)
        print("✅ Pessoa cadastrada com sucesso!")

    # Alguns erros externos
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro: {e}")

# Recebe um CPF, e busca por ele dentro dos Dados
def buscar_por_cpf(cpf):
    return [p for p in dados if p["cpf"] == cpf]

# Recebe um nome (ou parte dele), e busca por ele dentro dos Dados
def buscar_por_nome(nome_busca):
    nome_busca = nome_busca.strip().lower()
    return [p for p in dados if nome_busca in p["nome"].lower()]

# Recebe uma idade, e busca por ela no dicionário
def filtrar_por_idade(min_idade):
    return [p for p in dados if p["idade"] >= min_idade]

# Exclui uma pessoa com base no CPF informado
def excluir_por_cpf(cpf):
    global dados  # Permite alterar a lista original
    original_len = len(dados)
    # Cria nova lista sem o CPF informado
    dados = [p for p in dados if p["cpf"] != cpf]
    # Verifica se alguém foi realmente removido
    if len(dados) < original_len:
        print("Usuário excluído com sucesso!")
    else:
        print("CPF não encontrado.")

# Adiciona uma opção para verificar os próprios dados
def visualizar_dados_pessoais(cpf):
    pessoa = buscar_por_cpf(cpf)
    print(pessoa if pessoa else "CPF não encontrado.")

# Cria o Json, usando a biblioteca importada no início
def gerar_relatorio_json():
    with open("relatorio_dados.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print("📄 Relatório salvo como relatorio_dados.json")

# Função principal, o menu
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar pessoa")
        print("2. Buscar por CPF")
        print("3. Buscar por nome")
        print("4. Filtrar por idade")
        print("5. Excluir por CPF")
        print("6. Vizualizar Dados Pessoais")
        print("7. Gerar relatório JSON")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            cpf = input("Digite o CPF para busca: ")
            resultado = buscar_por_cpf(cpf)
            print(resultado if resultado else "Nenhuma pessoa encontrada.")
        elif opcao == "3":
            nome = input("Digite o nome (ou parte dele): ")
            resultado = buscar_por_nome(nome)
            print(resultado if resultado else "Nenhuma pessoa encontrada.")
        elif opcao == "4":
            idade = int(input("Idade mínima: "))
            print(filtrar_por_idade(idade))
        elif opcao == "5":
            cpf = input("Digite o CPF para exclusão: ")
            excluir_por_cpf(cpf)
        elif opcao == "6":
            visualizar_dados_pessoais()
        elif opcao == "7":
            gerar_relatorio_json()
        elif opcao == "8":
            break
        else:
            print("Opção inválida.")

# Função de teste para garantir que as validações estão corretas
def testes():
    assert validar_cpf("12345678901") == True
    assert validar_cpf("abc123") == False
    assert validar_nome("João da Silva") == True
    assert validar_nome("João123") == False
    print("Tudo ok")

# Inicia o programa se estiver rodando como script principal
if __name__ == "__main__":
    testes()
    menu()
