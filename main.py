import gspread
from google.oauth2.service_account import Credentials
import json
import os

# ====== LOAD CREDS FROM SECRET ====== #
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

# ====== CONFIG ====== #
SPREADSHEET_ID = "1Y31SSWQ18svGk2cdTZzpVFR8kCk2yVPlGDFyVOFrAx4"
SHEET_NAME = "Sheet1"

# ====== WRITE ====== #
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
sheet.update("A1", "Hôm nay tôi buồn")

print("✅ Done")
