from distutils.core import setup

with open('./README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='pipe-fn',
    long_description=readme,
    version='0.1',
    packages=['pipe_fn'],
    url='https://github.com/Xython/pipe-fn',
    license='MIT',
    author='thautwarm',
    author_email='twshere@outlook.com',
    description='functional pipeline operation in Python',
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'],
    zip_safe=False
)
