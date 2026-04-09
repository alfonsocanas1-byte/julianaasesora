import streamlit as st
import urllib.parse

# Configuración de página
st.set_page_config(
    page_title="Juliana R - Asesoría Integral",
    page_icon="🛡️",
    layout="centered"
)

# Estilos CSS optimizados para botones de enlace real
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
    /* Estilo para simular el botón de Streamlit pero que sea un enlace real */
    .whatsapp-button {
        display: block;
        width: 100%;
        padding: 15px;
        background-color: #25d366;
        color: white !important;
        text-align: center;
        text-decoration: none;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: 0.3s;
        margin-top: 10px;
        border: none;
    }
    .whatsapp-button:hover {
        background-color: #128c7e;
        transform: scale(1.02);
        text-decoration: none;
    }
    .service-container {
        background: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        border-left: 5px solid #1e3a8a;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

def link_whatsapp(mensaje):
    phone = "573015492898" 
    encoded_msg = urllib.parse.quote(mensaje)
    return f"https://wa.me/{phone}?text={encoded_msg}"

# --- SECCIÓN SUPERIOR ---
col_img_1, col_img_2, col_img_3 = st.columns([1, 2, 1])
with col_img_2:
    # Usamos el nombre exacto de tu archivo adjunto
    st.image("pelirojita1.jpg.jpeg", use_container_width=True)

st.markdown("<h1 class='main-title'>Juliana R</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='sub-title'>Asesora seguros de vida y medicina prepagada</h4>", unsafe_allow_html=True)
st.divider()

# --- BLOQUE DE SERVICIOS CON BOTONES HTML ---

# Servicio 1
with st.container():
    st.markdown("""<div class="service-container">
        <h3>🏥 Medicina Prepagada</h3>
        <p>Afiliación a Colsanitas, Sura y otros prestadores líderes.</p>
    </div>""", unsafe_allow_html=True)
    msg1 = "Soy Alfonso, solicito información de afiliación a medicina prepagada (Colsanitas, Sura, otros)"
    st.markdown(f'<a href="{link_whatsapp(msg1)}" target="_blank" class="whatsapp-button">Recibir asesoría</a>', unsafe_allow_html=True)

st.write("") # Espaciador

# Servicio 2
with st.container():
    st.markdown("""<div class="service-container">
        <h3>📋 Seguros y Pensiones</h3>
        <p>Protección para tu futuro y el de tu familia con asesoría integral.</p>
    </div>""", unsafe_allow_html=True)
    msg2 = "Soy Alfonso, solicito información de Asesoría de seguros y pensiones"
    st.markdown(f'<a href="{link_whatsapp(msg2)}" target="_blank" class="whatsapp-button">Recibir asesoría</a>', unsafe_allow_html=True)

st.write("") # Espaciador

# Servicio 3
with st.container():
    st.markdown("""<div class="service-container">
        <h3>📑 Certificaciones Z</h3>
        <p>Gestión ágil de certificaciones de la empresa medicina prepagada Z.</p>
    </div>""", unsafe_allow_html=True)
    msg3 = "Soy Alfonso, solicito información de Certificaciones de la empresa medicina prepagada Z"
    st.markdown(f'<a href="{link_whatsapp(msg3)}" target="_blank" class="whatsapp-button">Recibir asesoría</a>', unsafe_allow_html=True)