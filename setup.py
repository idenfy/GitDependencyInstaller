from distutils.core import setup
setup(
    name='git_dependency_installer',
    packages = ['git_dependency_installer'],
    version='1.0.0',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    description='SDK that helps to manage dependencies directly from git repositories.',
    include_package_data=True,
    install_requires=[],
    author='Deividas Tamkus',
    author_email='deividas@idenfy.com',
    keywords='Git Python Dependency Manager',
    url='https://github.com/idenfy/GitDependencyInstaller.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Operating System :: OS Independent',
    ],
)
