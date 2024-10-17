%define oname kiwi

# There are no binary files in package itself,
# but we need to place files to arch-specific glade3 libdir
%define debug_package %{nil}

Summary: A framework and a set of enhanced widgets based on PyGTK
Name:    python-kiwi
Version: 1.9.41.post1
Release: 1
Source0: https://pypi.python.org/packages/source/k/kiwi-gtk/kiwi-gtk-%{version}.tar.gz
License: LGPLv2+
Group:   Development/Python
Url:     https://www.async.com.br/projects/kiwi/
BuildRequires: pkgconfig(python2)
BuildRequires: pygtk2.0-devel
BuildRequires: python2-setuptools
Requires: pygtk2.0-libglade

%description
kiwi offers a set of enhanced widgets for
Python based on PyGTK. It also includes a framework designed to make
creating Python applications using PyGTK and libglade much
simpler.

%package docs
Group:	Development/Python
Summary: Documentation related to python-kiwi
Requires: %{name} = %{EVRD}

%description docs
This package contains documentation that contains APIs and related materials,
useful for reference when writing software using Kiwi.


%prep
%setup -q -n %{oname}-gtk-%{version}
sed -i -e 's|share/doc/kiwi|share/doc/%{name}-%{version}|' setup.py

rm requirements.txt
touch requirements.txt
rm kiwi_gtk.egg-info/requires.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
rm -rf %{buildroot}%{_defaultdocdir}
%if %{_lib} != lib
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/glade3 %{buildroot}%{_libdir}
%endif

%find_lang %{oname}

%clean

%files -f %{oname}.lang
%doc AUTHORS COPYING README NEWS
%{_bindir}/*
%{py2_puresitedir}/*.egg-info
#gw this dir is arch-dependant:
%{_libdir}/glade3/*
%{_datadir}/glade3/*
%{py2_puresitedir}/kiwi

%files docs
%doc COPYING doc/* examples
