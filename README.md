# Como foi feito

## Passo 1: Criar o ambiente
Criei uma instância EC2 na AWS usando a imagem Debian, pois o Ubuntu não funcionou corretamente no meu caso.

## Passo 2: Configuração do projeto
Desenvolvi um dashboard financeiro usando a biblioteca Streamlit.

O dashboard carrega dados de um arquivo CSV (MS_Financial Sample.csv) com separador ;.

Utilizei pandas para tratamento dos dados, incluindo conversão da coluna de datas e criação de uma coluna Ano-Mês para facilitar agrupamentos temporais.

## Passo 3: Funcionalidades do dashboard
Filtro lateral para seleção do país (coluna Country).

### Visualizações:

Receita por segmento (Segment).

Receita ao longo do tempo (agrupada por Ano-Mês).

Top 10 produtos por receita (Product).

Receita por canal de vendas (Sales Channel).

### Insights automáticos:

Segmento com maior receita.

Produto mais lucrativo.

Mês com maior faturamento.

Visualização opcional dos dados brutos filtrados por país.

## Passo 4: Código principal
O código usa cache para otimizar o carregamento dos dados.

Inclui tratamento de erros para leitura do CSV e verificação da existência das colunas necessárias.

Gráficos são gerados com as funções nativas do Streamlit (st.bar_chart, st.line_chart).

Instruções para rodar
Certifique-se de ter Python 3.7+ instalado.

### Instale as dependências:

bash
Copiar
Editar
pip install streamlit pandas
Coloque o arquivo MS_Financial Sample.csv na mesma pasta do script.

### Execute o dashboard:

bash
Copiar
Editar
streamlit run nome_do_seu_script.py
