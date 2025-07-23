from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Ishant Garg",
    author_email="ishant.garg@example.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "pyPDF2"],
    packages=find_packages(),
)