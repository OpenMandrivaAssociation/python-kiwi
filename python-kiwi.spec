%define oname kiwi
%define name python-kiwi
%define version 1.9.29
%define release %mkrel 1

Summary: A framework and a set of enhanced widgets based on PyGTK
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.gnome.org/sources/%{oname}/1.9/%{oname}-%{version}.tar.bz2
License: LGPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://www.async.com.br/projects/kiwi/
BuildRequires: pygtk2.0-devel
Requires: pygtk2.0-libglade

%description
kiwi offers a set of enhanced widgets for
Python based on PyGTK. It also includes a framework designed to make
creating Python applications using PyGTK and libglade much
simpler.

%package docs
Group:	Development/Python
Summary: Documentation related to python-kiwi
Requires: %{name} = %{version}-%{release}

%description docs
This package contains documentation that contains APIs and related materials,
useful for reference when writing software using Kiwi.


%prep
%setup -q -n %oname-%version
sed -i -e 's|share/doc/kiwi|share/doc/%{name}-%{version}|' setup.py

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}

%find_lang %oname

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %oname.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS
%{_bindir}/*
%{_libdir}/python*/site-packages/*.egg-info
%{_libdir}/glade3/*
%{_datadir}/glade3/*
%_datadir/%oname
%{python_sitelib}/kiwi

%files docs
%defattr(-,root,root,-)
%doc COPYING doc/* examples

