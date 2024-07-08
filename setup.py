from setuptools import setup, find_packages

setup(
    name="insurance_calculator",
    version="0.1.0",
    description="A library to calculate car insurance assurance amounts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="himavanthraavi23",
    author_email="himavanthraavi23@gmail.com",
    url="https://github.com/raavihimavanth23/x23101083_carinsurance",  # Update this with your actual URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

