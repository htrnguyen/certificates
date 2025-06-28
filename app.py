import gspread
from jinja2 import Template
from oauth2client.service_account import ServiceAccountCredentials

# Setup Google Sheets API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Connect to Google Sheets and get data
sheet = client.open("My Certificates").sheet1
data = sheet.get_all_records()

# Reverse data to show the latest certificate first
data.reverse()

# Render HTML template
with open("templates/index.html") as file_:
    template = Template(file_.read())
    rendered_html = template.render(data=data)

# Save rendered HTML to index.html
with open("index.html", "w") as f:
    f.write(rendered_html)
