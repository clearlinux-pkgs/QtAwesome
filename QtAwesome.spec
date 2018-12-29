#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : QtAwesome
Version  : 0.4.4
Release  : 12
URL      : https://pypi.python.org/packages/28/be/cadd6e06a6219f31d6153eb43e9f17dadb7c968835b10180a7bca39ae8ab/QtAwesome-0.4.4.tar.gz
Source0  : https://pypi.python.org/packages/28/be/cadd6e06a6219f31d6153eb43e9f17dadb7c968835b10180a7bca39ae8ab/QtAwesome-0.4.4.tar.gz
Summary  : FontAwesome icons in PyQt and PySide applications
Group    : Development/Tools
License  : MIT
Requires: QtAwesome-python3
Requires: QtAwesome-python
Requires: QtPy
Requires: six
BuildRequires : QtPy
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
# QtAwesome
## Build status
[![Travis](https://travis-ci.org/spyder-ide/qtawesome.svg?branch=master)](https://travis-ci.org/spyder-ide/qtawesome)
[![Appveyor](https://ci.appveyor.com/api/projects/status/un8vnw4628cl6qfu?svg=true)](https://ci.appveyor.com/project/spyder-ide/qtawesome)
[![CircleCI](https://circleci.com/gh/spyder-ide/qtawesome/tree/master.svg?style=shield)](https://circleci.com/gh/spyder-ide/qtawesome/tree/master)
[![Quantified Code](https://www.quantifiedcode.com/api/v1/project/5b42f6edb1ac4465b0e891a4b0144bd8/badge.svg)](https://www.quantifiedcode.com/app/project/5b42f6edb1ac4465b0e891a4b0144bd8)
[![Scrutinizer](https://scrutinizer-ci.com/g/spyder-ide/qtawesome/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/spyder-ide/qtawesome/?branch=master)

%package python
Summary: python components for the QtAwesome package.
Group: Default
Requires: QtAwesome-python3
Provides: qtawesome-python

%description python
python components for the QtAwesome package.


%package python3
Summary: python3 components for the QtAwesome package.
Group: Default
Requires: python3-core

%description python3
python3 components for the QtAwesome package.


%prep
%setup -q -n QtAwesome-0.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515337144
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
