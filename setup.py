from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="try-except-ai",
    version="0.1.0",
    author="Federico Ulfo",
    author_email="federicoulfo@gmail.com",
    description="A Python package to handle exceptions and suggest resolutions using OpenAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/etnalab/try-except-ai",
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
