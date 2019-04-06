from setuptools import setup
#from distutils.core import setup, Extension

setup(name = 'MQccdt.json',
    version = '1.1',
    description = 'Python code to validate an IBM MQ ccdt.json file.',
    long_description= 'Python code to validate an IBM MQ ccdt.json file.',
    author='Colin Paice',
    author_email='colinpaicemq@gmail.com',
    url='https://github.com/colinpaicemq/MQccdt.json/',
    download_url='https://github.com/colinpaicemq/MQccdt.json/',
    platforms='OS Independent',
    #packages = find_packages('pymqi'),
    #packages = ['mqtools'],
    license='Python Software Foundation License',
    keywords=('MQ IBM ccdt jsonF'),
    include_package_data=True,
    
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Python Software Foundation License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
