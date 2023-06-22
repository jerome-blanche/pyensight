"""The setup script."""
from distutils.core import setup
import os

# Add version constraints to play nice with other packages
# running on Ansys Lab.  Which versions to use is determined
# by installing the pyensight wheel on Ansys Lab and seeing
# what pip complains about.
REQUIREMENTS = [
    "protobuf>=3.9.1",
    "grpcio>=1.23.0",
    "numpy>=1.20.0",
    "Pillow>=9.3.0",
    "requests>=2.20.1",
    "urllib3>=1.25.4",
    "dill>=0.3.5.1",
]

curr_dir = os.path.abspath(os.path.dirname(__file__))


def get_file_text(file_name):
    with open(os.path.join(curr_dir, file_name), "r", encoding="utf-8") as in_file:
        return in_file.read()


_version = {}
_version_file = os.path.join(curr_dir, "src", "ansys", "pyensight", "_version.py")
with open(_version_file) as fp:
    exec(fp.read(), _version)
version = _version["VERSION"]

packages = [
    "ansys",
    "ansys.api",
    "ansys.api.enshell",
    "ansys.api.enshell.v0",
    "ansys.api.ensight",
    "ansys.api.ensight.v0",
    "ansys.pyensight",
    "ansys.pyensight.utils",
    "ansys.tests.ensight",
    "ansys.tests.ensight.example_tests",
    "ansys.tests.ensight.unit_tests",
]


setup(
    name="ansys-ensight",
    version=version,
    description="Python interface to Ansys EnSight",
    long_description=get_file_text("README.rst") + "\n\n" + get_file_text("CHANGELOG.rst"),
    long_description_content_type="text/x-rst",
    author="ANSYS, Inc.",
    author_email="pyansys.support@ansys.com",
    maintainer="PyAnsys developers",
    maintainer_email="pyansys.maintainers@ansys.com",
    license="MIT",
    packages=packages,
    package_dir={
        "ansys": "src/ansys",
        "ansys.pyensight": "src/ansys/pyensight",
        "ansys.api": "src/ansys/api",
        "ansys.api.enshell": "src/ansys/api/enshell",
        "ansys.api.enshell.utils": "src/ansys/api/enshell/utils",
        "ansys.api.enshell.v0": "src/ansys/api/enshell/v0",
        "ansys.api.ensight": "src/ansys/api/ensight",
        "ansys.api.ensight.utils": "src/ansys/api/ensight/utils",
        "ansys.api.ensight.v0": "src/ansys/api/ensight/v0",
        "ansys.tests.ensight": "tests",
        "ansys.tests.ensight.example_tests": "tests/example_tests",
        "ansys.tests.ensight.unit_tests": "tests/unit_tests",
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    url="https://github.com/ansys/pyensight",
    project_urls={
        "Documentation": "https://ensight.docs.pyansys.com/",
        "Changelog": "https://github.com/ansys/pyensight/blob/main/CHANGELOG.rst",
        "Bug Tracker": "https://github.com/ansys/pyensight/issues",
        "Source Code": "https://github.com/ansys/pyensight",
    },
    python_requires=">=3.9",
    keywords="ensight pyensight pyansys ansys",
    test_suite="tests",
    install_requires=REQUIREMENTS,
)
