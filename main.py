import gspread
from google.oauth2.service_account import Credentials
import json
import os

creds = Credentials.from_service_account_info(
    json.loads(os.environ["GOOGLE_CREDENTIALS"]),
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"]
)

client = gspread.authorize(creds)

sheet = client.open_by_key("1Y31SSWQ18svGk2cdTZzpVFR8kCk2yVPlGDFyVOFrAx4").worksheet("Sheet1")

sheet.update_acell("A1", "RUN OK 123"))

print("DONE")
