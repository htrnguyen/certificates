import os

import gspread
from jinja2 import Template
from oauth2client.service_account import ServiceAccountCredentials

# Setup Google Sheets API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

try:
    # Check if credentials file exists
    if os.path.exists("credentials.json"):
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "credentials.json", scope
        )
        client = gspread.authorize(creds)

        # Connect to Google Sheets and get data
        sheet = client.open("My Certificates").sheet1
        data = sheet.get_all_records()

        # Reverse data to show the latest certificate first
        data.reverse()

        print(f"Successfully fetched {len(data)} certificates from Google Sheets")
    else:
        print("No credentials.json found, using empty data")
        data = []

except Exception as e:
    print(f"Error fetching data from Google Sheets: {e}")
    print("Using empty data as fallback")
    data = []

# Ensure data is not None
if data is None:
    data = []

# Render HTML template
try:
    with open("templates/index.html", "r", encoding="utf-8") as file_:
        template = Template(file_.read())
        rendered_html = template.render(data=data)

    # Save rendered HTML to index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print(f"Successfully created index.html with {len(data)} certificates")

except Exception as e:
    print(f"Error creating index.html: {e}")
    # Create a basic fallback HTML if template fails
    fallback_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ha Trong Nguyen | Professional Certificates</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>Ha Trong Nguyen</h1>
    <h2>Professional Certificates Portfolio</h2>
    <p class="error">Unable to load certificates at this time.</p>
    <p>Please check back later or contact the administrator.</p>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(fallback_html)

    print("Created fallback index.html due to template error")
