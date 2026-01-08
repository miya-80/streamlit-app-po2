"""
このファイルは、メインの実行プログラムが書かれたファイルです。
"""

#######################################################
# ライブラリの読み込み
#######################################################
import pandas as pd
import openpyxl
import constants as ct
import streamlit as st
import urllib.parse
import webbrowser
import unit as ut
from io import BytesIO

#######################################################
# メイン処理
#######################################################

st.title(ct.TITLE)
st.markdown(
    "<span style='color: red;'>公開用のため、テストサンプルのみでの動作します</span>",
    unsafe_allow_html=True
)

# =========================
# 初期化
# =========================

ut.initialize()

# =========================
# テストファイルを添付（常に表示）
# =========================

use_sample = st.checkbox(ct.EXCEL_SAMPLE_USE)


# =========================
# ボタン（常に表示）
# =========================
col1, col2, col3, col4 = st.columns(4)

with col1:
    start_clicked = st.button(ct.START_BUTTON)

with col2:
    transfer_clicked = st.button(ct.SEND_BUTTON)

with col3:
    delete_all_session = st.button(ct.DELET_BUTTON)

with col4:
    open_session_clicked = st.button(ct.EXCEL_BUTTON)


#######################################################
# 1.Excel読み込み
#######################################################
# =========================
# セッション再起動
# =========================
if delete_all_session:
    ut.all_session_delete()


# =========================
# スタート押下後に処理開始
# =========================
if  start_clicked and use_sample:
    # アップロードされたExcelを直接読み込む
    wb = openpyxl.load_workbook(ct.DEFAULT_EXCEL_PATH)
    ws = wb.worksheets[ct.SHEET_INDEX]

    current_field = None

    # 重複防止のため初期化
    ct.FIELD_CATEGORIES.clear()
    ct.PRODUCT_CATEGORIES_BY_FIELD.clear()

    for row in ws.iter_rows(min_col=1, max_col=1):
        value = row[0].value

        if value is None:
            continue

        text = str(value).strip()

        # ■ 分野カテゴリー
        if text.startswith("■"):
            current_field = text.replace("■", "").strip()
            ct.FIELD_CATEGORIES.append(current_field)
            ct.PRODUCT_CATEGORIES_BY_FIELD[current_field] = []

        # ・ 商品カテゴリー
        elif text.startswith("・") and current_field is not None:
            product = text.replace("・", "").strip()
            ct.PRODUCT_CATEGORIES_BY_FIELD[current_field].append(product)

    # session_stateに保存
    st.session_state.FIELD_CATEGORIES = ct.FIELD_CATEGORIES
    st.session_state.PRODUCT_CATEGORIES_BY_FIELD = ct.PRODUCT_CATEGORIES_BY_FIELD
    st.session_state.loaded = True

    st.session_state.excel_loaded_message = True

elif start_clicked and not use_sample:
    st.warning(ct.EXCEL_ATTENTION)

elif transfer_clicked and not use_sample:
    st.warning(ct.EXCEL_ATTENTION)

if st.session_state.get("excel_loaded_message", False) and use_sample:
        st.success(ct.EXCEL_LOADED)

if open_session_clicked:
    df = pd.read_excel(ct.DEFAULT_EXCEL_PATH, engine='openpyxl')
    # DataFrameの内容を画面に表示 
    st.dataframe(df)
   
    # =========================
# プルダウン（常に表示）
# =========================
if st.session_state.loaded:

    selected_field = st.selectbox(
        ct.FIELD_CATEGORIES_NAME,
        st.session_state.FIELD_CATEGORIES,
        key="selected_field"
    )

    selected_product = st.selectbox(
        ct.PRODUCT_CATEGORIES_BY_FIELD_NAME,
        st.session_state.PRODUCT_CATEGORIES_BY_FIELD.get(selected_field, []),
        key="selected_product"
    )


    # =========================
    # 選択結果表示
    # =========================
    st.write(f"{ct.FIELD_CATEGORIES_NAME}：", selected_field)
    st.write(f"{ct.PRODUCT_CATEGORIES_BY_FIELD_NAME}：", selected_product, "（転送ボタン押下でAmazonの検索欄に自動入力）")


    # =========================
    # Amazonへ転送ボタン
    # =========================
    
    if transfer_clicked and use_sample:

        # 分野別カテゴリーを検索ワードに使用
        query = urllib.parse.quote(selected_product)
        amazon_url = f"https://www.amazon.co.jp/s?k={query}"
        webbrowser.open(amazon_url)
        

