import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="missingpy",
    version="0.2.3",
    author="{2023 maintain: eedrobup, Original: Ashim Bhattarai}",
    description="Missing Data Imputation for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eedrobup/missingpy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
)
