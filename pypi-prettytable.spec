#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : pypi-prettytable
Version  : 3.16.0
Release  : 105
URL      : https://files.pythonhosted.org/packages/99/b1/85e18ac92afd08c533603e3393977b6bc1443043115a47bb094f3b98f94f/prettytable-3.16.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/99/b1/85e18ac92afd08c533603e3393977b6bc1443043115a47bb094f3b98f94f/prettytable-3.16.0.tar.gz
Summary  : A simple Python library for easily displaying tabular data in a visually appealing ASCII table format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-prettytable-license = %{version}-%{release}
Requires: pypi-prettytable-python = %{version}-%{release}
Requires: pypi-prettytable-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# PrettyTable
[![PyPI version](https://img.shields.io/pypi/v/prettytable.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/prettytable/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/prettytable.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/prettytable/)
[![PyPI downloads](https://img.shields.io/pypi/dm/prettytable.svg)](https://pypistats.org/packages/prettytable)
[![GitHub Actions status](https://github.com/prettytable/prettytable/workflows/Test/badge.svg)](https://github.com/prettytable/prettytable/actions)
[![Codecov](https://codecov.io/gh/prettytable/prettytable/branch/main/graph/badge.svg)](https://codecov.io/gh/prettytable/prettytable)
[![Licence](https://img.shields.io/github/license/prettytable/prettytable.svg)](LICENSE)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)
[![Tidelift](https://tidelift.com/badges/package/pypi/prettytable)](https://tidelift.com/subscription/pkg/pypi-prettytable?utm_source=pypi-prettytable&utm_medium=badge)

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
%setup -q -n prettytable-3.16.0
cd %{_builddir}/prettytable-3.16.0
pushd ..
cp -a prettytable-3.16.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742848074
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-prettytable
cp %{_builddir}/prettytable-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-prettytable/5c51c5dac61ba4be822af5e4dbfbdc9aaac1a2b1 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
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
