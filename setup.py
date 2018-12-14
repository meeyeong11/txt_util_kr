#-*- coding:utf-8 -*-
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "txt_util_kr",
    version = "0.0.1",
    author = "Meeyeong Im",
    author_email = "meeyeong1211@gmail.com",
    description = (u"한국어 파일 입출력, 코사인 유사도, 절대 경로, json 로딩, kkma 태거를 사용한 한국어 형태소 분석, 시간 프린트 하기 등 util 파일들"),
    url = "https://github.com/meeyeong11/txt_util_kr/",
    install_requires=['konlpy','numpy'],
    python_requires=">=2.6",
    license = "BSD",
    keywords = "some txt parsing util",
    
    packages=['txt_util_kr'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

