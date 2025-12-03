# 🐦 Twitter Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Data-07405e?style=for-the-badge&logo=sqlite)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)

Este é um projeto de **Processamento de Linguagem Natural (NLP)** que simula uma plataforma de microblogging (semelhante ao Twitter/X). O sistema permite que o usuário escreva postagens e utiliza algoritmos para analisar automaticamente o sentimento expresso no texto, classificando-o e armazenando os dados para fins analíticos.

## 🎯 Objetivo

O objetivo principal é demonstrar a aplicação de análise de dados e NLP para entender tendências em redes sociais. O sistema classifica as interações como **"Positivo"**, **"Negativo"** ou **"Neutro"** com base na polaridade do texto inserido.

## 🖼️ Interface do Projeto

<div align="center">
  <img src="twitter.jpg" alt="Logo Twitter" width="100">
  <br>
  <i>Interface gráfica desenvolvida com CustomTkinter para inserção e visualização de posts.</i>
</div>


## 🚀 Funcionalidades

* **Análise de Sentimento (VADER):** Utiliza a biblioteca NLTK para calcular o "Compound Score" de uma frase e determinar sua polaridade.
* **Classificação Automática:**
    * 😊 **Positivo:** Score >= 0.05
    * 😐 **Neutro:** Score entre -0.05 e 0.05
    * fq😦 **Negativo:** Score <= -0.05
* **Banco de Dados Persistente:** Armazenamento local utilizando SQLite para guardar o histórico de postagens e suas respectivas pontuações.
* **Interface Gráfica (GUI):** Interface amigável construída com `customtkinter` para entrada de dados e visualização do feedback em tempo real.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Banco de Dados:** SQLite3
* **Bibliotecas Principais:**
    * `nltk` (Natural Language Toolkit) - Para a lógica de análise de sentimentos.
    * `customtkinter` - Para a construção da interface gráfica moderna.
    * `sqlite3` - Para manipulação do banco de dados.

## 📂 Estrutura do Projeto

O projeto segue uma arquitetura modular para facilitar a manutenção:

```text
/
├── database.py              # Classe responsável pela conexão e operações CRUD no SQLite
├── sentiment_analysis.py    # Lógica de classificação (Positivo/Negativo/Neutro)
├── sentiment_analysis_score.py # Retorna a pontuação bruta (float) do sentimento
├── interface_grafica.py     # Janela principal da aplicação (View)
├── main.py                  # Script para testes via terminal
├── twitter3.db              # Arquivo do banco de dados SQLite
├── img/                     # Recursos visuais (ícones, imagens)
└── README.md                # Documentação do projeto
