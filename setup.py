from setuptools import setup, find_packages

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='toto',
      description="package description",
      package=find_packages(),
      install_requires=requirements,
      scripts=['scripts/toto-run'])