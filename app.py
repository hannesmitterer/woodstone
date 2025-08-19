# --- INIT DB ---
if not os.path.exists(DB_NAME):
    init_db()
    # Create first admin user
    create_user("woodstone", "threefold-zes", role="admin")
    print("✅ Admin user created: username='woodstone', password='threefold-zes'")
from pathlib import Path
import tarfile
import os
import sqlite3

# --- BASE DIRECTORIES ---
base_dir = Path("woodstone_festival_2025_euystacio_warp")
app_dir = base_dir / "app"
static_dir = base_dir / "static"
templates_dir = base_dir / "templates"
pages_dir = base_dir / "pages-clean"

for d in [app_dir, static_dir, templates_dir, pages_dir]:
    d.mkdir(parents=True, exist_ok=True)

# --- STATIC CSS ---
(main_css := static_dir / "main.css").write_text("""
body { font-family: Arial, sans-serif; background-color:#f9f9f9; color:#222; margin:0; padding:0; }
header { background:#333; color:#fff; padding:1rem; text-align:center; }
button { background:#4CAF50; border:none; padding:10px 20px; color:#fff; border-radius:8px; cursor:pointer; }
button:hover { background:#45a049; }
.card { border:1px solid #ccc; padding:10px; margin:10px 0; border-radius:6px; background:#fff; }
""", encoding="utf-8")

# --- FLASK APP.PY ---
(app_py := app_dir / "app.py").write_text("""
from flask import Flask, render_template, request, redirect, url_for, session, flash
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

# --- ROUTES OMITTED FOR BREVITY ---
""", encoding="utf-8")

# --- TEMPLATES AND PAGES ---
# (Use same templates and pages setup as previous full warp script)

# --- CREATE TAR.GZ ---
tar_path = Path("woodstone_festival_2025_euystacio_warp_full_ready_admin.tar.gz")
with tarfile.open(tar_path, "w:gz") as tar:
    tar.add(base_dir, arcname=base_dir.name)

print(f"✅ Full warp TAR.GZ with admin created at {tar_path.resolve()}")
