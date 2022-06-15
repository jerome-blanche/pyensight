"""The setup script."""
import os

from setuptools import setup

REQUIREMENTS = ["grpcio", "requests"]

curr_dir = os.path.abspath(os.path.dirname(__file__))


def get_file_text(file_name):
    with open(os.path.join(curr_dir, file_name), "r", encoding="utf-8") as in_file:
        return in_file.read()


version = {}
_version_file = os.path.join(curr_dir, "src", "ansys", "pyensight", "_version.py")
with open(_version_file) as fp:
    exec(fp.read(), version)

setup(
    name="ansys-ensight",
    version=version["VERSION"],
    description="Python interface to ANSYS-EnSight",
    long_description=get_file_text("README.rst")
    + "\n\n"
    + get_file_text("CHANGELOG.rst"),
    long_description_content_type="text/x-rst",
    author="ANSYS, Inc.",
    author_email="pyansys.support@ansys.com",
    maintainer="PyAnsys developers",
    maintainer_email="pyansys.maintainers@ansys.com",
    license="MIT license",
    packages=["ansys"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    url="https://github.com/pyansys/pyensight",
    project_urls={
        "Documentation": "https://docs.pyansys.com/",
        "Changelog": "https://github.com/pyansys/pyensight/blob/main/CHANGELOG.rst",
        "Bug Tracker": "https://github.com/pyansys/pyensight/issues",
        "Source Code": "https://github.com/pyansys/pyensight",
    },
    python_requires=">=3.7",
    keywords="py ensight pyensight pyansys ansys",
    test_suite="tests",
    install_requires=REQUIREMENTS,
)
