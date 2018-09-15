from felement.app import app

from felement import views

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/special/', view_func=views.special)
app.add_url_rule('/ajax/send/email/', methods=['POST'], view_func=views.send_email)

# helpers
app.add_url_rule('/img/<filename>', endpoint='image', view_func=views.image_view)
