from api import createApp
from dotenv import load_dotenv
import os

load_dotenv()

app = createApp()

if __name__ == "__main__":
    debug_mode = os.environ.get("DEBUG", "False").lower() == "true"
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=debug_mode, port=port)