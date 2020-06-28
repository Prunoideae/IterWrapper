import setuptools

setuptools.setup(
    name="iterwrapper",
    version="0.1.4",
    author="Prunoideae",
    author_email="a455167189@163.com",
    description="A wrapper for FP style iterator manipulation",
    long_description=open("readme.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Prunoideae/IterWrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
