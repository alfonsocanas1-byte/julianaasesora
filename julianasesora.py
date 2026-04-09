import streamlit as st
import urllib.parse

# Configuración de página para producción
st.set_page_config(
    page_title="Juliana R - Asesoría Integral",
    page_icon="🛡️",
    layout="centered"
)

# Estilos personalizados para mejorar la estética
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .main-title {
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #4b5563;
        text-align: center;
        margin-bottom: 20px;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #25d366;
        color: white;
        font-weight: bold;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #128c7e;
        color: white;
    }
    .service-card {
        padding: 15px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def enviar_whatsapp(mensaje):
    # Número de Juliana (Formato internacional sin el +)
    phone = "573000000000" 
    base_url = "https://wa.me/"
    encoded_msg = urllib.parse.quote(mensaje)
    return f"{base_url}{phone}?text={encoded_msg}"

# --- SECCIÓN SUPERIOR ---
# Imagen central superior (pelirojita1.jpg)
col_img_1, col_img_2, col_img_3 = st.columns([1, 2, 1])
with col_img_2:
    st.image("pelirojita1.jpg.jpeg", use_container_width=True)

st.markdown("<h1 class='main-title'>Juliana R</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='sub-title'>Asesora seguros de vida y medicina prepagada</h4>", unsafe_allow_html=True)

st.divider()

# --- BLOQUE DE SERVICIOS ---

# Servicio 1
with st.container():
    st.markdown("### 🏥 Medicina Prepagada")
    st.write("Afiliación a medicina prepagada (Colsanitas, Sura, otros)")
    msg1 = "Soy Alfonso, solicito información de afiliación a medicina prepagada (Colsanitas, Sura, otros)"
    if st.button("Recibir asesoría", key="prep"):
        link = enviar_whatsapp(msg1)
        st.markdown(f'<a href="{link}" target="_blank">Click aquí si no redirige automáticamente</a>', unsafe_allow_html=True)
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{link}\'" />', unsafe_allow_html=True)

st.markdown("---")

# Servicio 2
with st.container():
    st.markdown("### 📋 Seguros y Pensiones")
    st.write("Asesoría integral en seguros de vida y fondos de pensión")
    msg2 = "Soy Alfonso, solicito información de Asesoría de seguros y pensiones"
    if st.button("Recibir asesoría", key="seg"):
        link = enviar_whatsapp(msg2)
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{link}\'" />', unsafe_allow_html=True)

st.markdown("---")

# Servicio 3
with st.container():
    st.markdown("### 📑 Certificaciones Z")
    st.write("Trámite de certificaciones de la empresa medicina prepagada Z")
    msg3 = "Soy Alfonso, solicito información de Certificaciones de la empresa medicina prepagada Z"
    if st.button("Recibir asesoría", key="cert"):
        link = enviar_whatsapp(msg3)
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{link}\'" />', unsafe_allow_html=True)