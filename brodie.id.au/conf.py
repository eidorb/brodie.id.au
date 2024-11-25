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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# Project information
project = "brodie.id.au"
author = "Brodie Blackburn"
copyright = "2021, 2024"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["ablog", "sphinx.ext.intersphinx", "myst_nb"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
html_title = "brodie.id.au"

# Include ‘Last updated on:’ timestamp.
html_last_updated_fmt = "%b %d, %Y"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_book_theme"

html_theme_options = {
    # https://sphinx-book-theme.readthedocs.io/en/latest/components/source-files.html#set-your-source-repository
    "repository_url": "https://github.com/eidorb/brodie.id.au",
    # https://sphinx-book-theme.readthedocs.io/en/latest/components/source-files.html#add-a-button-to-the-page-source
    "use_source_button": True,
    "repository_branch": "master",
    "path_to_docs": "brodie.id.au",
}

html_logo = "ambigram.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    # Include CSS to fix sidebar scrollbars.
    # TODO: Remove this once fix upstreamed to pydata-sphinx-theme.
    "fix.css",
    # Custom styling.
    "custom.css",
]


# Myst-NB options.
# Don't execute notebooks.
nb_execution_mode = "off"
myst_enable_extensions = ["dollarmath"]

# ABlog options.
post_date_format_short = "%b %d, %Y"
post_auto_image = 1
html_sidebars = {
    # blog page includes default and ablog sidebar elements.
    "blog": [
        "navbar-logo.html",
        "icon-links.html",
        "search-button-field.html",
        "sbt-sidebar-nav.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/archives.html",
    ],
    # blog post pages drop sidebar nav and add post info (postcard) sidebar elements.
    "blog/**": [
        "navbar-logo.html",
        "icon-links.html",
        "search-button-field.html",
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/archives.html",
    ],
}
