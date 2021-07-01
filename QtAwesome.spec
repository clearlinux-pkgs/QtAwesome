#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : QtAwesome
Version  : 0.5.8
Release  : 32
URL      : https://files.pythonhosted.org/packages/b5/a0/d5d10e6a51dedd547eb9af0e224eed07f492ffa21030e6b89aed7cbb1e6a/QtAwesome-0.5.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/a0/d5d10e6a51dedd547eb9af0e224eed07f492ffa21030e6b89aed7cbb1e6a/QtAwesome-0.5.8.tar.gz
Summary  : FontAwesome icons in PyQt and PySide applications
Group    : Development/Tools
License  : MIT
Requires: QtAwesome-license = %{version}-%{release}
Requires: QtAwesome-python = %{version}-%{release}
Requires: QtAwesome-python3 = %{version}-%{release}
Requires: QtPy
Requires: six
BuildRequires : QtPy
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
# QtAwesome
[![license](https://img.shields.io/pypi/l/qtawesome.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/qtawesome.svg)](https://pypi.org/project/qtawesome/)
[![conda version](https://img.shields.io/conda/vn/conda-forge/qtawesome.svg)](https://www.anaconda.com/download/)
[![download count](https://img.shields.io/conda/d/conda-forge/qtawesome.svg)](https://www.anaconda.com/download/)
[![OpenCollective Backers](https://opencollective.com/spyder/backers/badge.svg?color=blue)](#backers)
[![Join the chat at https://gitter.im/spyder-ide/public](https://badges.gitter.im/spyder-ide/spyder.svg)](https://gitter.im/spyder-ide/public)<br>
[![PyPI status](https://img.shields.io/pypi/status/qtawesome.svg)](https://github.com/spyder-ide/qtawesome)
[![Appveyor build status](https://ci.appveyor.com/api/projects/status/un8vnw4628cl6qfu?svg=true)](https://ci.appveyor.com/project/spyder-ide/qtawesome)
[![CircleCI build status](https://circleci.com/gh/spyder-ide/qtawesome/tree/master.svg?style=shield)](https://circleci.com/gh/spyder-ide/qtawesome/tree/master)
[![Documentation Status](https://readthedocs.org/projects/qtawesome/badge/?version=latest)](http://qtawesome.readthedocs.org/en/latest/?badge=latest)

%package license
Summary: license components for the QtAwesome package.
Group: Default

%description license
license components for the QtAwesome package.


%package python
Summary: python components for the QtAwesome package.
Group: Default
Requires: QtAwesome-python3 = %{version}-%{release}
Provides: qtawesome-python

%description python
python components for the QtAwesome package.


%package python3
Summary: python3 components for the QtAwesome package.
Group: Default
Requires: python3-core
Provides: pypi(qtawesome)
Requires: pypi(qtpy)
Requires: pypi(six)

%description python3
python3 components for the QtAwesome package.


%prep
%setup -q -n QtAwesome-0.5.8
cd %{_builddir}/QtAwesome-0.5.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583522809
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/QtAwesome
cp %{_builddir}/QtAwesome-0.5.8/LICENSE %{buildroot}/usr/share/package-licenses/QtAwesome/cde8ccad1073a4360ae14180a7cf4bc7e28980e9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/QtAwesome/cde8ccad1073a4360ae14180a7cf4bc7e28980e9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
