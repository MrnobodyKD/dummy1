from app import app, db

# Create tables if they don't exist
with app.app_context():
    db.create_all()
    print("✅ Database tables created/verified")
