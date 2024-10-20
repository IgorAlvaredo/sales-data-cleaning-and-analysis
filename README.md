# Dashboard de Vendas - Streamlit
## Descrição do Projeto
Este projeto é um dashboard interativo de vendas construído com Streamlit, que utiliza uma base de dados de vendas obtida no Kaggle. O objetivo é praticar a construção de dashboards, explorar os dados e gerar insights visuais dinâmicos.

## Funcionalidades
* Carregamento e exibição interativa dos dados de vendas.
* Visualização de gráficos para análise de performance.
* Gráfico de barras por produto ou categoria.
* Gráfico de linha para vendas ao longo do tempo.
* Filtros dinâmicos para selecionar períodos ou categorias específicas.
* Integração com Streamlit para uma interface web fácil de usar.
  
## Tecnologias Utilizadas
* Python
* Streamlit para criação do dashboard interativo.
* Pandas para manipulação de dados.
* Matplotlib/Seaborn para geração de gráficos (dependendo das bibliotecas que você usou).
* CSV como base de dados.

## Como Criar e Usar um Ambiente Virtual (venv)
1. Criação do Ambiente Virtual

Para manter as dependências do seu projeto isoladas, é uma boa prática usar um ambiente virtual. Execute o seguinte comando no diretório do seu projeto para criar um ambiente virtual:

  `python -m venv venv`

2. Ativação do Ambiente Virtual
   
Depois de criar o ambiente virtual, ative-o. Dependendo do seu sistema operacional, siga o comando correspondente:

* Windows:

`.\venv\Scripts\activate`

* Linux/MacOS:

    `source venv/bin/activate`

3. Instalação de Dependências
   
Com o ambiente virtual ativado, você pode instalar as dependências do projeto (como Streamlit e Pandas) usando o arquivo requirements.txt:

  `pip install -r requirements.txt`

4. Desativar o Ambiente Virtual
   
Quando você terminar de trabalhar no projeto, pode desativar o ambiente virtual com o seguinte comando:

  `deactivate`
  
##  Como Executar o Projeto
1. Clone este repositório:

`git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio`

2.  Instale as dependências necessárias:

`pip install -r requirements.txt`

3. Execute o aplicativo Streamlit:

`streamlit run dashboard.py`

4. Abra o navegador na URL que será exibida no terminal, algo como:

http://localhost:8501

## Base de Dados
A base de dados utilizada neste projeto foi obtida no Kaggle. Ela contém informações sobre vendas, como:

Produtos
* Quantidades vendidas
* Datas de transações
* Preços unitários

## Como Contribuir
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
