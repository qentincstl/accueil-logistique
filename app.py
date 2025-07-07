import streamlit as st
# Vérification de mot de passe simple
def check_password():
    def password_entered():
        if st.session_state["password"] == "tonmotdepasse123":
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("🔐 Mot de passe :", type="password", on_change=password_entered, key="password")
        st.stop()
    elif not st.session_state["password_correct"]:
        st.text_input("🔐 Mot de passe :", type="password", on_change=password_entered, key="password")
        st.error("Mot de passe incorrect.")
        st.stop()

check_password()

st.set_page_config(page_title="Accueil logistique", layout="wide")

# URLs des autres pages à ouvrir dans un nouvel onglet :
url_bl = "https://app-bon-livraison3-ncfb7urzyr7e3p5cwohdsk.streamlit.app/"      # Remplace ici par la vraie URL de la page "Bon de livraison"
url_qte = "https://app-quantites-recues-c8olmzeaxjq7helzmh7qyc.streamlit.app/"

st.markdown("""
<style>
    body { background: #f7fafd; }
    .container-choice {
        display: flex; gap: 3.5rem; justify-content: center; align-items:center; margin-top:4.5rem;
    }
    .bigcard {
        width: 370px; min-height: 260px; background: #fff; border-radius: 1.2rem;
        box-shadow: 0 4px 18px #0002; padding:2.5rem 2rem;
        cursor:pointer; text-align:center; transition:.19s;
        border:2.5px solid #fff; position:relative;
        display:flex; flex-direction:column; align-items:center; justify-content:center;
    }
    .bigcard:hover {
        border:2.5px solid #3897f033;
        box-shadow: 0 7px 28px #257ee12b;
        transform: translateY(-7px) scale(1.04);
    }
    .bigicon { font-size:3.1rem; margin-bottom:1.6rem;}
    .title { font-size:1.45rem; font-weight:700; color:#133a5a;}
    .subtitle { font-size:1.07rem; color:#516080; margin-top:.75rem;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#202944; margin-top:2rem; margin-bottom:2.4rem;">Accueil plateforme logistique</h1>', unsafe_allow_html=True)

# Cards côte à côte au centre
st.markdown(f"""
<div class="container-choice">
    <a href="{url_bl}" target="_blank" style="text-decoration:none;">
        <div class="bigcard">
            <div class="bigicon">📦</div>
            <div class="title">Bon de livraison</div>
            <div class="subtitle">Déposer un bon de livraison<br>et extraire les produits reçus.</div>
        </div>
    </a>
    <a href="{url_qte}" target="_blank" style="text-decoration:none;">
        <div class="bigcard">
            <div class="bigicon">✅</div>
            <div class="title">Quantités réellement reçues</div>
            <div class="subtitle">Saisir à la main les quantités<br>réellement réceptionnées.</div>
        </div>
    </a>
</div>
""", unsafe_allow_html=True)
