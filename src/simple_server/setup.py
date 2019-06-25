import setuptools

setuptools.setup(
    name="simple_server",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=["flask", "simple_package==0.0.2"],
)
