from app import app

# Don't initialize database here - let app handle it
print("🚀 Starting TradePass on Railway...")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)  # debug=False for production

