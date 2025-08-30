
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory, send_file
import sqlite3, os

app = Flask(__name__)
app.secret_key = "supersecretkey"
DB_NAME = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    schema = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT CHECK(role IN ('tutor','visitor','admin')) NOT NULL
    );
    CREATE TABLE IF NOT EXISTS content (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        body TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        author_id INTEGER,
        FOREIGN KEY(author_id) REFERENCES users(id)
    );
    '''
    conn = get_db_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()

def create_user(username,password,role="visitor"):
    conn = get_db_connection()
    conn.execute("INSERT INTO users (username,password,role) VALUES (?,?,?)",(username,password,role))
    conn.commit()
    conn.close()

# --- INIT DB AND CREATE FIRST ADMIN ---
if not os.path.exists(DB_NAME):
    init_db()
    create_user("woodstone", "threefold-zes", role="admin")
    print("✅ Admin user created: username='woodstone', password='threefold-zes'")

@app.route("/")
def index():
    return "Euystacio Portal is live. <a href='/woodstone'>Woodstone Festival</a> | <a href='/chat'>Chat</a> | Login at /login"

@app.route("/woodstone")
def woodstone():
    """Serve the Woodstone Festival landing page"""
    try:
        with open('woodstone.md', 'r') as f:
            content = f.read()
        # Convert markdown to basic HTML for display
        html_content = content.replace('\n', '<br>').replace('# ', '<h1>').replace('</h1><br>', '</h1>').replace('### ', '<h3>').replace('</h3><br>', '</h3>').replace('* ', '<li>').replace('<li>', '<ul><li>').replace('<br><ul>', '</ul><br><ul>')
        return f"<html><head><title>Woodstone Festival</title><style>body{{font-family:Arial,sans-serif;margin:40px;}}h1,h3{{color:#4caf50;}}</style></head><body>{html_content}</body></html>"
    except FileNotFoundError:
        return "Woodstone Festival landing page not found", 404

@app.route("/chat")
def chat():
    """Serve the chat module"""
    return send_file('chat/index.html')

@app.route("/chat/<path:filename>")
def chat_assets(filename):
    """Serve chat assets (CSS, JS)"""
    return send_from_directory('chat', filename)

@app.route("/assets/<path:filename>")
def assets(filename):
    """Serve assets like the emblem"""
    return send_from_directory('assets', filename)

@app.route("/js/<path:filename>")
def javascript(filename):
    """Serve JavaScript files like harmonic bridge map"""
    return send_from_directory('js', filename)

@app.route("/metadata.json")
def metadata():
    """Serve metadata file"""
    return send_file('metadata.json')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
