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
