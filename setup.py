from setuptools import setup, find_namespace_packages

setup(
    name='cli_assis_1teem',
    version='0.2.7',
    description='cli_assistant_project',
    url='https://github.com/Roman-Braneshty/Py6CoreProject-1',
    author='Троє в пітоні',
    author_email='robran54ff@gmail.com, katerynaklymentenko@gmail.com, o.romaniuk54@gmail.com',
    license='Apache',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'cli_assistant=cli_assis_1teem.main:main']}
)