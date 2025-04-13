import streamlit as st
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Importações atualizadas
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI # type: ignore

import os
import yaml

# Configuração do arquivo de API
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']

# Modelo OpenAI
openai = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.7)

# Logo SVG completo
LOGO_SVG = '''
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="90" fill="#1E1E1E"/>
  <path d="M70 60 Q80 40 100 40 Q120 40 130 60 Q140 80 130 100 Q120 120 100 120 Q80 120 70 100 Q60 80 70 60" 
        fill="none" stroke="#4A90E2" stroke-width="4"/>
  <path d="M70 80 Q80 60 100 60 Q120 60 130 80 Q140 100 130 120 Q120 140 100 140 Q80 140 70 120 Q60 100 70 80" 
        fill="none" stroke="#F5A623" stroke-width="4"/>
  <circle cx="60" cy="90" r="3" fill="#4A90E2"/>
  <circle cx="140" cy="90" r="3" fill="#F5A623"/>
  <circle cx="100" cy="50" r="3" fill="#4A90E2"/>
  <circle cx="100" cy="130" r="3" fill="#F5A623"/>
  <line x1="60" y1="90" x2="80" y2="90" stroke="#4A90E2" stroke-width="2"/>
  <line x1="120" y1="90" x2="140" y2="90" stroke="#F5A623" stroke-width="2"/>
  <line x1="100" y1="50" x2="100" y2="70" stroke="#4A90E2" stroke-width="2"/>
  <line x1="100" y1="110" x2="100" y2="130" stroke="#F5A623" stroke-width="2"/>
  <text x="100" y="175" text-anchor="middle" fill="white" font-family="Arial" font-size="12">
    Psicol Agentes IA
  </text>
</svg>
'''

# Estilo personalizado para o logo e layout
st.markdown("""
    <style>
    .logo-container {
        position: fixed;
        left: 20px;
        top: 50px;
        width: 150px;  /* Aumentado de 100px para 150px */
        height: 150px; /* Aumentado de 100px para 150px */
        z-index: 999;
    }
    .logo-container svg {
        width: 100%;
        height: 100%;
    }
    .main-content {
        margin-top: 180px; /* Adicionado para evitar sobreposição com o logo */
    }
    </style>
""", unsafe_allow_html=True)

# Logo no topo
st.markdown(f"""
            
    <div class="logo-container"> {LOGO_SVG} </div>            
          
""", unsafe_allow_html=True)

# Interface Streamlit com margem superior
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.title("ChatBot: Especialista em Psicologia Clínica Avançada 🧠💬")
st.write("Digite sua pergunta ou preocupação abaixo e receba orientações de um especialista em psicologia.")

# Template para Psicologia
template = '''
Você é um especialista em psicologia com experiência em clínica avançada.
Responda à pergunta do usuário de maneira clara, empática e profissional.

Pergunta do usuário: "{pergunta}"

Certifique-se de fornecer insights baseados em psicologia e, quando apropriado, sugerir estratégias práticas para lidar com a situação. Seja empático e direto.
'''

# Configuração do Prompt Template
prompt_template = PromptTemplate.from_template(template=template)

# Entrada do usuário
user_input = st.text_area("Sua pergunta ou preocupação:", placeholder="Escreva aqui...")

# Botão de enviar
if st.button("Enviar"):
    if user_input.strip() == "":
        st.warning("Por favor, digite uma pergunta para o especialista responder.")
    else:
        # Formatar o prompt com a entrada do usuário
        prompt = prompt_template.format(pergunta=user_input)
        
        # Chamada ao modelo
        response = openai.invoke(prompt)
        
        # Exibição da resposta
        st.subheader("Resposta do Especialista:")
        st.write(response.content)

st.markdown('</div>', unsafe_allow_html=True)