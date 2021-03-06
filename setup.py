import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dev-ethanr-MasterReach1",
    version="0.1.0",
    author="Ethan Cox",
    author_email="mrxone2025@protonmail.com",
    description="A command line password generator tailored to your needs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MasterReach1/pw_gen",
    project_urls={
        "",
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU License",
        "Operating System :: Windows 10",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)