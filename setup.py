from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = '''\
      Package computing total image volume
      in different units.'''
  
setup(
        name ='calcvol',
        version ='0.0.1',
        author ='Michael Dayan',
        author_email ='michael.dayan@fcbg.ch',
        url ='https://github.com/neurorepro/calcvol',
        description ='Compute total image volume',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'calcvol = calcvol.__main__:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='neuroimaging nifti volume',
        install_requires = requirements,
        zip_safe = False
)