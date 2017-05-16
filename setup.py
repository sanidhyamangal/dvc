import platform
from setuptools import setup, find_packages
from distutils.errors import DistutilsPlatformError
from dvc.main import VERSION

install_requires = [
    'altgraph==0.13',
    'appdirs==1.4.3',
    'backports.shutil-get-terminal-size==1.0.0',
    'boto==2.46.1',
    'cachetools==2.0.0',
    'configparser==3.5.0',
    'decorator==4.0.11',
    'dill==0.2.6',
    'enum34==1.1.6',
    'fasteners==0.14.1',
    'funcsigs==1.0.2',
    'future==0.16.0',
    'futures==3.0.5',
    'gapic-google-cloud-datastore-v1==0.15.3',
    'gapic-google-cloud-error-reporting-v1beta1==0.15.3',
    'gapic-google-cloud-logging-v2==0.91.3',
    'gapic-google-cloud-pubsub-v1==0.15.3',
    'gapic-google-cloud-spanner-admin-database-v1==0.15.3',
    'gapic-google-cloud-spanner-admin-instance-v1==0.15.3',
    'gapic-google-cloud-spanner-v1==0.15.3',
    'gapic-google-cloud-speech-v1beta1==0.15.3',
    'gapic-google-cloud-vision-v1==0.90.3',
    'google-auth==0.10.0',
    'google-auth-httplib2==0.0.2',
    'google-cloud==0.24.0',
    'google-cloud-bigquery==0.24.0',
    'google-cloud-bigtable==0.24.0',
    'google-cloud-core==0.24.0',
    'google-cloud-datastore==1.0.0',
    'google-cloud-dns==0.24.0',
    'google-cloud-error-reporting==0.24.0',
    'google-cloud-language==0.24.0',
    'google-cloud-logging==0.24.0',
    'google-cloud-monitoring==0.24.0',
    'google-cloud-pubsub==0.24.0',
    'google-cloud-resource-manager==0.24.0',
    'google-cloud-runtimeconfig==0.24.0',
    'google-cloud-spanner==0.24.0',
    'google-cloud-speech==0.24.0',
    'google-cloud-storage==1.0.0',
    'google-cloud-translate==0.24.0',
    'google-cloud-vision==0.24.0',
    'google-gax==0.15.8',
    'googleapis-common-protos==1.5.2',
    'grpc-google-iam-v1==0.11.1',
    'grpcio==1.2.1',
    'httplib2==0.10.3',
    'ipython==5.3.0',
    'ipython-genutils==0.2.0',
    'macholib==1.8',
    'mock==2.0.0',
    'modulegraph==0.14',
    'monotonic==1.3',
    'nose==1.3.7',
    'oauth2client==3.0.0',
    'packaging==16.8',
    'pathlib==1.0.1',
    'pathlib2==2.2.1',
    'pbr==3.0.0',
    'pexpect==4.2.1',
    'pickleshare==0.7.4',
    'ply==3.8',
    'prompt-toolkit==1.0.14',
    'proto-google-cloud-datastore-v1==0.90.3',
    'proto-google-cloud-error-reporting-v1beta1==0.15.3',
    'proto-google-cloud-logging-v2==0.91.3',
    'proto-google-cloud-pubsub-v1==0.15.3',
    'proto-google-cloud-spanner-admin-database-v1==0.15.3',
    'proto-google-cloud-spanner-admin-instance-v1==0.15.3',
    'proto-google-cloud-spanner-v1==0.15.3',
    'proto-google-cloud-speech-v1beta1==0.15.3',
    'proto-google-cloud-vision-v1==0.90.3',
    'protobuf==3.2.0',
    'ptyprocess==0.5.1',
    'pyasn1==0.2.3',
    'pyasn1-modules==0.0.8',
    'Pygments==2.2.0',
    'PyInstaller==3.2.1',
    'pyparsing==2.2.0',
    'requests==2.13.0',
    'rsa==3.4.2',
    'scandir==1.5',
    'simplegeneric==0.8.1',
    'six==1.10.0',
    'traitlets==4.3.2',
    'wcwidth==0.1.7',
]

if platform.system() == 'Darwin':
    install_requires.append('appnope==0.1.0')
    install_requires.append('py2app==0.12')

setup(
    name='dvc',
    version=VERSION,
    description='Data Version Control makes your data science projects reproducible and shareable.',
    author='Dmitry Petrov',
    author_email='dmitry@dataversioncontrol.com',
    url='https://github.com/dataversioncontrol/dvc.git',
    license='Apache License 2.0',
    install_requires=install_requires,
    keywords='data science, data version control, machine learning',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=['bin', 'tests', 'functests']),
    include_package_data=True,
    download_url='dataversioncontrol.com',
    entry_points={
        'console_scripts': ['dvc = dvc.main:main']
    },
    zip_safe=False
)