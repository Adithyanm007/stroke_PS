import streamlit as st
import joblib
from translations import ui_text, LANGS
from ui_utils import login_page, stroke_prediction_app

VALID_USERNAME = "user"
VALID_PASSWORD = "pass"
MODEL_PATH = "stroke_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

def main():
    st.set_page_config(layout="centered")
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "rerun_flag" not in st.session_state:
        st.session_state.rerun_flag = False

    lang = st.sidebar.selectbox("🌐 Select Language / ಭಾಷೆ / മലയാളം", LANGS,
        index=LANGS.index(st.session_state.get("selected_language", LANGS[0])))
    st.session_state.selected_language = lang

    t = ui_text[lang]
    model = load_model()

    # Hidden input just to force rerun by its value changing
    rerun_trigger = st.checkbox("trigger rerun", value=st.session_state.rerun_flag, key='dummy_rerun', help="hidden", label_visibility="collapsed")

    # Rerun logic
    login_success = login_page(t, VALID_USERNAME, VALID_PASSWORD)
    if login_success:
        st.session_state.logged_in = True
        # Flip rerun_flag to trigger a rerun via the dummy widget
        st.session_state.rerun_flag = not st.session_state.rerun_flag
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else None  # works if available!

    if st.session_state.logged_in:
        stroke_prediction_app(t, model, lang)

if __name__ == "__main__":
    main()
