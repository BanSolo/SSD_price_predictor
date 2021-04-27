# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:23:03 2021

@author: user
"""

import pandas as pd
import streamlit as st
import pickle
import sklearn

def main():
    
    #f = open(r'C:\Projects\SSD_price_predictor\finalized_model.sav', 'rb')
    model = pickle.load(open('finalized_model.sav', 'rb'))
    #result = loaded_model.score(X_test, Y_test)
    sc_X = pickle.load(open(r'sc_X.sav', 'rb'))
    sc_y = pickle.load(open(r'sc_y.sav', 'rb'))
    #print(sc_y.inverse_transform([[-0.51533502]]))    
    
    
    #df = pd.read_csv(r'C:\Projects\SSD_price_predictor\ssd2.csv')
    size = st.sidebar.selectbox('Méret', ["Homepage", "Exploration"])
    connection = st.sidebar.selectbox('Csatlakozás', ["123", "refre"])
    tech = st.sidebar.selectbox('Technológia', ["dsadad", "54tgerg"])
    capacity = st.sidebar.slider('Tároló kapacitás (GB)', min_value=120, max_value=4000, 
                      step=10)
    writing = st.sidebar.slider('SSD max írás (MB/s)', min_value=300, max_value=6000, 
                      step=10)
    reading = st.sidebar.slider('SSD max olvasás (MB/s)', min_value=300, max_value=9000, 
                      step=10)
    tbw = st.sidebar.slider('TBW (TB)', min_value=0, max_value=3000, step=10)
    lights = st.sidebar.selectbox('Világítás', ['Nem', 'Igen'])
    cooling = st.sidebar.selectbox('Hűtőborda', ['Nem', 'Igen'])
    button = st.sidebar.button('Becslés')
    
    st.header('SSD ár becslő alkalmazás')
    st.image('https://gamespot1.cbsistatic.com/uploads/original/1568/15683559/3224016-intel-optane-memory-review%20conclusion.jpg')
    st.write('Tároló kapacitás ', capacity, ' GB')
    st.write(reading)
    st.write(sc_y.inverse_transform([[-0.51533502]]))
    
    if button == True:
        st.write('§§§§§§§§§§§§')
    
    if size == "Homepage":
        st.header("This is your data explorer.")
        st.write("Please select a page on the left.")
        #st.write(df)
    elif size == "Exploration":
        pass





if __name__ == "__main__":
    main()










