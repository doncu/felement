from flask import url_for
from flask import render_template


def sitemap_index():
    urls = (
        url_for('index'),
        url_for('marks'),
        url_for('contacts'),
        url_for('services'),
        url_for('help'),
        url_for('calc'),
    )
    return render_template('sitemaps/index.xml', urls=urls)
