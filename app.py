import streamlit as st
import joblib
from translations import ui_text, LANGS
from ui_utils import login_page, stroke_prediction_app

VALID_USERNAME = "user"
VALID_PASSWORD = "pass"

@st.cache_resource
def load_model():
    return joblib.load('stroke_model.pkl')

def main():
    st.set_page_config(layout="centered")
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    lang = st.sidebar.selectbox("🌐 Select Language / ಭಾಷೆ / ഭാഷ", LANGS,
                               index=LANGS.index(st.session_state.get("selected_language", LANGS[0])))
    st.session_state.selected_language = lang

    t = ui_text[lang]
    model = load_model()

    login_page(t, VALID_USERNAME, VALID_PASSWORD)
    if st.session_state.logged_in:
        stroke_prediction_app(t, model, lang)

if __name__ == "__main__":
    main()
