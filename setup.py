# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under the Apache license (see LICENSE)
from setuptools import setup

VERSION = "0.1.0"

REQUIRES = ["click", "markdown"]

setup(
    name="mkdocs_click",
    version=VERSION,
    description="An mkdocs extension to document click methods",
    keywords="mkdocs datadog click",
    url="https://github.com/DataDog/mkdocs-click",
    author="Datadog",
    author_email="packages@datadoghq.com",
    license="Apache",
    packages=["mkdocs_click"],
    install_requires=REQUIRES,
    python_requires=">=3.0",
    include_package_data=True,
    entry_points={"markdown.extensions": ["mkdocs-click = mkdocs_click:MKClickExtension"]},
)
