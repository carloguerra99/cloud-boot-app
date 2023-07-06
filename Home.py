import streamlit as st

st.title("Hello everyone!")

st.header("This is a Streamlit header!")


selected_option = st.selectbox(
    "Seleziona opzione:",
    ["Opzione 1", "Opzione 2"]
)
st.write(selected_option)


st.image("https://www.ldlc.com/it-it/scheda/PB00395869.html")