import gspread
from google.oauth2.service_account import Credentials
import json
import os

# ===== AUTH =====
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

# ===== OPEN SHEET =====
sheet = client.open_by_key("1Y31SSWQ18svGk2cdTZzpVFR8kCk2yVPlGDFyVOFrAx4").worksheet("Sheet1")

# ===== WRITE =====
sheet.update_acell("A1", "OK RUN DUOC")

print("✅ DONE")
