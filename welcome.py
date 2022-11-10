import streamlit as st

def bienvenida(nombre):
    mymsensaje= 'bienvenido/a :'+nombre
    return mymsensaje

myname=st.text_input('nombre :')
if (myname):
    mensaje=bienvenida(myname)
    st.write(f" mensaje : {myname}")