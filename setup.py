from setuptools import setup

setup(
    name='pr_parse',
    version='0.0.1',
    description='A tool for parsing subunit files from persistent resources during an upgrade',
    author='Anthony D. Washington',
    url='https://github.com/antwash/pr_parse',
    install_requires=open('Requirements.txt').read(),
        classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'console_scripts': [
            'resource-parse = parse.resource:entry_point']})
