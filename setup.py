from setuptools import find_packages, setup

setup(

    name='myblog',
    version='0.0.1',
    author="DidaZxc",
    author_email="didazxc@gmail.com",
    description = "Only for myself",

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=1.1.2',
        'Flask-SQLAlchemy>=2.4.3',
        'Flask-HTTPAuth>=4.0.0',
        'Flask-Cors>=3.0.8',
        'waitress>=1.4.3',
        'numpy>=1.18.4',
        'requests>=2.23.0'
    ],

    entry_points = {
        'console_scripts' : [
            'myblog = myblog.manage:main'
        ]
    }
)
