from setuptools import setup, find_packages

setup(
    name="create_component",
    version="1.2",
    packages=find_packages(),
    url="https://github.com/isaacismaelx14/Project-Manager-CLI/",
    license="MIT License",
    author="Isaac Martinez",
    author_email="isaacismaelx14@gmail.com",
    description="With this script you have a template for create react components with some default files",
    entry_points={
        'console_scripts': ['create_component = create_component.app:main'],
    }
)