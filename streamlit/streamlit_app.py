# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import streamlit as st
import pickle

def main():
    
    df = pd.read_csv('data/prepeared_data.csv')
    
    # onjects
    model = pickle.load(open('finalized_model.sav', 'rb'))
    sc_X = pickle.load(open(r'sc_X.sav', 'rb'))
    sc_y = pickle.load(open(r'sc_y.sav', 'rb'))
    oh_enc = pickle.load(open(r'oh_enc.sav', 'rb'))
    
    # main
    st.header('SSD ár becslő alkalmazás')
    st.image('https://gamespot1.cbsistatic.com/uploads/original/1568/15683559/3224016-intel-optane-memory-review%20conclusion.jpg')
    st.write('Az előkészített adathalmaz a modell számára')
    st.write(df)
    
    # sidebar
    st.sidebar.header('Paraméterek')
    size = st.sidebar.selectbox('Méret', df['Méret'].unique())
    connection = st.sidebar.selectbox('Csatlakozás', df['Csatlakozás'].unique())
    tech = st.sidebar.selectbox('Technológia', df['Technológia'].unique())
    capacity = st.sidebar.slider('Tároló kapacitás (GB)', min_value=120, 
                                 max_value=3000, step=10)
    writing = st.sidebar.slider('SSD max írás (MB/s)', min_value=300, 
                                max_value=4000, step=10)
    reading = st.sidebar.slider('SSD max olvasás (MB/s)', min_value=300, 
                                max_value=7000, step=10)
    lights = st.sidebar.selectbox('Világítás', df['Világítás'].unique())
    cooling = st.sidebar.selectbox('Hűtőborda', df['Hűtőborda'].unique())
    button = st.sidebar.button('Becslés')
    
    num_values = sc_X.transform([[capacity, writing, reading]])
    cat_values = oh_enc.transform(np.array([size, connection, tech, lights, 
                                            cooling]).reshape(-1, 5))
    
    array = []
    for i in num_values:
        for j in i:
            array.append(j)
    for i in cat_values:
        for j in i:
            array.append(j)
    
    if button:
        st.write('Az SSD várható ára: ', round(sc_y.inverse_transform(
            model.predict([array]))[0][0]), ' Ft')
        st.write('A következő tulajdonságok alapján:')
        st.write('Méret: ', size)
        st.write('Csatlakozás: ', connection)
        st.write('Technológia: ', tech)
        st.write('Tároló kapacitás: ', capacity, ' GB')
        st.write('SSD max írás: ', writing, ' MB/s')
        st.write('SSD max olvasás: ', reading, ' MB/s')
        st.write('Világítás: ', lights)
        st.write('Hűtőborda: ', cooling)
    

if __name__ == "__main__":
    main()



