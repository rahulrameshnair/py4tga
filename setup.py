from setuptools import setup, find_packages

setup(
    name="py4tga",
    version="0.1.0",
    description="Python for thermogravimetry analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Rahul Ramesh Nair",
    author_email="rahulascents@gmail.com",
    maintainer="Rahul Ramesh Nair",
    maintainer_email="rahulascents@gmail.com",
    url="https://github.com/rahulrameshnair/py4tga",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"": ["*.*"]},
    classifiers=[],
    license="MIT license",
    install_requires=[],
    extras_require={
        "dev": ["coverage", "mypy", "pytest", "ruff"]
    },
    project_urls={
        "Bug Tracker": "https://github.com/rahulrameshnair/py4tga/issues",
        "Changelog": "https://github.com/rahulrameshnair/py4tga/blob/master/changelog.md",
        "Homepage": "https://github.com/rahulrameshnair/py4tga"
    }
)
