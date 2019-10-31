"""
Setup Documentation
"""
import setuptools


REQUIRED = [
    "numpy",
    "pandas",
    "scipy",
]
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    setuptools.setup(
        name="datutil",
        version = "1.0.3",
        author = "bmulas1535",
        description = "A collection of classes and functions for common data science processes.",
        long_description = LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://lambdaschool.com/courses/data-science",
        packages=setuptools.find_packages(),
        python_requires=">=3.7",
        install_requires = REQUIRED,
        classifiers=["Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ]
        )
