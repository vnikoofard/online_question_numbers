import pandas as pd
import numpy as np
import streamlit as st
from streamlit import caching
import numpy as np
import shutil
import math


def check_matricula(num):
    if int(num) in df['Matricula'].tolist():
        return True
    else:
        st.write('A sua matricula não está correta')
        return False
def get_name(matricula):
    name = df[df['Matricula']==int(matricula)]['Nome'].iloc[0]
    return name




st.set_option('deprecation.showfileUploaderEncoding', False)

df = pd.read_csv('alunos_matriculados.csv')


#Initialization
st.title("Insira a sua matrícula e aperte ENTER")
#st.markdown("A extensão do arquivo deve ser `.py`, ou seja, no formato de Python puro. Para mais instruções verifiquem [YouTube](https://youtu.be/Y4IDTneyMns). ")

matricula = st.text_input('Matricula')

if matricula:
    st.write('Oi ', get_name(matricula).split()[0].title(), 'Tudo bem?')
    st.write(f"As questões para voce resolver são {df[df['Matricula']==int(matricula)]['lista_4 exercicios'].iloc[0]}")





            







