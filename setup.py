from setuptools import setup, find_packages

setup(
    name="stakeengine",
    version="0.0.0",
    description="Tools for defining and simulating slot-game mathematics",
    python_requires=">=3.12",
    author="CarrotRGS",
    packages=find_packages(),
    install_requires=[
        "boto3>=1.35,<2",
        "numpy>=2,<3",
        "python-dotenv>=1,<2",
        "xlsxwriter>=3,<4",
        "zstandard>=0.23,<1",
    ],
)
