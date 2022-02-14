import os
from setuptools import setup, find_packages, Command

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('del ./*.egg-info')

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='ask_nature_scraper',
      description="package needed to scrape",
      package=find_packages(),
      install_requires=requirements,
      cmdclass={'clean': CleanCommand})