#
# Conditional build:
%bcond_without	tests	# tests

Summary:	Backport of the functools module from Python 3.2.3 to Python 2.7
Summary(pl.UTF-8):	Backport modułu functools z Pythona 3.2.3 do 2.7
Name:		python-functools32
%define	src_ver	3.2.3-2
Version:	%(echo %{src_ver} | tr - .)
%define	egg_ver	%(echo %{src_ver} | tr - _)
Release:	1
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/functools32/
Source0:	https://pypi.python.org/packages/c5/60/6ac26ad05857c601308d8fb9e87fa36d0ebf889423f47c3502ef034365db/functools32-%{src_ver}.tar.gz
# Source0-md5:	09f24ffd9af9f6cd0f63cb9f4e23d4b2
URL:		https://github.com/MiCHiLU/python-functools32
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a backport of the functools standard library module from
Python 3.2.3 for use on Python 2.7 and PyPy. It includes new features
lru_cache (Least-recently-used cache decorator).

%description -l pl.UTF-8
Ten pakiet zawiera backport modułu functools z biblioteki standardowej
Pythona 3.2.3, przeznaczony dla Pythona 2.7 oraz PyPy. Obejmuje nową
funkcję lru_cache (dekorator pamięci podręcznej ostatnio użytych
elementów).

%prep
%setup -q -n functools32-%{src_ver}

%build
%py_build

%if %{with tests}
%{__python} test_functools32.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE
%{py_sitescriptdir}/functools32
%{py_sitescriptdir}/functools32-%{egg_ver}-py*.egg-info
