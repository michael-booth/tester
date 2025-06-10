from setuptools import setup

install_requires = [
    'requests==2.32.4',
]

dev_requires = [
    'pytest==7.2.2',
]


setup(
    name="tester",
    version="0.0.1",
    description="Test project",
    include_package_data=True,
    platforms="any",
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
    }
)