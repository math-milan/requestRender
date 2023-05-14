from setuptools import setup

setup(
    name="requestRender",
    version="0.0.1",
    description="A PyPI package that provides a simple headless Selenium web browser for scraping wrapper around reactive websites.",
    py_modules=["requestRender"],
    package_dir={"": "src"},

    maintainer="Milan Lovis Ramthun",
    maintainer_email="dev.math.milan@gmail.com",

    install_requires=[
        "chromedriver_autoinstaller",
        "requests",
        "selenium"
    ]
)