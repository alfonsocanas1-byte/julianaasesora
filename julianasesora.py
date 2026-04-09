import streamlit as st
import urllib.parse

# Configuración de página para producción
st.set_page_config(
    page_title="Juliana R - Asesoría Integral",
    page_icon="🛡️",
    layout="centered"
)

# Estilos personalizados para máxima conversión en móviles
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .main-title {
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 0px;
        font-weight: bold;
    }
    .sub-title {
        color: #4b5563;
        text-align: center;
        margin-bottom: 20px;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #25d366;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #128c7e;
        color: white;
        transform: scale(1.02);
    }
    .service-container {
        background: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        border-left: 5px solid #1e3a8a;
    }
    </style>
    """, unsafe_allow_html=True)

def enviar_whatsapp(mensaje):
    # Número actualizado de Juliana 
    phone = "573015492898" 
    base_url = "https://wa.me/"
    encoded_msg = urllib.parse.quote(mensaje)
    return f"{base_url}{phone}?text={encoded_msg}"

# --- SECCIÓN SUPERIOR ---
# Imagen central superior basada en el archivo adjunto 
col_img_1, col_img_2, col_img_3 = st.columns([1, 2, 1])
with col_img_2:
    st.image("pelirojita1.jpg.jpeg", use_container_width=True)

st.markdown("<h1 class='main-title'>Juliana R</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='sub-title'>Asesora seguros de vida y medicina prepagada</h4>", unsafe_allow_html=True)

st.divider()

# --- BLOQUE DE SERVICIOS ---

# Servicio 1: Medicina Prepagada
with st.container():
    st.markdown("### 🏥 Medicina Prepagada")
    st.write("Afiliación a Colsanitas, Sura y otros prestadores líderes.")
    msg1 = "Soy Alfonso, solicito información de afiliación a medicina prepagada (Colsanitas, Sura, otros)"
    if st.button("Recibir asesoría", key="prep"):
        link = enviar_whatsapp(msg1)
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{link}\'" />', unsafe_allow_html=True)
        st.js_code(f"window.open('{link}', '_blank').focus();")

# Servicio 2: Seguros y Pensiones
with st.container():
    st.markdown("### 📋 Seguros y Pensiones")
    st.write("Protección para tu futuro y el de tu familia con asesoría integral.")
    msg2 = "Soy Alfonso, solicito información de Asesoría de seguros y pensiones"
    if st.button("Recibir asesoría ", key="seg"):
        link = enviar_whatsapp(msg2)
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{link}\'" />', unsafe_allow_html=True)

# Servicio 3: Certificaciones Z
with st.container():
    st.markdown("### 📑 Certificaciones Z")
    st.write("Gestión ágil de certificaciones de la empresa medicina prepagada Z.")
    msg3 = "Soy Alfonso, solicito información de Certificaciones de la empresa medicina prepagada Z"
    if st.button("Recibir asesoría  ", key="cert"):
        link = enviar_whatsapp(msg3)
        st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{link}\'" />', unsafe_allow_html=True)