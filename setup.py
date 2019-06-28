from setuptools import setup, find_packages


with open('README.md', 'r') as fh:
    long_description = fh.read()

version = '0.0.7'

setup(
    name='flashtorch',
    version=version,
    author='Misa Ogura',
    author_email='misa.ogura01@gmail.com',
    description='Visualisation toolkit for neural networks in PyTorch',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MisaOgura/flashtorch',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    package_data={'flashtorch.utils.resources':
        ['imagenet_class_index.json']
    },
    install_requires=[
        'matplotlib',
        'numpy',
        'Pillow',
        'torch',
        'torchvision',
        'importlib_resources'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
