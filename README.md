# 📋 Cadastro de Pessoas com Validação e LGPD

Este é um projeto em Python para cadastro de pessoas, com validações de entrada, busca, exclusão e geração de relatório em JSON, seguindo princípios da **Lei Geral de Proteção de Dados Pessoais (LGPD)**.

## 💡 Funcionalidades

- ✅ Cadastro de nome, CPF e idade
- 🔍 Busca por CPF ou nome (parcial ou completo)
- 📊 Filtro por idade mínima
- 🗑️ Exclusão de pessoa por CPF
- 📁 Geração de relatório JSON
- 🔐 Consentimento do usuário conforme LGPD
- 👤 Visualização de dados com base no CPF

## 🧠 Validações

- O **CPF** deve conter exatamente 11 dígitos numéricos
- O **nome** deve conter apenas letras (espaços são permitidos)
- A **idade** deve ser um número inteiro válido

## ⚖️ LGPD (Lei 13.709/18)

Este sistema segue os princípios da LGPD:

- Informa o usuário sobre a coleta de dados
- Solicita consentimento explícito antes do cadastro
- Permite visualizar ou excluir dados a qualquer momento
- Armazena os dados localmente, sem compartilhamento com terceiros

## ▶️ Como usar

1. Execute o script:
   ```bash
   python seu_arquivo.py
   ```

2. Escolha as opções do menu:

```
--- MENU ---
1. Cadastrar pessoa
2. Buscar por CPF
3. Buscar por nome
4. Filtrar por idade
5. Excluir por CPF
6. Gerar relatório JSON
7. Sair
8. Visualizar meus dados (direito LGPD)
```

## 📝 Exemplo de saída JSON

```json
[
    {
        "nome": "Carlos Eduardo",
        "cpf": "12345678901",
        "idade": 28
    }
]
```

O relatório será salvo como `relatorio_dados.json` na mesma pasta do script.

## 🔒 Segurança (sugestão para evolução)

Este sistema é um protótipo. Para produção, recomenda-se:

- Armazenar dados criptografados
- Limitar o acesso ao arquivo JSON
- Implementar autenticação por CPF e senha
- Usar banco de dados com controle de acesso
