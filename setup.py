from setuptools import setup, find_packages

requirements = list()
with open('requirements.txt', 'r', encoding='utf-16') as f:
    for r in f.readlines():
        requirements.append(r.strip())
print(requirements)

with open('README.md', 'r') as readme:
    long_description = readme.read()

classifiers=[
    'Development Status :: 1 - Beta',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]

setup(
    name="Firewall_RuleBase_Audit",
    version="1.0.0",
    description="IPv4 Policy Audit",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Andrey Kolihanov',
    python_requires="~=3.8",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    license='GNU General Public License v3 (GPLv3)',
    classifiers=classifiers
)