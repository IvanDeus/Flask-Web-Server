# 🌐 Flask Web Server

A simple, cross-platform, universal web server built using Flask library.  
It serves static files from the `/static` directory and can be run on **Windows**, **Linux**, **macOS**, **Android** (with Python support), and more!

---

## 📦 Requirements

- Python 3.x
- Flask

---

## ⚙️ Setup Instructions

0. **Setup Virtual Environment (optional):**

   ```bash
   python3 -m venv my-v-env
   source my-v-env/bin/activate
   ```
   
1. **Install:**

   ```bash
   pip install flask
   git clone https://github.com/IvanDeus/Flask-Web-Server.git
   cd Flask-Web-Server
   mkdir static
   ```

2. **Configure Settings:**

   - Edit `flask_web_server_cfg.py` to set:
     - Web server port (`WPORT`)
     - Debug mode (`DEBUG`)
     - Log file path (`LOGFILE`) *(optional)*

3. **Place Files:**

   - Put any static files (HTML, CSS, JS, images, etc.) in the `static/` directory.
   - These will be served at `http://localhost:<port>/filename.ext`

---

## ▶️ How to Run

In your terminal or command prompt:

```bash
python flask_web_server.py
```

By default, the server will start on port `1555`. You can access it via:

```
http://localhost:1555/
```

---

## 📁 Example File Structure

```
project_folder/
│
├── flask_web_server.py
├── flask_web_server_cfg.py
├── static/
│   ├── index.html
│   └── style.css
└── flask_web_server.log  (generated automatically)
```

---

## 📝 Logging

The server logs events such as startup and route access into the file defined by `LOGFILE` in your config.  
When `DEBUG=True`, logs are also printed to the console.

---

## 🧪 Customization Tips

- Change `WPORT` to use a different port.
- Set `DEBUG=True` for development mode with live reload and detailed error pages.
- Modify the main route (`'/'`) in `flask_web_server.py` to serve a custom homepage.

---

## ✅ Tested On

- Windows
- Linux
- Android (via Termux) 

---

2025 [ ivan deus ]
