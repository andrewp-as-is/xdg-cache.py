import setuptools

setuptools.setup(
    name='xdg-cache',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
