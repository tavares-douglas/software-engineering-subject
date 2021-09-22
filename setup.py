import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='testing-implementation',
    version='0.0.1',
    packages=setuptools.find_packages(),
    author='douglas',
    author_email='tavares-douglas@outlook.com',
    description='software-engineering subject appointment',
    install_requires=required
)