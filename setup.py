from setuptools import find_packages, setup

setup(
    name="your_package",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "your-command=your_package.module:main_function",
        ],
    },
)
