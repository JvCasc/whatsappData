# 🐢 WhatsApp Wrapped – Analisador de Conversas

Página que pega a sua **conversa do WhatsApp** e mostra **estatísticas e visualizações** sobre a conversa: quem mais mandou mensagem, dias mais ativos e etc...

> Perfeito para matar a curiosidade sobre qual amigo mais fala, quem some do grupo e como o grupo se comporta ao longo do tempo. 😅

---

## ✨ Funcionalidades

- 📂 **Importação de dados**
  - Lê o arquivo .txt contendo as mensagens exportadas do WhatsApp.
  - Usa colunas como: `data`, `hora`, `autor`, `mensagem`
  - Para pegar esse arquivo .txt do seu WhatsApp vá em "Exportar Conversa" na conversa/grupo que queria e faça o download do arquivo sem mídias.

- 📊 **Estatísticas gerais**
  - Total de mensagens.
  - Média de mensagens.
  - Mês mais movimentado do grupo.

- 🧑‍🤝‍🧑 **Ranking por participante**
  - Quem mais mandou mensagens.
  - Outas features que ainda estão por vir ⏳

- 🕒 **Atividade ao longo do tempo**
  - Distribuição das mensagens por:
    - Meses/anos.

---

## 🧠 Como funciona (visão geral)

1. O script transforma o .txt das mensagens do grupo do WhatsApp em um **.csv**.
2. O programa:
   - Lê o arquivo com **pandas**.
   - Faz alguns tratamentos básicos (datas, horários, nomes).
   - Calcula estatísticas com base nessas colunas.
   - Exibe os resultados em uma interface.

> A ideia é ser simples: você aponta o arquivo, o programa faz as contas e mostra os insights.

---

## 🛠 Tecnologias utilizadas

- **Linguagem:** Python
- **Bibliotecas principais:**
  - `pandas` – manipulação e análise da tabela de mensagens
  - `streamlit` – interface web simples e rápida (se estiver usando interface gráfica)
---

## ✅ Pré-requisitos

Instale as dependências com pip install -r requirements.txt:

