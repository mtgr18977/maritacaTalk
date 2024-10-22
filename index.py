import openai
import streamlit as st

# Configurando a API da Maritaca
client = openai.OpenAI(
    api_key="api_key",
    base_url="api_url",
)

# Configuração da interface do Streamlit
st.title("Fale com a Maritaca")

# Caixa de entrada de texto para a mensagem do usuário
user_input = st.text_input("Digite sua mensagem:")

# Botão de enviar
if st.button("Enviar"):
    if user_input:
        # Criando a mensagem a ser enviada para a API
        messages = [
            {"role": "user", "content": user_input},
        ]

        # Chamando a API para gerar a resposta
        response = client.chat.completions.create(
            model="sabia-3",
            messages=messages,
            temperature=0.7,
            max_tokens=512,
        )

        # Extraindo a resposta da API
        answer = response.choices[0].message.content

        # Exibindo a resposta formatada
        st.markdown(f"**Resposta do chatbot:** {answer}")
    else:
        st.warning("Por favor, insira uma mensagem antes de clicar em Enviar.")
