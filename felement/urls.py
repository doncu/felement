from felement.app import app

# from felement.admin import views
from felement.views import ajax
from felement.views import pages
from felement.views import helpers
from felement.views import sitemap


app.add_url_rule('/ajax/send/email/', methods=['POST'], view_func=ajax.send_email)

app.add_url_rule('/', view_func=pages.index)

app.add_url_rule('/sitemaps.xml', view_func=sitemap.sitemap_index)

# helpers
app.add_url_rule('/img/<filename>', endpoint='image', view_func=helpers.image_view)
