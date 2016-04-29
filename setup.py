# (C) Copyright Digital Economy Limited 2014-2015

from setuptools import find_packages, setup
import template

setup(
    name='opp template service',
    version=template.__version__,
    description='Open Permissions Platform Template Service',
    author='CDE Catapult',
    author_email='support-copyrighthub@cde.catapult.org.uk',
    url='https://github.com/openpermissions/template-srv',
    packages=find_packages(exclude=['test']),
    entry_points={
        'console_scripts':
            ['template-svr = template.app:main']},
    )
