"""
このファイルは、画面表示系のプログラムが書かれたファイルです。
"""

#######################################################
# ライブラリの読み込み
#######################################################
import streamlit as st
import constants as ct


#######################################################
# 1.初期化
#######################################################
def initialize():
    if "loaded" not in st.session_state:
        st.session_state["loaded"] = False

    if "FIELD_CATEGORIES" not in st.session_state:
        st.session_state["FIELD_CATEGORIES"] = []

    if "PRODUCT_CATEGORIES_BY_FIELD" not in st.session_state:
        st.session_state["PRODUCT_CATEGORIES_BY_FIELD"] = {}
    

# =========================
# セッション再起動
# =========================
def all_session_delete():
    st.session_state.clear()
    st.rerun()