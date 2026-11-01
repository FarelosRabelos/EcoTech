# EcoTech — Sistema de Gerenciamento de Resíduos Eletrônicos

O **EcoTech** é um sistema desenvolvido em Python para auxiliar no gerenciamento de equipamentos eletrônicos recebidos em pontos de coleta, permitindo registrar, consultar, atualizar e acompanhar a destinação desses materiais.

O projeto foi idealizado como parte da disciplina **Projeto Integrador — Laboratório de Programação**, do curso de Engenharia de Software da Universidade Santo Amaro (UNISA).

## Objetivo

Desenvolver uma aplicação administrativa que facilite o controle de resíduos eletrônicos, substituindo registros manuais por um sistema organizado, com armazenamento persistente e ferramentas de consulta.

O projeto também busca aplicar conceitos de lógica de programação, estruturas de dados, funções, manipulação de arquivos JSON e algoritmos de busca.

## Funcionalidades

O EcoTech possui as seguintes funcionalidades principais:

- **Cadastro de equipamentos:** registro de novos dispositivos, com geração automática de códigos únicos.
- **Listagem:** visualização dos equipamentos cadastrados e suas informações.
- **Pesquisa:** localização de equipamentos por código utilizando busca sequencial.
- **Atualização:** alteração de nome, marca, condição e peso dos dispositivos.
- **Controle de status:** acompanhamento das etapas de avaliação e processamento dos equipamentos.
- **Registro de destinação:** classificação dos equipamentos conforme seu encaminhamento.
- **Armazenamento em JSON:** persistência dos registros entre execuções do programa.

### Status dos equipamentos

O sistema foi planejado para utilizar os seguintes status padronizados:

| Status | Descrição |
|---|---|
| Aguardando avaliação | Equipamento recebido e ainda não avaliado |
| Em avaliação | Equipamento em processo de análise |
| Aguardando destinação | Equipamento aguardando encaminhamento |
| Finalizado | Processo de destinação concluído |
| Outro | Situação personalizada |

### Tipos de destinação

- Reciclagem
- Reutilização
- Tratamento especializado
- Outro, com descrição personalizada

## Tecnologias utilizadas

- **Python 3:** linguagem principal da aplicação.
- **JSON:** formato utilizado para armazenar os registros.
- **Visual Studio Code:** ambiente de desenvolvimento.
- **Git e GitHub:** versionamento e disponibilização do código-fonte.

O sistema foi desenvolvido inicialmente para execução no terminal, sem necessidade de interface gráfica ou banco de dados externo.

## Estrutura do projeto

```text
EcoTech/
│
├── main.py
├── equipamentos.py
├── buscas.py
├── relatorios.py
│
└── dados/
    └── equipamentos.json
```

**Descrição dos arquivos:**

- `main.py`: menu principal e navegação.
- `equipamentos.py`: cadastro, atualização e gerenciamento dos equipamentos.
- `buscas.py`: pesquisa de equipamentos por código.
- `relatorios.py`: módulo reservado para geração de relatórios.
- `dados/equipamentos.json`: base de registros dos equipamentos.

## Como executar

### Pré-requisitos

É necessário ter o Python 3 instalado no computador.

### Passo 1 — Obter o projeto

Clone o repositório pelo Git ou baixe os arquivos para uma pasta local.

### Passo 2 — Acessar a pasta

No terminal, navegue até o diretório principal:

```bash
cd EcoTech
```

### Passo 3 — Executar

```bash
python3 main.py
```

O menu principal será apresentado no terminal.

```text
===================================================
                    ECOTECH
 Sistema de Gerenciamento de Resíduos Eletrônicos
===================================================

1 - Cadastrar Equipamento
2 - Listar Equipamentos cadastrados
3 - Pesquisar Equipamentos cadastrados
4 - Atualizar Equipamentos cadastrados
5 - Registrar Destinação
6 - Visualizar Relatórios
0 - Sair do sistema
```

Algumas funcionalidades podem estar em desenvolvimento, conforme a versão do projeto.

## Estrutura dos registros

Cada equipamento possui um identificador numérico e informações administrativas.

Exemplo:

```json
{
  "codigo": 1001,
  "equipamento": "Notebook",
  "marca": "Dell",
  "condicao": "novo",
  "peso": 0.15,
  "data_entrada": "2023-01-01",
  "status": "disponivel",
  "destinacao": "reutilizacao"
}
```

A base inicial de testes contém 200 registros fictícios de equipamentos eletrônicos, utilizados para desenvolver e validar os algoritmos de pesquisa.

## Conceitos de programação aplicados

Durante o desenvolvimento do EcoTech são trabalhados:

- Variáveis e tipos de dados.
- Estruturas condicionais (`if`, `elif`, `else`).
- Laços de repetição (`for`, `while`).
- Funções e modularização.
- Listas e dicionários.
- Leitura e escrita de arquivos JSON.
- Validação de entradas.
- Busca sequencial por identificador.

## Melhorias planejadas

- [ ] Concluir e validar os menus de status e destinação.
- [ ] Implementar relatórios estatísticos.
- [ ] Desenvolver busca binária.
- [ ] Implementar árvore binária de busca.
- [ ] Comparar o desempenho dos algoritmos com diferentes volumes de registros.
- [ ] Melhorar a navegação e a apresentação das informações.
- [ ] Avaliar a criação de uma interface web utilizando Flask, HTML e CSS.

## Finalidade acadêmica

O EcoTech é um projeto acadêmico desenvolvido para aplicar os conhecimentos adquiridos na graduação em Engenharia de Software.

Seu objetivo é demonstrar a construção de uma solução computacional para um problema de gerenciamento de resíduos eletrônicos, desde a definição dos requisitos até a implementação e os testes.

Os dados iniciais de equipamentos são fictícios e utilizados exclusivamente para desenvolvimento e experimentação.

## Autor

**Fabrício Paz**

Engenharia de Software — Universidade Santo Amaro (UNISA)

Projeto Integrador — Laboratório de Programação
