#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-prettytable
Version  : 3.4.0
Release  : 84
URL      : https://files.pythonhosted.org/packages/63/42/b8b24cfe616a8217515011fc54ed37b45077cd4467230b3a0132166696a1/prettytable-3.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/63/42/b8b24cfe616a8217515011fc54ed37b45077cd4467230b3a0132166696a1/prettytable-3.4.0.tar.gz
Summary  : A simple Python library for easily displaying tabular data in a visually appealing ASCII table format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-prettytable-license = %{version}-%{release}
Requires: pypi-prettytable-python = %{version}-%{release}
Requires: pypi-prettytable-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(wcwidth)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# PrettyTable
[![Jazzband](https://jazzband.co/static/img/badge.svg)](https://jazzband.co/)
[![PyPI version](https://img.shields.io/pypi/v/prettytable.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/prettytable/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/prettytable.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/prettytable/)
[![PyPI downloads](https://img.shields.io/pypi/dm/prettytable.svg)](https://pypistats.org/packages/prettytable)
[![GitHub Actions status](https://github.com/jazzband/prettytable/workflows/Test/badge.svg)](https://github.com/jazzband/prettytable/actions)
[![codecov](https://codecov.io/gh/jazzband/prettytable/branch/master/graph/badge.svg)](https://codecov.io/gh/jazzband/prettytable)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

%package license
Summary: license components for the pypi-prettytable package.
Group: Default

%description license
license components for the pypi-prettytable package.


%package python
Summary: python components for the pypi-prettytable package.
Group: Default
Requires: pypi-prettytable-python3 = %{version}-%{release}

%description python
python components for the pypi-prettytable package.


%package python3
Summary: python3 components for the pypi-prettytable package.
Group: Default
Requires: python3-core
Provides: pypi(prettytable)
Requires: pypi(wcwidth)

%description python3
python3 components for the pypi-prettytable package.


%prep
%setup -q -n prettytable-3.4.0
cd %{_builddir}/prettytable-3.4.0
pushd ..
cp -a prettytable-3.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661445099
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-prettytable
cp %{_builddir}/prettytable-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-prettytable/5c51c5dac61ba4be822af5e4dbfbdc9aaac1a2b1 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-prettytable/5c51c5dac61ba4be822af5e4dbfbdc9aaac1a2b1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
