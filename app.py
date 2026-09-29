import datetime
import streamlit as st

st.set_page_config(
    page_title="Un detalle para ti ❤️", page_icon="💖", layout="centered"
)

st.title("💖 Un detalle especial para ti")
st.write(
    "¡Hola, Amor! Creé este pequeño programa solo para ti, para recordarte lo mucho que te amo."
)

st.divider()

# Contador de días
fecha_inicio = datetime.date(2024, 05, 27)  
dias_juntos = (datetime.date.today() - fecha_inicio).days
st.metric(
    label="Días compartiendo momentos juntos 🗓️", value=f"{dias_juntos} días"
)

st.divider()

# Botón interactivo
st.subheader("🎁 Una sorpresa para ti")
if st.button("Haz clic aquí para abrir"):
    st.balloons()
    st.success("Gracias por estar en mi vida❤️")
