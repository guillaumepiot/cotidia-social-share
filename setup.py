import os

from setuptools import find_packages, setup


def package_files(dirs):
    paths = []
    for directory in dirs:
        for (path, directories, filenames) in os.walk(directory):
            # Only keep the last directory of the path
            path = path.replace(directory, directory.split("/")[-1])
            for filename in filenames:
                paths.append(os.path.join(path, filename))
    return paths

template_files = package_files([
    'cotidia/cms/templates',
    'cotidia/cms/static'
])

setup(
    name="cotidia-social-share",
    description="Social share for Cotidia projects.",
    version="1.0",
    author="Guillaume Piot",
    author_email="guillaume@cotidia.com",
    url="https://code.cotidia.com/cotidia/social-share/",
    packages=find_packages(),
    package_dir={'socialshare': 'socialshare'},
    package_data={
        'cotidia.socialshare': template_files
    },
    namespace_packages=['cotidia'],
    include_package_data=True,
    install_requires=[
        'django-recaptcha',
        'django-rest-recaptcha',
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
)
