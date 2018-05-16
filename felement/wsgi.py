from werkzeug.contrib.fixers import ProxyFix

from felement.app import app

app = ProxyFix(app)
