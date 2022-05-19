from setuptools import setup, find_packages

setup(
    name="pybe",
    version="0.0.1",
    description="Python backend",
    author="Cristina",
    author_email="",
    # url="https://github.com/CleverSoftwareSolutions/fashion_flask/",
    package_dir={"": "src/"},
    packages=find_packages("src/"),
)
