import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="binotel",
    version="0.0.1",
    author="Rostyslav",
    author_email="rostyslav.rigroup@gmail.com",
    description="This package provides Python implementation of some Binotel api. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/srostyslav/binotel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
