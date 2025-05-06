from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:  # noqa
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="dockdump",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Docker memory forensics tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0x8j0rn4r80r93/dockdump",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "License     :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "dockdump=dockdump.cli:cli",
        ],
    },
)
