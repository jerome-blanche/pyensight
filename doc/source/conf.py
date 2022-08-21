"""Sphinx documentation configuration file."""
from datetime import datetime
import os
import sys

from ansys_sphinx_theme import ansys_favicon, pyansys_logo_black
from sphinx_gallery.sorting import FileNameSortKey

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from ansys.pyensight import __version__  # noqa

# Project information
project = "ansys.pyensight"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "Ansys Inc."
release = version = __version__

# HTML output options
html_short_title = html_title = "PyEnSight"
html_logo = pyansys_logo_black
html_theme = "ansys_sphinx_theme"
html_favicon = ansys_favicon
html_theme_options = {
    "github_url": "https://github.com/pyansys/pyensight",
    "show_prev_next": False,
    "show_breadcrumbs": True,
}

# Sphinx extensions
extensions = [
    "numpydoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_gallery.gen_gallery",
]

autoapi_options = [
    "members",
    "undoc-members",
    "private-members",
    "special-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
    # kept here as an example
    # "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    # "numpy": ("https://numpy.org/devdocs", None),
    # "matplotlib": ("https://matplotlib.org/stable", None),
    # "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    # "pyvista": ("https://docs.pyvista.org/", None),
}

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    # "SS03", # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}

# -- Sphinx Gallery Options
examples_source = os.path.join(os.path.dirname(__file__), "examples_source")
default_gallery_thumbnail = os.path.join(examples_source, "default_thumb.png")

sphinx_gallery_conf = {
    # convert rst to md for ipynb
    "pypandoc": False,
    # path to your examples scripts
    "examples_dirs": [examples_source],
    # path where to save gallery generated examples
    "gallery_dirs": ["_examples"],
    # Pattern to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": None,
    # the initial notebook cell
    "first_notebook_cell": ("# PyEnSight example Notebook\n" "#\n"),
    "default_thumb_file": default_gallery_thumbnail,
    "plot_gallery": False,
}

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# exclude traditional Python prompts from the copied code
copybutton_prompt_text = r">>> ?|\.\.\. "
copybutton_prompt_is_regexp = True
