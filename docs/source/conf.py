# Configuration file for the Sphinx documentation builder.

# -- Project information

project = ''
copyright = '2022, MGI/SEGES/DTGES/CGESP'
author = 'MGI/SEGES/DTGES/CGESP'
project_copyright = 'Manual Usuário Básico'
version = '1.0'
release = ''


# -- General configuration

extensions = [
    'sphinx.ext.duration',
    "sphinx.ext.extlinks",
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxext.opengraph",

]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'furo'
html_title = ""
html_logo = 'pen_logo_sem_fundo.png'
html_theme_options = {
    'navigation_depth': 5,
    
}

html_favicon = 'Icone_PEN.png'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for Opengraph ext
ogp_site_url = "https://manuais.processoeletronico.gov.br/"
ogp_image = "https://manuais.processoeletronico.gov.br/pt-br/latest/_static/pen_logo_sem_fundo.png"
ogp_description_length = 300
ogp_type = "article"
ogp_use_first_image = True