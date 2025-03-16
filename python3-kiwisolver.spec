Summary:	Fast implementation of the Cassowary constraint solver
Summary(pl.UTF-8):	Szybka implementacja rozwiązywania układu ograniczeń metodą Cassowary
Name:		python3-kiwisolver
Version:	1.4.8
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/kiwisolver/
Source0:	https://files.pythonhosted.org/packages/source/k/kiwisolver/kiwisolver-%{version}.tar.gz
# Source0-md5:	2eb55aab42272292a732411bb6c79dee
URL:		https://github.com/nucleic/kiwi
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	python3-cppy >= 1.3.0
BuildRequires:	python3-devel >= 1:3.10
BuildRequires:	python3-setuptools >= 1:61.2
BuildRequires:	python3-setuptools_scm >= 3.4.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.10
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

%prep
%setup -q -n kiwisolver-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst releasenotes.rst
%dir %{py3_sitedir}/kiwisolver
%attr(755,root,root) %{py3_sitedir}/kiwisolver/_cext.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/kiwisolver/_cext.pyi
%attr(755,root,root) %{py3_sitedir}/kiwisolver/*.py
%attr(755,root,root) %{py3_sitedir}/kiwisolver/py.typed
%attr(755,root,root) %{py3_sitedir}/kiwisolver/__pycache__
%{py3_sitedir}/kiwisolver-%{version}-py*.egg-info
