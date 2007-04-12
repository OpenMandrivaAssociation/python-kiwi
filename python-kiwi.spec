%define oname kiwi
%define name python-kiwi
%define version 1.9.13
%define release %mkrel 1

Summary: A framework and a set of enhanced widgets based on PyGTK
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/kiwi/%{oname}-%{version}.tar.bz2
License: LGPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://www.async.com.br/projects/
BuildRequires: pygtk2.0-devel
Requires: pygtk2.0-libglade

%description

kiwi offers a set of enhanced widgets for
Python based on PyGTK. It also includes a framework designed to make
creating Python applications using PyGTK and libglade much
simpler.


%prep
%setup -q -n %oname-%version

%build
python setup.py build

%install
rm -rf %buildroot installed-docs
python setup.py install --root=$RPM_BUILD_ROOT
%find_lang %oname

mv %buildroot%_datadir/doc/%oname installed-docs
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %oname.lang
%defattr(-,root,root)
%doc installed-docs/*
%_bindir/*
%py_puresitedir/*
%_datadir/gazpacho/
%_datadir/%oname


