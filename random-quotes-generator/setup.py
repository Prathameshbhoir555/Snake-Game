from setuptools import setup, find_packages

setup(
    name="random-quotes-generator",
    version="1.0.0",
    description="A program that generates random quotes",
    author="Prathamesh",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["random_quotes"],
    install_requires=[
        # Add any dependencies here
        # For example: "requests>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
