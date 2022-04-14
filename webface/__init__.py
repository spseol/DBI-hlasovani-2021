import flask

# from flask_misaka import Misaka


class MyFlask(flask.Flask):
    def select_jinja_autoescape(self, filename):
        if filename.endswith(".html.j2"):
            return True
        return super().select_jinja_autoescape(self, filename)


app = MyFlask(__name__)
# Misaka(app)
app.secret_key = b"totoj e zceLa n@hodny retezec nejlepe os.urandom(24)"
app.secret_key = b"x6\x87j@\xd3\x88\x0e8\xe8pM\x13\r\xafa\x8b\xdbp\x8a\x1f\xd41\xb8"

from . import routes


# from . import models
