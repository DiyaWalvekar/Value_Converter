import os
port = int(os.environ.get("PORT", 5000))  # Use Railway's assigned port
app.run(host="127.0.0.1", port=port)
