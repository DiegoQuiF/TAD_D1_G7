from src import init_app
from src.database.db import DatabaseManager
from flask_cors import CORS
import time

db = DatabaseManager().getInstancia()

app = init_app()
db.db.init_app(app)
app.app_context().push()

CORS(app)

if __name__ == '__main__':
    app.run(debug=True)