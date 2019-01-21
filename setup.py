from setuptools import setup, find_packages
from os import path

import versioneer


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sugartex',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description='More readable LaTeX language extension and transcompiler to LaTeX',
    long_description=long_description,
    long_description_content_type="text/markdown",

    url='https://github.com/kiwi0fruit/sugartex',

    author='Peter Zagubisalo',
    author_email='peter.zagubisalo@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    # keywords='sample setuptools development',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.6',
    install_requires=['panflute'],

    include_package_data=True,
    package_data={
        'sugartex': ['sugartex/*.py'],
    },
    entry_points={
        'console_scripts': [
            'sugartex=sugartex.sugartex_pandoc_filter:cli',
            'pre-sugartex=sugartex.pre_sugartex:main',
        ],
    },
)
