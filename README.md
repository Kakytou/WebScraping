# WebScraping
Meu primeiro projeto de Web Scraping

# Web Scraping - Resultados da Copa do Mundo

Este projeto realiza web scraping para coletar os resultados de todas as Copas do Mundo de 1930 a 2022.
O script extrai o time da casa, placar, time visitante e o ano do campeonato, consolidando tudo em um arquivo Excel (resultados_copa.xlsx).
O objetivo é automatizar a coleta de dados históricos de futebol de maneira estruturada, facilitando análises estatísticas e estudos sobre o desempenho das seleções.

## Tecnologias e Bibliotecas

**Python** 

**requests:** para fazer requisições HTTP às páginas da Wikipedia

**BeautifulSoup:** para parsear e extrair os dados HTML

**pandas:** para manipulação e consolidação dos dados

**time.sleep:** para evitar sobrecarregar o servidor com requisições rápidas

## Funcionalidades

Coleta de resultados de todas as Copas do Mundo listadas.

Consolida os dados em um DataFrame pandas e exporta para Excel.

Automatiza requisições respeitando o intervalo de 1 segundo entre cada ano, evitando bloqueios.

## O que pratiquei

Coleta e extração de dados de páginas web com Python (requests e BeautifulSoup).

Organização e manipulação de dados usando pandas e exportação para Excel.

Automação de tarefas repetitivas e boas práticas ao acessar sites (uso de sleep).

Interpretação de estruturas HTML e aplicação de lógica em loops e funções Python.
