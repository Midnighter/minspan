try:
    from setuptools import setup
except:
    from distutils import setup

setup(
    name="minspan",
    version="0.1.0",
    py_modules=["minspan"],
    install_requires=[
        "cobra<=0.9.0",
        "numpy",
        "scipy<1.0.0",
        "sympy"
    ],
    author="Ali Ebrahim and Aarash Bordbar",
    author_email="aebrahim@ucsd.edu",
    url="https://github.com/SBRG/minspan",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7"
    ]
)
