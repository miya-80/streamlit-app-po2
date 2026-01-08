"""
このファイルは、定数が書かれたファイルです。
"""

#######################################################
# ライブラリの読み込み
#######################################################
from pathlib import Path

#######################################################
# 1.Excel関連
#######################################################

DEFAULT_EXCEL_PATH = Path(__file__).parent / "test_file.xlsx"
EXCEL_SAMPLE_USE = "サンプルExcel（test_file.xlsx）を使用する"
EXCEL_MESSAGE = "Excelを添付後にスタートを押してください"
SHEET_INDEX = 0  # シート1（0始まり）
EXCEL_URL = "https://github.com/miya80//blob/main/test_file.xlsx?raw=true"


#######################################################
# 2.画面表示関連
#######################################################

# ボタン表示
START_BUTTON = "スタート"
SEND_BUTTON = "Amazonへ転送"
DELET_BUTTON = "セッション再起動"

# プルダウン
FIELD_CATEGORIES_NAME = "分野別カテゴリー"
FIELD_CATEGORIES = []

PRODUCT_CATEGORIES_BY_FIELD_NAME = "商品カテゴリー"
PRODUCT_CATEGORIES_BY_FIELD = {}

# 単語表示
TITLE = "Amazon商品検索自動入力ツール"
EXCEL_LOADED = "Excelの読み込みが完了しました"
EXCEL_ATTENTION = "Excelファイルを添付してください（☑を入れる）"

#######################################################
# 3.その他
#######################################################

