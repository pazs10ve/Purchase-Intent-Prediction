from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Read requirements
def read_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="purchase-intent-prediction",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="End-to-end MLOps project for predicting e-commerce purchase intent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pazs10ve/Purchase-Intent-Prediction",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.11.0",
            "isort>=5.12.0",
            "flake8>=6.1.0",
            "mypy>=1.7.0",
            "pre-commit>=3.6.0",
        ],
        "docs": [
            "sphinx>=7.2.0",
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.4.0",
        ],
        "serving": [
            "fastapi>=0.104.0",
            "uvicorn[standard]>=0.24.0",
            "gunicorn>=21.2.0",
        ],
        "monitoring": [
            "prometheus-client>=0.19.0",
            "grafana-api>=1.0.3",
            "evidently>=0.4.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "train-model=scripts.train_model:main",
            "evaluate-model=scripts.evaluate_model:main",
            "serve-model=scripts.serve_model:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.yml", "*.json", "*.txt"],
    },
    zip_safe=False,
)