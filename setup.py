import versioneer

from distutils.core import setup


setup(
    name="cmpGen",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="David N. Mashburn",
    author_email="david.n.mashburn@gmail.com",
    packages=["cmpGen"],
    scripts=[],
    url="http://pypi.python.org/pypi/cmpGen/",
    license="LICENSE.txt",
    description="cmpGen is deprecated; it is maintained here for legacy purposes",
    long_description=open("README.rst").read(),
    install_requires=[],
)
