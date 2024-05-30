# -- Project information

project = 'TAD3'
copyright = '2024'
author = 'BlockTrans Syndicate'

release = '0.1'
version = '0.1.0'

extensions = [
    'recommonmark',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_markdown_tables',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
master_doc = 'index'
html_static_path = ['_static']
html_favicon = '_static/favicon.ico'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'navigation_depth': 4,
}

def setup(app):
    app.add_config_value('recommonmark_config', {
        'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)
    
# CSS not working RN
# def setup(app):
#     app.add_css_file('custom.css')
#
# html_context = {
#     'css_files': [
#         'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap',
#     ],
# }
