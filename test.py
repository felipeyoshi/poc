import streamlit as st
from audiorecorder import audiorecorder
from utils.aai_utils import TranscriberTest
from utils.openai_utils import LLM
from prompts.testes import PROMPT_TESTE_MAPA

# Initialize session state
if 'text' not in st.session_state:
    st.session_state.text = ''

if 'text_edited' not in st.session_state:
    st.session_state.text_edited = ''

if 'prompt_edited' not in st.session_state:
    st.session_state.prompt_edited = ''

# Setup keys
aai_key = st.secrets["secrets"]["AAI_KEY"]
openai_key = st.secrets["secrets"]["OPENAI_KEY"]

#Streamlit app
st.title('Teste: <nome do teste>')
st.markdown('### O que você vê na foto abaixo?')
st.write('Instruções para o teste: aperte o botão "Gravar" para iniciar a gravação. Ao final, aperte o mesmo botão para enviar a sua resposta.')
st.image('mapa_brasil.jpg')

audio = audiorecorder("Gravar", "Finalizar gravação")

if len(audio) > 0 and st.session_state.text == '':
    wav_file = open("audio.wav", "wb") 
    wav_file.write(audio.tobytes())
    transcriber = TranscriberTest(aai_key)
    st.session_state.text = transcriber.transcribe_audio("audio.wav")

st.session_state.text_edited = st.text_area('Editar a transcrição:', st.session_state.text, height=150)

if st.button('Enviar!'):
    st.text('Sua resposta foi enviada!')
    prompt_map_test = PROMPT_TESTE_MAPA.format(st.session_state.text_edited) 
    #st.session_state.prompt_edited = st.text_area('Prompt:', prompt_map_test, height=300)
    agent = "Você é um especialista em cognição social."
    llm = LLM(openai_key)
    message = llm.get_prompt(agent, prompt_map_test)
    result_map_test = llm.get_completion(message)
    st.components.v1.html(result_map_test, height=500, scrolling=True)
