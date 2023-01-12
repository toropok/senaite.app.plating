# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = "1.0.0"

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="senaite.app.plating",
    version=version,
    description="Plating worksheets",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords=["senaite", "lims", "plate"],
    author="Yme & TtD",
    author_email="ymettd@gmail.com",
    url="https://gitlab.timetodevelop.com/external/senaite-project/senaite.app.plating.git",
    packages=find_packages(where="src", include=("senaite*")),
    package_dir={"": "src"},
    namespace_packages=["senaite", "senaite.app"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "senaite.core",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "unittest2",
        ]
    },
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
