from docutils.core import publish_string
import jinja2

def rst_filter(s):
    return jinja2.Markup(publish_string(source=s, writer_name='html'))

def register_filters(app):
    app.jinja_env.filters['rst'] = rst_filter
