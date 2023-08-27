import streamlit as st
from audiorecorder import audiorecorder
from aai_utils import TranscriberTest

text = ''

#Streamlit app
st.title('Teste: <nome do teste>')
st.markdown('### O que você vê na foto abaixo?')
st.write('Instruções para o teste: aperte o botão "Gravar" para iniciar a gravação. Ao final, aperte o mesmo botão para enviar a sua resposta.')
st.image('mapa_brasil.jpg')

audio = audiorecorder("Gravar", "Gravando...")

if len(audio) > 0:
    wav_file = open("audio.wav", "wb") 
    wav_file.write(audio.tobytes())
    
    transcriber = TranscriberTest("47681e919af44ce5ae685f12b2bae0b7")
    text = transcriber.transcribe_audio("audio.wav")

st.text_area('Editar a transcrição:', text)