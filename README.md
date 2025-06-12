# Assistente de Treino Personalizado com IA 🏋️‍♂️

## Descrição
Este projeto é um **Assistente de Treino Personalizado com IA**, desenvolvido com **Streamlit** e integrado à API **Gemini** da Google Generative AI. Ele permite que os usuários criem planos de treino personalizados com base em seus objetivos, nível de dificuldade, tempo disponível, equipamentos e possíveis restrições físicas. A IA utiliza técnicas de **Prompt Engineering** para gerar treinos detalhados e adaptados às necessidades individuais.

---

## Funcionalidades
1. **Objetivo de Treino**: O usuário pode selecionar o objetivo principal do treino, como:
   - Ganhar Massa Muscular
   - Perder Peso
   - Manter a Forma
   - Aumentar Resistência
   - Outro

2. **Nível de Dificuldade**: Um slider permite que o usuário escolha o nível de dificuldade do treino, variando de 1 (Muito Fácil) a 5 (Desafiador).

3. **Tempo Disponível**: O usuário informa o tempo disponível para o treino, em minutos.

4. **Equipamentos Disponíveis**: O usuário pode listar os equipamentos que possui, como halteres, barra fixa, elásticos, etc.

5. **Restrições Físicas**: Caso o usuário tenha alguma restrição física (ex.: lesão no joelho, dor nas costas), ele pode especificá-la para que o treino seja adaptado.

6. **Geração de Treino**: Ao clicar no botão "Gerar Treino", o sistema utiliza a API Gemini para criar um plano de treino personalizado, incluindo:
   - Lista de exercícios
   - Número de séries e repetições
   - Dicas para execução

---

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Streamlit**: Framework para criar interfaces web interativas.
- **Google Generative AI (Gemini)**: API para geração de conteúdo com IA.
- **Prompt Engineering**: Técnica para estruturar prompts que guiam a IA na geração de respostas relevantes.

---

## Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior.
- Instalar as dependências:
  ```bash
  pip install streamlit google-generativeai
  ```

### Configuração da API
- Defina a variável de ambiente `GOOGLE_API_KEY` com sua chave de API da Google Generative AI.

### Executar o Projeto
1. No terminal, execute:
   ```bash
   streamlit run main.py
   ```
2. Abra o navegador e acesse o link fornecido pelo Streamlit (geralmente `http://localhost:8501`).

---

## Exemplo de Uso
1. Escolha o objetivo do treino, como "Ganhar Massa Muscular".
2. Defina o nível de dificuldade (ex.: 3).
3. Informe o tempo disponível (ex.: 45 minutos).
4. Liste os equipamentos disponíveis (ex.: halteres, barra fixa).
5. Caso tenha restrições físicas, especifique-as (ex.: lesão no joelho).
6. Clique em "Gerar Treino" e veja o plano detalhado criado pela IA.

---

## Estrutura do Código

### Principais Componentes
1. **Configuração da API**:
   ```python
   api_key = os.environ.get("GOOGLE_API_KEY")
   genai.configure(api_key=api_key)
   model = genai.GenerativeModel("gemini-2.0-flash")
   ```

2. **Função para Geração de Treino**:
   ```python
   def gerar_treino(prompt):
       try:
           response = model.generate_content(prompt)
           return response.text
       except Exception as e:
           return f"Erro ao gerar treino: {str(e)}"
   ```

3. **Interface do Usuário**:
   - Entrada de dados: `st.selectbox`, `st.slider`, `st.number_input`, `st.text_area`, `st.checkbox`, `st.text_input`.
   - Botão para gerar treino: `st.button`.
   - Exibição do treino gerado: `st.write`.

4. **Prompt Engineering**:
   O prompt é montado dinamicamente com base nas entradas do usuário:
   ```python
   prompt = f"Crie um plano de treino personalizado para o objetivo '{objetivo}' com nível de dificuldade {nivel_dificuldade} " \
            f"e duração de {tempo_disponivel} minutos. Considere os seguintes equipamentos disponíveis: '{equipamentos}'. " \
            f"{f'Leve em conta a seguinte restrição física: {restricao_str}.' if restricao_fisica else ''} " \
            f"Apresente uma lista de exercícios, número de séries e repetições, e dicas para execução."
   ```

---

## Contribuição
Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Para isso:
1. Faça um fork do repositório.
2. Crie uma branch para suas alterações.
3. Envie um pull request com uma descrição detalhada das mudanças.

## Desenvolvedores
Lucas Bezerra dos Santos - 29469970
Gabriel de Almeida Mangueira - 30194903
Victor de Almeida Mangueira - 30194989
