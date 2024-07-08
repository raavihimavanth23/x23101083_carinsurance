from setuptools import setup, find_packages

setup(
    name="insurance_calculator",
    version="0.1.0",
    description="A library to calculate car insurance assurance amounts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/insurance_calculator",  # Update this with your actual URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

