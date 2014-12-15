"""
Set up pytravis for your environment
pytravis <http://github.com/jmullan/pytravis>
"""

from setuptools import setup
import pytravis.pytravis

setup(
    name="pytravis",
    version=pytravis.pytravis.__version__,
    description="Extract stuff from Digital Photo Professional into XMP",
    license="GPLv3+",
    author="Jesse Mullan",
    author_email="jmullan@visi.com",
    url="http://github.com/jmullan/pytravis",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
        "GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"],
    packages=['pytravis'],
    py_modules=["pytravis"],
    scripts=['bin/pytravis'])
