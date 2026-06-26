import streamlit as st
import time

st.set_page_config(page_title="Spazio Sicuro", page_icon="🤍", layout="centered")

st.title("Ciao Ang, hai bisogno di aiuto? 🤍")
st.write("Fai un respiro profondo. Sei al sicuro. Io sono qui con te. Usa i pulsanti qui sotto.")

tab1, tab2, tab3 = st.tabs(["🧘 Respiro", "🧠 Domande per Calmarti", "📞 Chiamami"])

with tab1:
    st.subheader("Respiriamo insieme")
    st.write("Segui il ritmo qui sotto per rallentare il battito del cuore")
    if st.button("Clicca qui per iniziare a respirare"):
        placeholder = st.empty()
        for i in range(3):
            placeholder.markdown("### 🧘 **INSPIRA... (1... 2... 3... 4)")
            time.sleep(4)
            placeholder.markdown("### 🛑 **TRATTIENI... (1... 2... 3... 4)")
            time.sleep(4)
            placeholder.markdown("### 💨 **ESPIRA... (1... 2... 3... 4)")
            time.sleep(4)
        placeholder.markdown("### ✨ Bravissima Angelica. Un altro respiro profondo. Va già un po' meglio?")

with tab2:
    st.subheader("Riconnettiti con la realtà")
    st.write("Rispondi a queste domande una alla volta per fermare i pensieri:")
    st.info("**1. Dove ti trovi in questo momento?** Guarda la stanza, sei in un posto sicuro.")
    st.info("**2. Cosa puoi toccare adesso?** Senti il telefono tra le mani, o i piedi appoggiati a terra.")
    st.info("**3. Cosa vedi intorno a te?** Trova 3 oggetti di colore blu o verde nella stanza.")
    st.info("**4. Ripeti a te stessa:** *'È solo un attacco di panico, passerà. Mattia è con me.'*")

with tab3:
    st.subheader("Parla con me")
    st.write("Non sei sola. Puoi chiamarmi subito.")
    st.success("📞 **Chiamami:** Fai clic sul mio numero se sei da telefono: +39 391 181 3294")

