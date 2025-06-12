import os
import streamlit as st
import google.generativeai as genai

api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def gerar_treino(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar treino: {str(e)}"

st.title("Assistente de Treino Personalizado com IA 🏋️‍♂️")

objetivo = st.selectbox("Qual é o seu objetivo de treino?", 
                        ["Ganhar Massa Muscular", "Perder Peso", "Manter a Forma", "Aumentar Resistência", "Outro"])

nivel_dificuldade = st.slider("Escolha o Nível de Dificuldade do Treino:", 1, 5, 1)

tempo_disponivel = st.number_input("Quanto tempo você tem para treinar hoje? (em minutos)", min_value=10, step=5)

equipamentos = st.text_area("Liste os equipamentos disponíveis (se houver):", 
                             placeholder="Exemplo: halteres, barra fixa, elásticos")

restricao_fisica = st.checkbox("Possui alguma restrição física?")
restricao_str = ""
if restricao_fisica:
    restricao_str = st.text_input("Especifique a restrição física:", 
                                  placeholder="Exemplo: lesão no joelho, dor nas costas")

if st.button("Gerar Treino"):
    if objetivo and tempo_disponivel:
        with st.spinner("Montando treino..."):
            prompt = f"Crie um plano de treino personalizado para o objetivo '{objetivo}' com nível de dificuldade {nivel_dificuldade} " \
                     f"e duração de {tempo_disponivel} minutos. Considere os seguintes equipamentos disponíveis: '{equipamentos}'. " \
                     f"{f'Leve em conta a seguinte restrição física: {restricao_str}.' if restricao_fisica else ''} " \
                     f"Apresente uma lista de exercícios, número de séries e repetições, e dicas para execução."

            treino = gerar_treino(prompt)

            st.subheader("Plano de Treino:")
            st.write(treino)
    else:
        st.warning("Por favor, preencha os campos obrigatórios.")