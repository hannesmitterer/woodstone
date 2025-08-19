# --- INIT DB ---
if not os.path.exists(DB_NAME):
    init_db()
    # Create first admin user
    create_user("woodstone", "threefold-zes", role="admin")
    print("✅ Admin user created: username='woodstone', password='threefold-zes'")
