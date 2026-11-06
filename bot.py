import os
import threading
from flask import Flask

# Keep-alive web server for Render
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Market Bot is active and scanning!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Start web server in background thread
threading.Thread(target=run_web_server, daemon=True).start()

DISCORD_WEBHOOK_URL = os.environ.get("https://discord.com/api/webhooks/1567978798929150112/6_udoyMWJMoPztiTsk5qqheeD3ejzMJA8kQ96YWJO2i6InCeA1rq7mk9LdCnQ9hFxajD")

FINNHUB_API_KEY = os.environ.get("dbmd8c9r01qn1o5qgei0dbmd8c9r01qn1o5qgeig")
