from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='conda-test',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="conda test",
    license="MIT",
    author="Lars Buntemeyer",
    author_email='larsbuntemeyer@gmail.com',
    url='https://github.com/larsbuntemeyer/conda-test',
    packages=['conda-test'],
    entry_points={
        'console_scripts': [
            'conda-test=conda-test.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='conda-test',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
