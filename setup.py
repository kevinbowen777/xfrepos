import pathlib

import setuptools

long_description = pathlib.Path("README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="xfrepos-KEVIN-BOWEN",
    version="0.10.0",
    author="Kevin Bowen",
    author_email="kevin.bowen@gmail.com",
    description="Scripts for managing Xfce repositories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevinbowen777/xfrepos",
    project_urls={
        "Bug Tracker": "https://github.com/kevinbowen777/xfrepos/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3.15",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    package_dir={},
    packages=setuptools.find_packages(),
    python_requires=">=3.12",
)
