from setuptools import setup, find_packages

setup(
    name="create_project",
    version="0.0.1",
    # package_dir = {
    #     "create_project":"create_project",
    #     "create_project.functions":"create_project/functions",
    #     "create_project.config":"create_project/config"
    # },
    # packages=["create_project", "create_project.functions", "create_project.config"],
    packages=find_packages(),
    url="https://github.com/isaacismaelx14/Project-Manager-CLI/",
    license="MIT License",
    author="Isaac Martinez",
    author_email="isaacismaelx14@gmail.com",
    description="With this script you have a template for create react components with some default files",
    entry_points={
        'console_scripts': ['create_project = create_project.app:main'],
    }
)