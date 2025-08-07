from flask import Flask
from flask_smorest import Api
from resources.store import blp as StoreBlueprint
from resources.item import blp as ItemBlueprint  # ← importa el nuevo blueprint

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Store and Item API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(StoreBlueprint)
api.register_blueprint(ItemBlueprint)  # ← registra el blueprint
