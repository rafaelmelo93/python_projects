---
#title: Documentação do Projeto: Teste de Velocidade da Internet com Streamlit
---
Objetivo:
Este projeto permite realizar um teste de velocidade de internet (download, upload e ping) através de uma interface web, utilizando o Streamlit para a interface gráfica e a biblioteca speedtest-cli para medir a velocidade da rede.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Passo 1: Ter o Python e o PIP instalados
Antes de começar a usar o código, é necessário garantir que o Python e o pip (gerenciador de pacotes do Python) estão instalados no seu sistema.

Verificar se o Python está instalado: Abra o terminal (ou Prompt de Comando) e digite o seguinte comando: python --version

ou, se estiver usando o Python 3 especificamente: python3 --version

Caso o Python não esteja instalado, você pode baixá-lo e instalá-lo a partir do site oficial do Python. Durante a instalação, certifique-se de marcar a opção "Add Python to PATH".

Verificar se o pip está instalado: O pip geralmente vem instalado com o Python. Para verificar se o pip está instalado, digite: pip --version ou: pip3 --version

Caso não tenha o pip instalado, você pode instalar manualmente com o seguinte comando: python -m ensurepip --upgrade
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Passo 2: Criando um Ambiente Virtual (Essa parte é opicional)
Criar um ambiente virtual ajuda a manter as dependências do seu projeto isoladas, evitando conflitos com outras versões de pacotes no sistema.

Para criar um Ambiente Virtual: No terminal, dentro da pasta do seu projeto, execute: python -m venv venv

Ativar o Ambiente Virtual (windows): venv\Scripts\activate
No macOS ou Linux: source venv/bin/activate

Após a ativação, você verá (venv) no início da linha de comando, indicando que o ambiente virtual está ativo.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Passo 3: Instalando as Dependências
O seu projeto utiliza as bibliotecas streamlit e speedtest-cli. Para instalá-las, execute os seguintes comandos no terminal:

Instalar o Streamlit: pip install streamlit
Instalar o Speedtest-cli: Instalar o Speedtest-cli:
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Passo 4: Preparando o Código
Criar um arquivo Python: Crie um arquivo Python na pasta do seu projeto.

Use o código a seguir e faça as alterações que considerar necessárias:

Código:
~~~~python
import streamlit as st # É usado para criar a interface gráfica da aplicação web. O alias st é utilizado para simplificar a chamada de funções do Streamlit.
import speedtest # Importa o módulo speedtest-cli, que é utilizado para realizar o teste de velocidade da internet (download, upload e ping).

def main(): #Função principal 
    st.header("Teste de Velocidade", divider=True) # Título. O divider=True adiciona uma linha divisória abaixo do título.
    st.write('Para iniciar o teste, clique no botão abaixo.') # Texto de instrução
    #Botão com configuração
    if st.button('Testar velocidade'):
        with st.spinner('Sua internet está sendo verificada, só um momento...'): # Texto durante a verificação do teste

            # Configuração e execução do Speedtest
            s = speedtest.Speedtest() # Cria um objeto da classe Speedtest, que permite interagir com a funcionalidade de teste de velocidade da internet.
            s.get_best_server() # Seleciona o servidor mais próximo e com a melhor latência para realizar o teste de velocidade.

            # Medição de velocidade de download e upload
            download_speed = s.download() / 1_000_000  # em Mbps
            upload_speed = s.upload() / 1_000_000  # em Mbps

            results = s.results.dict() # Retorna o resultado do teste em formato de dicionário (Ping, upload, dowload e servidor)

            max_speed = 100  # Defina a velocidade máxima para o gráfico de progresso

            st.write(f'Velocidade de Download: {download_speed:.2f} Mbps') 
            st.progress(min(download_speed / max_speed, 1.0)) # Exibe uma barra de progresso que indica a porcentagem de preenchimento com base na velocidade de download

            st.write(f'Velocidade de Upload: {upload_speed:.2f} Mbps')
            st.progress(min(upload_speed / max_speed, 1.0)) # Exibe uma barra de progresso para a velocidade de upload

            st.write(f"Ping: {results['ping']} ms") # Exibe o valor de ping (latência) em milissegundos

# Execução da função
# para executar, rode o comando: streamlit run Speed.py
main()
~~~~
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Passo 5: Executando o Projeto
Para executar a aplicação, siga estas etapas:

No terminal, dentro da pasta do seu projeto, digite o seguinte comando para rodar o Streamlit: streamlit run nomedoProjeto.py

Acessar a aplicação: O Streamlit iniciará um servidor local e fornecerá um endereço para você acessar no navegador (geralmente algo como http://localhost:8501).
Caso não abra no navegado, use o link exibido no terminal copiando e colando ou apenas segure o ctrl e clique com o mouse.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Interagir com o aplicativo:

O título que deficniu será exibido.
Ao clicar no botão Testar velocidade", o aplicativo começará a medir a velocidade da internet e exibirá os resultados, incluindo a velocidade de download, upload e ping, com barras de progresso visualizando os valores em Mbps.


