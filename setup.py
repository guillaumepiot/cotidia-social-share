import os
from distutils.core import setup
from setuptools import find_packages


VERSION = __import__("socialshare").VERSION

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
]

install_requires = [
]

# taken from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('socialshare'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:

        ################################################################################
        # !!! IMPORTANT !!!                                                            #
        # To get the right prefix, enter the index key of the same                     #
        # value as the length of your package folder name, including the slash.        #
        # Eg: for 'cmsbase/'' , key will be 8                                          #
        ################################################################################

        prefix = dirpath[12:] # Strip "socialshare/" or "socialshare\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name="cotidia-social-share",
    description="Django application to add sharing links on social network",
    version=VERSION,
    author="Guillaume Piot",
    author_email="guillaume@cotidia.com",
    url="https://bitbucket.org/guillaumepiot/cotidia-social-share",
    download_url="https://bitbucket.org/guillaumepiot/cotidia-social-share/downloads/cotidia-social-share-%s.tar.gz" % VERSION,
    package_dir={'socialshare': 'socialshare'},
    packages=packages,
    package_data={'socialshare': data_files},
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)
