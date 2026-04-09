import streamlit as st
import urllib.parse

# Configuración de página
st.set_page_config(
    page_title="Juliana R - Asesoría Integral",
    page_icon="🛡️",
    layout="centered"
)

# Estilos CSS optimizados
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
        margin-bottom: 10px;
        border-left: 5px solid #1e3a8a;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

def link_whatsapp(nombre, servicio):
    phone = "573015492898"
    # Si el nombre está vacío, usamos un genérico para no romper el mensaje
    user_name = nombre if nombre else "un cliente"
    mensaje = f"Hola Juliana, soy {user_name}. Solicito información de: {servicio}"
    encoded_msg = urllib.parse.quote(mensaje)
    return f"https://wa.me/{phone}?text={encoded_msg}"

# --- SECCIÓN SUPERIOR ---
col_img_1, col_img_2, col_img_3 = st.columns([1, 2, 1])
with col_img_2:
    st.image("pelirojita1.jpg.jpeg", use_container_width=True)

st.markdown("<h1 class='main-title'>Juliana R</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='sub-title'>Asesora seguros de vida y medicina prepagada</h4>", unsafe_allow_html=True)
st.divider()

# --- INPUT DE NOMBRE ---
st.markdown("### 👤 Déjanos tu nombre")
nombre_usuario = st.text_input("Escribe tu nombre completo para personalizar tu asesoría:", placeholder="Ej: Alfonso Pérez")

st.write("") 

# --- BLOQUE DE SERVICIOS ---

# Servicio 1
with st.container():
    st.markdown("""<div class="service-container">
        <h3>🏥 Medicina Prepagada</h3>
        <p>Afiliación a Colsanitas, Sura y otros prestadores líderes.</p>
    </div>""", unsafe_allow_html=True)
    svc1 = "Afiliación a medicina prepagada (Colsanitas, Sura, otros)"
    st.markdown(f'<a href="{link_whatsapp(nombre_usuario, svc1)}" target="_blank" class="whatsapp-button">Recibir asesoría</a>', unsafe_allow_html=True)

st.write("") 

# Servicio 2
with st.container():
    st.markdown("""<div class="service-container">
        <h3>📋 Seguros y Pensiones</h3>
        <p>Protección para tu futuro y el de tu familia con asesoría integral.</p>
    </div>""", unsafe_allow_html=True)
    svc2 = "Asesoría de seguros y pensiones"
    st.markdown(f'<a href="{link_whatsapp(nombre_usuario, svc2)}" target="_blank" class="whatsapp-button">Recibir asesoría</a>', unsafe_allow_html=True)

st.write("") 

# Servicio 3
with st.container():
    st.markdown("""<div class="service-container">
        <h3>📑 Certificaciones Z</h3>
        <p>Gestión ágil de certificaciones de la empresa medicina prepagada Z.</p>
    </div>""", unsafe_allow_html=True)
    svc3 = "Certificaciones de la empresa medicina prepagada Z"
    st.markdown(f'<a href="{link_whatsapp(nombre_usuario, svc3)}" target="_blank" class="whatsapp-button">Recibir asesoría</a>', unsafe_allow_html=True)