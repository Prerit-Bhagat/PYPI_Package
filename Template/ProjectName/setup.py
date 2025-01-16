# from setuptools import setup, find_packages
# from pathlib import Path

# # Read the contents of your README file
# this_directory = Path(__file__).parent
# long_description = (this_directory / "README.md").read_text() #Gets the long description from Readme file

# setup(
#     name='TOPSIS_Prerit_102217030',
#     version='0.0',
#     packages=find_packages(),
#     install_requires=[
#         'pandas','numpy',
#     ],  # Add a comma here
#     author='Prerit Bhagat',
#     author_email='preritbhagat.pb@gmail.com',
#     description='This is the short description',

#     long_description=long_description,
#     long_description_content_type='text/markdown',
#     license='MIT',
#      project_urls={
#            'Source Repository': 'https://github.com/A-Sharan1/' #replace with your github source
#     }
# )

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()  # Gets the long description from Readme file

setup(
    name='TOPSIS_Prerit_102217030',
    version='1.0.0',  # Updated to reflect initial release
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    author='Prerit Bhagat',
    author_email='preritbhagat.pb@gmail.com',
    description='A Python package for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='topsis mcdm multi-criteria decision-making ranking analysis',
    project_urls={
        'Documentation': 'https://github.com/Prerit-Bhagat/PYPI_Package#readme',  # Replace with your GitHub documentation link
        'Source Repository': 'https://github.com/Prerit-Bhagat/PYPI_Package',  # Replace with your actual GitHub repository link
        'Bug Tracker': 'https://github.com/Prerit-Bhagat/PYPI_Package/issues',  # Replace with your issue tracker
    },
    python_requires='>=3.7',
)



