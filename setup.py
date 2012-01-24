from setuptools import setup, find_packages
import os

CLASSIFIERS = []

setup(
    author="Ales Kocjancic",
    author_email="ales.kocjancic@divio.ch",
    name='django-shop-multiplecurrencies',
    version='1.0.0',
    description='Multiple currencies for Django Shop',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='http://www.django-shop.org/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.2',
        'django-shop>=0.0.9',
    ],
    packages=find_packages(exclude=["example", "example.*"]),
    zip_safe = False
)

