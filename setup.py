from setuptools import setup, find_packages
setup(
    name = "pyopenshift",
    version = "0.2",
    packages = find_packages(),
    install_requires = ['requests'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['README', '*.rst', '*.txt'],
    },

    # metadata for upload to PyPI
    author = "Peter Ruan",
    author_email = "pruan@redhat.com",
    description = "This is a python interface for the new Openshift REST API.",
    license = "Apache v2",
    keywords = "PaaS Redhat OpenShift",
    url = "https://github.com/ypreiger/massemail.git",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
    entry_points = """
    [console_scripts]
    oshift = oshift:command_line
    """,
)
