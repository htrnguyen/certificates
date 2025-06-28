# 🎓 Professional Certificates Portfolio

A beautiful, responsive portfolio website showcasing professional certificates with both grid and timeline views.

## ✨ Features

-   **Dual View Modes**: Switch between Grid and Timeline views
-   **Auto Data Sync**: Automatically fetches data from Google Sheets
-   **Search & Filter**: Find certificates by name or platform
-   **Dark Mode**: Toggle between light and dark themes
-   **Responsive Design**: Works perfectly on all devices
-   **Auto Deploy**: Updates daily via GitHub Actions

## 🚀 Live Demo

Visit: [Your GitHub Pages URL] (will be available after setup)

## 📋 Setup Instructions

### 1. Repository Setup

1. **Fork or Clone** this repository
2. **Enable GitHub Pages**:
    - Go to Settings → Pages
    - Source: Deploy from a branch
    - Branch: `gh-pages` (will be created by workflow)
    - Save

### 2. Google Sheets Setup

1. **Create Google Sheet** with columns:

    - `Certificate Name`
    - `Certificate Type` (Platform name)
    - `Date Issued`
    - `URL`

2. **Setup Google Service Account**:

    - Go to [Google Cloud Console](https://console.cloud.google.com/)
    - Create new project or select existing
    - Enable Google Sheets API
    - Create Service Account
    - Download JSON credentials

3. **Add Repository Secrets**:
    - Go to Settings → Secrets and variables → Actions
    - Add secret: `GOOGLE_CREDENTIALS`
    - Value: Content of your JSON credentials file

### 3. Update Configuration

Edit `app.py`:

```python
# Update sheet name
sheet = client.open("YOUR_SHEET_NAME").sheet1
```

### 4. Deploy

1. **Push to main branch** - triggers automatic deployment
2. **Manual trigger** - Go to Actions → Deploy to GitHub Pages → Run workflow

## 🛠️ Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Open index.html in browser
```

## 📁 Project Structure

```
certificates/
├── app.py                 # Main script to fetch data and generate HTML
├── templates/
│   └── index.html        # Jinja2 template
├── index.html            # Generated static site
├── requirements.txt      # Python dependencies
├── .github/workflows/
│   └── deploy.yml        # GitHub Actions workflow
└── README.md
```

## 🎨 Customization

### Colors & Styling

Edit CSS variables in `templates/index.html`:

```css
:root {
    --primary: #2563eb;
    --secondary: #64748b;
    --accent: #f59e0b;
    /* ... more variables */
}
```

### Adding New Platforms

Platforms are automatically detected from your Google Sheet data in the `Certificate Type` column.

## 🔄 Workflow

1. **Daily Update**: GitHub Actions runs at midnight
2. **Data Fetch**: Pulls latest data from Google Sheets
3. **Build**: Generates new HTML with updated data
4. **Deploy**: Pushes to GitHub Pages
5. **Commit**: Updates main branch with latest HTML

## 📊 Statistics

The site automatically displays:

-   Total number of certificates
-   Number of unique platforms
-   Certificates earned this year

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

## 📄 License

MIT License - see LICENSE file for details

## 👤 Author

**Ha Trong Nguyen**

-   GitHub: [@htrnguyen](https://github.com/htrnguyen)
-   LinkedIn: [htrnguyen](https://www.linkedin.com/in/htrnguyen)
-   Facebook: [htrnguyenn](https://www.facebook.com/htrnguyenn)

---

⭐ **Star this repository if you find it helpful!**
