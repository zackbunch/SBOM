import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sysk-zackbunch",
    version="0.0.1",
    author="Zack Bunch",
    author_email="zackbunch96@gmail.com",
    description="Shit You Should Know Software Bill of Materials",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zackbunch/sysk",
    project_urls={
        "Bug Tracker": "https://github.com/zackbunch/sysk/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
