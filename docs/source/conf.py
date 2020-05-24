# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('.', '..', '..')))


# -- Project information -----------------------------------------------------

project = 'Natch'
copyright = ' Ertuğrul Noyan Keremoğlu'
author = 'Ertuğrul Noyan Keremoğlu'

# The full version, including alpha/beta/rc tags
version = '1.0.0'
release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    'show_powered_by': False,
    'show_related': False,
    'github_user': 'ertgl',
    'github_repo': 'natch',
    'github_banner': False,
}

html_show_sourcelink = False

html_show_sphinx = False

html_show_copyright = True

html_sidebars = {
    'index': [
        'styles.html',
        'logo.html',
        'github.html',
        'navigation.html',
        'links.html',
        'searchbox.html',
    ],
    '**': [
        'styles.html',
        'logo.html',
        'github.html',
        'navigation.html',
        'links.html',
        'searchbox.html',
    ],
}

autodoc_default_options = {
    'member-order': 'bysource',
    'undoc-members': True,
    'inherited-members': True,
    'imported-members': True,
}
