# 🌐 Flask Web Server

A simple, cross-platform, universal web server built using Flask library.  
It serves static files from the `/static` directory and can be run on **Windows**, **Linux**, **macOS**, **Android** (with Python support), and can be publicly accessible via ngrok!

---

## 📦 Requirements

- Python 3.x
- Flask
- ngrok (optional)

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

   Every setting comes from a `FWS_*` environment variable, falling back to the built-in default when unset. The one exception is `NGROK_AUTHTOKEN`, which keeps ngrok's own name so the tunnel can read it directly.

   | Env variable | Default | Meaning |
   |---|---|---|
   | `FWS_HOST` | `0.0.0.0` | Address to bind (`0.0.0.0` = reachable from other machines) |
   | `FWS_PORT` | `1555` | TCP port |
   | `FWS_DEBUG` | off | Debug logs + Werkzeug debugger; accepts `1/true/yes/on` |
   | `FWS_LOGFILE` | `flask_web_server.log` | Log file path *(relative to the current directory)* |
   | `FWS_STATIC` | `<script dir>/static` | Directory to serve |
   | `NGROK_AUTHTOKEN` | unset | If set (and `pip install ngrok`), also expose the server through an ngrok tunnel |
   | `FWS_NGROK_DOMAIN` | unset | Reserved/standard ngrok domain to bind, e.g. `fitting-sturgeon-dynamic.ngrok-free.app` |

   Paths work as follows:

   - The default `static/` is anchored to the directory containing `flask_web_server.py`, **not** to where you launch the command, so `python /path/to/Flask-Web-Server/flask_web_server.py` still serves `/path/to/Flask-Web-Server/static`.
   - A `FWS_STATIC` value is converted to an absolute path at startup: a relative value such as `FWS_STATIC=./site` resolves against the directory you launch from, and an absolute value (`FWS_STATIC=/srv/mysite/static`) is used as given.
   - `FWS_LOGFILE` is not rewritten, so a relative log path lands in the directory you launch from.

   Export the variables per deployment:

   ```bash
   FWS_PORT=8080 FWS_HOST=127.0.0.1 python3 flask_web_server.py
   ```

3. **Place Files:**

   - Put any static files (HTML, CSS, JS, images, etc.) in the `static/` directory.
   - `static/index.html` is served at `/`; everything else under `/static/`, e.g. `http://localhost:<port>/static/style.css`.

---

## ▶️ How to Run

In your terminal or command prompt:

```bash
python flask_web_server.py
```

By default, the server will start on port `1555` and print the address it is reachable on:

```
IP:PORT 192.168.1.42:1555 (also reachable as 127.0.0.1:1555)
```

From the same machine you can use:

```
http://localhost:1555/
```

For production use PM2 service (with Virtual Environment):
```bash
pm2 start flask_web_server.py --interpreter /home/user/my-v-env/bin/python3
```

### Public access via ngrok (optional)

Without `NGROK_AUTHTOKEN` the server behaves exactly as above. Set it and the tunnel starts with the server, logging its public URL:

```bash
pip install ngrok
```
```
NGROK_AUTHTOKEN=xxxx python3 flask_web_server.py
```
```
INFO: Ngrok tunnel: https://fitting-sturgeon-dynamic.ngrok-free.app
```

---

## 📁 Example File Structure

```
project_folder/
│
├── flask_web_server.py
├── static/
│   ├── index.html
│   └── style.css
└── flask_web_server.log  (generated automatically)
```

---

## 📝 Logging

The server logs startup and every incoming request (method, path, status, client IP) to both the file defined by `FWS_LOGFILE` and the console, so a running server is readable without `tail`. To follow the file instead:
```
tail -f flask_web_server.log
```
---

## ✅ Tested On

- Windows
- Linux
- Android (via Termux) 

---

2025 [ ivan deus ]
