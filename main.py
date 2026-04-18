import gspread
from google.oauth2.service_account import Credentials
import json
import os
from datetime import datetime

# ====== CONFIG ====== #
SPREADSHEET_ID = "1Y31SSWQ18svGk2cdTZzpVFR8kCk2yVPlGDFyVOFrAx4"
SHEET_NAME = "Sheet1"

# ====== AUTH ====== #
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

# ====== OPEN SHEET ====== #
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

# ====== DATA MẪU (bạn thay bằng API sau) ====== #
data_input = [
    {"id": "A001", "message": "Hôm nay tôi buồn"},
    {"id": "A002", "message": "Hôm nay tôi vui"},
]

# ====== LẤY ID ĐÃ CÓ (tránh trùng) ====== #
try:
    existing_ids = sheet.col_values(1)  # cột A = ID
except:
    existing_ids = []

existing_ids = set(existing_ids)

# ====== CHUẨN BỊ DATA GHI ====== #
rows_to_append = []

for item in data_input:
    if item["id"] in existing_ids:
        continue

    rows_to_append.append([
        item["id"],
        item["message"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])

# ====== GHI ====== #
if rows_to_append:
    sheet.append_rows(rows_to_append)
    print(f"✅ Đã ghi {len(rows_to_append)} dòng")
else:
    print("⚠️ Không có dữ liệu mới (tránh trùng)")
