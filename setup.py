from setuptools import setup, find_packages


setup(
    name='pydom',
    version='0.1',
    packages=find_packages(),
    license='GPL',
    author='Umang Singhal',
    author_email='umang010894@gmail.com',
    url='https://github.com/umang-singhal/pydom',
    description=('Sharpness Estimation for Document and Scene Images.'),
    long_description=open('README.md').read(),
    install_requires=[
        'numpy',
        'opencv-python'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

    ]
)