from setuptools import setup, find_packages

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='ask_nature_scraper',
      description="package needed to scrape",
      package=find_packages(),
      install_requires=requirements)