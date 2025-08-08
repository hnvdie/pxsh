from setuptools import setup,find_packages


setup(
   name="pxsh",
   version="0.1",
   packagses=find_packages(),
   install_requires=[],
   entry_points={
       "console_scripts":[
       "pxsh=pxsh.main:main",
       ],
      }
)
