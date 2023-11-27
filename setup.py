from setuptools import setup

with open('requirements.txt', 'r') as f:
    reqs = f.readlines()

    setup(
        name='package_test',
        version='0.1',
        description='A sample Python package',
        author='Alessio',
        author_email='a@example.com',
        packages=['my_package'],
        install_requires=reqs,
        include_package_data=True,
        package_data={
            'static': ['*'],
        },
        zip_safe=False,
    )
