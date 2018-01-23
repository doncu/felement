from werkzeug.contrib.fixers import ProxyFix

from vakaavto.app import app

app = ProxyFix(app)
