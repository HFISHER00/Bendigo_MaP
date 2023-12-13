import streamlit as st

APP_TITLE = "Interactive Map of Bendigo Transmission Lines"
APP_SUB_TITLE = "Source: CSIRO"

def main():
    st.set_page_config(page_title=APP_TITLE, page_icon=":earth_americas:")
    st.title(APP_TITLE)
    st.write(APP_SUB_TITLE)

if __name__ == "__main__":
    main()
