import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gploter", 
    version="0.1",
    scripts=['gploter'],
    author="rakshit kumar",
    author_email="rakshitkhpi@example.com",
    description="A  python library to plot charts from google sheet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spctr01/gploter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ['streamlit', 'plotly', 'pandas'],
    python_requires='>=3.6',
)
