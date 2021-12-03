from setuptools import setup, find_packages




VERSION = '0.0.4'
DESCRIPTION = 'Wrapper for Crypto library to get encrytped key and data using less code and less complexity.'
with open('README.md') as f:
    long_description = f.read()

# Setting up
setup(
    name="CryptoAesGcm",
    version=VERSION,
    author="Hardik Seth",
    author_email="<hseth469@gmail.com>",
    url = '',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['Crypto', 'json', 'base64'],
    keywords=['python', 'Encryption', 'Decryption', 'Cypher', 'Aes', 'GCM'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ]
)