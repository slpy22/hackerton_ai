import logging
import connexion


logging.basicConfig(level=logging.INFO)
app = connexion.FlaskApp(__name__, specification_dir="../spec")
app.add_api("estate.yaml")
application = app.app


if __name__ == "__main__":
    app.run(port=8010)
