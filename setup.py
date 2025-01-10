from setuptools import setup, find_packages

setup(
    name="aoc-colab-template",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'ipython',
        'advent-of-code-data',  # aocd package
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A template generator for Advent of Code solutions in Google Colab",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/aoc-colab-template",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
