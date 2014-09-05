from setuptools import setup, find_packages

def runtests():
    import os
    import sys
    
    import django
    from django.core.management import call_command
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
    if django.VERSION[0] == 1 and django.VERSION[1] >= 7:
        django.setup()
    call_command('test')
    sys.exit()

setup(
    name = "django-report-builder",
    version = "2.0.2",
    author = "David Burke",
    author_email = "david@burkesoftware.com",
    description = ("Query and Report builder for Django ORM"),
    license = "BSD",
    keywords = "django report",
    url = "https://github.com/burke-software/django-report-builder",
    packages=find_packages(),
    include_package_data=True,
    test_suite='setup.runtests',
    tests_require=(
        'south',
        'argparse',
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        'django>=1.4',
        'openpyxl',
        'python-dateutil',
        'django-report-utils>=0.2.3',
    ]
)
