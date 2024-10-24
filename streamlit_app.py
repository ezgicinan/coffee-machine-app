import streamlit as st
from resources import Resources

if "resources_instance" not in st.session_state:
  st.session_state.resources_instance = Resources()


resources = Resources()
st.title("🎈Coffee Machine ☕")
st.write("Resources:")
st.write(st.session_state.resources_instance)
