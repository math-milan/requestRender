from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="requestRender",
    version="0.0.2",
    description="A PyPI package that provides a simple headless Selenium web browser for scraping wrapper around reactive websites.",
    packages=["requestRender"],
    package_dir={"": "src"},

    maintainer="Milan Lovis Ramthun",
    maintainer_email="dev.math.milan@gmail.com",

    install_requires=[
        "chromedriver_autoinstaller",
        "requests",
        "selenium"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/math-milan/requestRender"
)