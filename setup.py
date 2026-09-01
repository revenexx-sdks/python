import setuptools

long_description: str

with open("README.md", "r", encoding="utf-8") as readme_file_desc:
    long_description = readme_file_desc.read()

setuptools.setup(
  name = 'revenexx',
  packages = setuptools.find_packages(),
  version = '0.0.2',
  license='',
  description = 'Revenexx Python SDK.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Revenexx Platform',
  author_email = '',
  maintainer = 'Revenexx Platform',
  maintainer_email = '',
  url = 'https://revenexx.com',
  download_url='https://github.com/revenexx-sdks/python/archive/0.0.2.tar.gz',
  install_requires=[
    'requests',
    'pydantic>=2,<3',
  ],
  python_requires='>=3.9',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Environment :: Web Environment',
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
  ],
)
