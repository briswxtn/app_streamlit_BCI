import streamlit as st

st.title("Mi aplicación Programación")
st.button("hacer click aquí")
st.balloons()
st.title("Clasificador de temperatura")
temperatura = st.number_input(
  "Introduce la temperatura en °C:",
  value=20
)
st.writte:

if temperatura<20:
  print("hace frío")
elif temperatura<30:
  print("la temperatura es agradable")
else:
  print("hace calor")
  
