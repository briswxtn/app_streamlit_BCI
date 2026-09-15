import streamlit as st

st.title("Mi aplicación Programación")
st.button("hacer click aquí")
st.balloons()

st.title("Clasificador de temperatura")
temperatura = st.number_input(
  "Introduce la temperatura en °C:",
  value=20
)
if temperatura<20:
  st.writte("hace frío")
elif temperatura<30:
  st.writte("la temperatura es agradable")
else:
 st.writte("hace calor") 
  )

 st.title("Control de acceso")

