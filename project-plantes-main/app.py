from collections import OrderedDict

import streamlit as st

from streamlit_app import config

from streamlit_app.tabs import intro, second_tab, third_tab, fourth_tab


st.set_page_config(
    page_title=config.TITLE,
    page_icon="https://publithings.com/wp-content/uploads/2021/03/logo_data_scientest.png",
)

with open("streamlit_app/style.css", "r") as f:
    style = f.read()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)

TABS = OrderedDict(
    [
        (intro.sidebar_name, intro),
        (second_tab.sidebar_name, second_tab),
        (third_tab.sidebar_name, third_tab),
        (fourth_tab.sidebar_name, fourth_tab),
    ]
)

def run():
    st.sidebar.image(
        "https://publithings.com/wp-content/uploads/2021/03/logo_data_scientest.png",
        width=200,
    )
    tab_name = st.sidebar.radio("", list(TABS.keys()), 0)
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"## {config.PROMOTION}")

    st.sidebar.markdown("### Equipe projet :")

    for member in config.TEAM_MEMBERS:
        st.sidebar.markdown(member.sidebar_markdown(), unsafe_allow_html=True)

    tab = TABS[tab_name]

    st.sidebar.markdown("### Datasets utilisés :")
    st.sidebar.markdown(f"{config.DATASET1}")
    st.sidebar.markdown(f"{config.DATASET2}")

    tab.run()


if __name__ == "__main__":
    run()
