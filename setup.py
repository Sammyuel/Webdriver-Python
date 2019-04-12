#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import io
import os
from distutils.core import setup
from setuptools import setup

def library_version():
    """
    Return a version of this python library
    """

    return 0

setup(
    name='python_webdriver',
    version=library_version(),
    description='Python client for Appium',
    long_description=io.open(os.path.join(os.path.dirname('__file__'), 'README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    keywords=[
        'appium',
        'selenium',
        'selenium 3',
        'python client',
        'mobile automation'
    ],
    author='Sam Lee',

    packages=[
        'core',
        'core.appium',
        'apps',
        'apps.fibetv',
        'apps.fibetv.pages',

    ],
    license='Apache 2.0',
    classifiers=[
        
    ],
)
