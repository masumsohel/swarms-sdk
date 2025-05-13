from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="swarms-sdk",
    version="0.1.0",
    author="Swarms",
    author_email="support@swarms.world",
    description="A production-grade Python client for the Swarms API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swarms-ai/swarms-sdk",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "aiohttp>=3.8.0",
        "requests>=2.28.0",
        "pydantic>=1.10.0",
        "loguru>=0.6.0",
        "typing-extensions>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.18.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "isort>=5.10.0",
            "mypy>=0.990",
            "flake8>=4.0.0",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/swarms-ai/swarms-sdk/issues",
        "Source": "https://github.com/swarms-ai/swarms-sdk",
        "Documentation": "https://docs.swarms.world",
    },
) 