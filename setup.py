import setuptools

setuptools.setup(
    name="gramformer",
    version="1.0",
    author="prithiviraj damodaran",
    author_email="",
    description="Gramformer",
    long_description="A framework for detecting, highlighting and correcting grammatical errors on natural language text",
    url="https://github.com/PrithivirajDamodaran/Gramformer.git",
    packages=setuptools.find_packages(),
    install_requires=['transformers', 'sentencepiece', 'python-Levenshtein', 'fuzzywuzzy',  'tokenizers', 'fsspec', 'lm-scorer', 'errant'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
)

