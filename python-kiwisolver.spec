#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Fast implementation of the Cassowary constraint solver
Summary(pl.UTF-8):	Szybka implementacja rozwiązywania układu ograniczeń metodą Cassowary
Name:		python-kiwisolver
Version:	1.1.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/kiwisolver/
Source0:	https://files.pythonhosted.org/packages/source/k/kiwisolver/kiwisolver-%{version}.tar.gz
# Source0-md5:	fc8a614367f7ba0d34a02fd08c535afc
URL:		https://github.com/nucleic/kiwi
BuildRequires:	libstdc++-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kiwi is an efficient C++ implementation of the Cassowary constraint
solving algorithm. Kiwi is an implementation of the algorithm based on
the seminal Cassowary paper. It is *not* a refactoring of the original
C++ solver. Kiwi has been designed from the ground up to be
lightweight and fast. Kiwi ranges from 10x to 500x faster than the
original Cassowary solver with typical use cases gaining a 40x
improvement. Memory savings are consistently > 5x.

In addition to the C++ solver, Kiwi ships with hand-rolled Python
bindings.

%description -l pl.UTF-8
Kiwi to napisana w C++, wydajna implementacja algorytmu rozwiązywania
układu ograniczeń Cassowary. Kiwi to implementacja oparta na
nowatorskim dokumencie Cassowary, nie refaktor oryginalnej
implementacji w C++. Kiwi zostało od początku napisane z myślą o
lekkości i szybkości; jest od 10x do 500x szybsze od oryginalnej
implementacji, w typowych przypadkach osiągając 40-krotne
przyspieszenie. Oszczędność pamięci jest pięciokrotna.

Poza kodem w C++ Kiwi zawiera ręcznie napisane wiązania Pythona.

%package -n python3-kiwisolver
Summary:	Fast implementation of the Cassowary constraint solver
Summary(pl.UTF-8):	Szybka implementacja rozwiązywania układu ograniczeń metodą Cassowary
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-kiwisolver
Kiwi is an efficient C++ implementation of the Cassowary constraint
solving algorithm. Kiwi is an implementation of the algorithm based on
the seminal Cassowary paper. It is *not* a refactoring of the original
C++ solver. Kiwi has been designed from the ground up to be
lightweight and fast. Kiwi ranges from 10x to 500x faster than the
original Cassowary solver with typical use cases gaining a 40x
improvement. Memory savings are consistently > 5x.

In addition to the C++ solver, Kiwi ships with hand-rolled Python
bindings.

%description -n python3-kiwisolver -l pl.UTF-8
Kiwi to napisana w C++, wydajna implementacja algorytmu rozwiązywania
układu ograniczeń Cassowary. Kiwi to implementacja oparta na
nowatorskim dokumencie Cassowary, nie refaktor oryginalnej
implementacji w C++. Kiwi zostało od początku napisane z myślą o
lekkości i szybkości; jest od 10x do 500x szybsze od oryginalnej
implementacji, w typowych przypadkach osiągając 40-krotne
przyspieszenie. Oszczędność pamięci jest pięciokrotna.

Poza kodem w C++ Kiwi zawiera ręcznie napisane wiązania Pythona.

%prep
%setup -q -n kiwisolver-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst releasenotes.rst
%attr(755,root,root) %{py_sitedir}/kiwisolver.so
%{py_sitedir}/kiwisolver-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-kiwisolver
%defattr(644,root,root,755)
%doc README.rst releasenotes.rst
%attr(755,root,root) %{py3_sitedir}/kiwisolver.cpython-*.so
%{py3_sitedir}/kiwisolver-%{version}-py*.egg-info
%endif
