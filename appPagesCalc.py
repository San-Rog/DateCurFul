import streamlit as st
import datetime
import time

def main():
    #Define the pages
    pages = {
    "Opções": [st.Page("contaDiasNew.py", title="Tela de entrada de dados", icon="📆"), 
              st.Page("calDaysCurrentNew.py", title="Tabelas e gráficos de dias corridos", icon="📑"), 
              st.Page("calDaysUsefulNew.py", title="Tabelas e gráficos de dias úteis", icon="📙")]   
    }
    pg = st.navigation(pages)
    pg.run()   

def supplyState():
    if 'color' not in st.session_state: 
        st.session_state.color = "#0059F9" 
    if 'colorOpt' not in st.session_state:
        st.session_state.colorOpt = '#A22845'
    if 'info' not in st.session_state: 
        now = datetime.datetime.now()
        hour = now.hour
        minutes = now.minute
        second = now.second
        st.session_state.info = {'conta': 0, 
                                'dateIni': now, 
                                'hourIni': f'{hour}h{minutes}min{second}s', 
                                'tempusIni' : time.time()}
    st.session_state.info['conta'] += 1
    
if __name__ == '__main__':
    supplyState()                   
    main()
