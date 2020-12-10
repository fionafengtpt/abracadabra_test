from setuptools import setup, find_packages

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="abracadabra",
    version="0.0.5",
    description="Making hypothesis and AB testing magically simple!",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Quizlet Data Team",
    author_email="data-team@quizlet.com",
    url="http://github.com/quizlet/abracadabra",
    packages=find_packages(),
    python_requires='>=3.7',
    # `install_requires` generated via `pipenv-setup sync`
    install_requires=[
        "appnope==0.1.0",
        "attrs==19.3.0",
        "backcall==0.1.0",
        "bleach==3.1.5",
        "cycler==0.10.0",
        "cython==0.29.19",
        "decorator==4.4.2",
        "defusedxml==0.6.0",
        "entrypoints==0.3",
        "importlib-metadata==1.6.0",
        "ipykernel==5.3.0",
        "ipython==7.15.0",
        "ipython-genutils==0.2.0",
        "ipywidgets==7.5.1",
        "jedi==0.17.0",
        "jinja2==2.11.2",
        "jsonschema==3.2.0",
        "jupyter==1.0.0",
        "jupyter-client==6.1.3",
        "jupyter-console==6.1.0",
        "jupyter-core==4.6.3",
        "kiwisolver==1.2.0",
        "markupsafe==1.1.1",
        "matplotlib==3.2.1",
        "mistune==0.8.4",
        "more-itertools==8.3.0",
        "nbconvert==5.6.1",
        "nbformat==5.0.6",
        "notebook>=6.1.4",
        "numpy==1.18.4",
        "packaging==20.4",
        "pandas==1.0.4",
        "pandocfilters==1.4.2",
        "parso==0.7.0",
        "patsy==0.5.1",
        "pexpect==4.8.0",
        "pickleshare==0.7.5",
        "pipfile==0.0.2",
        "pluggy==0.13.1",
        "prettytable==0.7.2",
        "prometheus-client==0.8.0",
        "prompt-toolkit==3.0.5",
        "ptyprocess==0.6.0",
        "py==1.8.1",
        "pygments==2.6.1",
        "pyparsing==2.4.7",
        "pyrsistent==0.16.0",
        "pystan==2.19.1.1",
        "pytest==5.4.2",
        "python-dateutil==2.8.1",
        "pytz==2020.1",
        "pyyaml==5.3.1",
        "pyzmq==19.0.1",
        "qtconsole==4.7.4",
        "qtpy==1.9.0",
        "scipy==1.4.1",
        "send2trash==1.5.0",
        "six==1.15.0",
        "statsmodels==0.11.1",
        "terminado==0.8.3",
        "testpath==0.4.4",
        "toml==0.10.1",
        "tornado==6.0.4",
        "traitlets==4.3.3",
        "wcwidth==0.2.2",
        "webencodings==0.5.1",
        "widgetsnbextension==3.5.1",
        "zipp==3.1.0",
    ],
    dependency_links=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization"
    ],
    keywords=[
        'AB testing',
        'analytics',
        'statistics',
        'Bayesian statistics',
        'Frequentist statistics'
    ],
    project_urls={
        'Bug Reports': 'https://github.com/quizlet/abracadabra/issues',
        'Source': 'https://github.com/quizlet/abracadabra/',
    },
    include_package_data=True
)
