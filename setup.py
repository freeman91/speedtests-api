import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="",
    version="0.0.0",
    author="Addison Freeman",
    author_email="addisonfreeman91@gmail.com",
    description="API service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/freeman91/mongo-flask-api-template",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
