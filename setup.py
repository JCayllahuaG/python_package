from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requiremnts = f.read().splitlines()


setup(
    name='my_package',
    version='0.1',
    include_package_data=True,
    python_requires='>=3.8',
    packages=find_packages(),
    setup_requires=['setuptools-git-versioning'],
    install_requires=requiremnts,
    author='Jose Cayllahua',
    author_email="u202019558@upc.edu.pe",
    description='A small example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    version_config={
        "dirty_template": "{tag}",
    }
)