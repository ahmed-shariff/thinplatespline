from setuptools import setup
from Cython.Build import cythonize
# from setuptools.extension import Extension

setup(
    name = "tps",
    version = "0.2",
    description='Thin plate spline transformation',
    author = "Oliver Tonnhofer",
    author_email = "olt@omniscale.de",
    license='MIT',
    packages=['tps', 'tps.test'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: C++",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering",
    ],
    test_suite = 'tps.test.test_suite',
    ext_modules=cythonize("tps/_tps.pyx"),
        # Extension("tps._tps", ["tps/_tps.cpp", "tps/thinplatespline.cpp"], libraries=["stdc++"]),
    zip_safe=False
)
