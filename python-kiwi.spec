%define oname kiwi
%define name python-kiwi
%define version 1.9.29
%define release %mkrel 2

Summary: A framework and a set of enhanced widgets based on PyGTK
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.gnome.org/sources/%{oname}/1.9/%{oname}-%{version}.tar.xz
License: LGPLv2+
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}
%if %_lib != lib
mkdir -p %buildroot%_libdir
mv %buildroot%_prefix/lib/glade3 %buildroot%_libdir
%endif

%find_lang %oname

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %oname.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS
%{_bindir}/*
%{py_puresitedir}/*.egg-info
#gw this dir is arch-dependant:
%{_libdir}/glade3/*
%{_datadir}/glade3/*
%_datadir/%oname
%{py_puresitedir}/kiwi

%files docs
%defattr(-,root,root,-)
%doc COPYING doc/* examples



%changelog
* Sat Jul 30 2011 Götz Waschk <waschk@mandriva.org> 1.9.29-2mdv2012.0
+ Revision: 692405
- no more noarch for glade3 module
- xz tarball
- fix license
- fix build on 64 bit

* Fri Jul 29 2011 Leonardo Coelho <leonardoc@mandriva.com> 1.9.29-1
+ Revision: 692288
- bump new version

* Wed Apr 06 2011 Leonardo Coelho <leonardoc@mandriva.com> 1.9.27-2
+ Revision: 651280
- Update to version 1.9.27

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 1.9.26-2mdv2011.0
+ Revision: 592832
- rebuild for new python 2.7

* Wed Jul 15 2009 Götz Waschk <waschk@mandriva.org> 1.9.26-1mdv2011.0
+ Revision: 396180
- new version
- update file list

* Fri Apr 24 2009 Götz Waschk <waschk@mandriva.org> 1.9.25-1mdv2010.0
+ Revision: 368992
- new version

* Wed Jan 28 2009 Götz Waschk <waschk@mandriva.org> 1.9.24-1mdv2009.1
+ Revision: 334931
- update to new version 1.9.24

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 1.9.23-2mdv2009.1
+ Revision: 320621
- rebuild for new python

* Thu Sep 11 2008 Götz Waschk <waschk@mandriva.org> 1.9.23-1mdv2009.0
+ Revision: 283850
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.9.22-2mdv2009.0
+ Revision: 269031
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 02 2008 Götz Waschk <waschk@mandriva.org> 1.9.22-1mdv2009.0
+ Revision: 214372
- new version

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 1.9.21-1mdv2009.0
+ Revision: 192412
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description

* Thu Jan 31 2008 Götz Waschk <waschk@mandriva.org> 1.9.20-1mdv2008.1
+ Revision: 160769
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 09 2007 Götz Waschk <waschk@mandriva.org> 1.9.19-1mdv2008.1
+ Revision: 107180
- new version

* Sat Sep 15 2007 Götz Waschk <waschk@mandriva.org> 1.9.18-1mdv2008.0
+ Revision: 85941
- new version

* Thu Aug 30 2007 Götz Waschk <waschk@mandriva.org> 1.9.17-1mdv2008.0
+ Revision: 75141
- new version

* Mon Jul 16 2007 Götz Waschk <waschk@mandriva.org> 1.9.16-1mdv2008.0
+ Revision: 52578
- new version

* Wed May 23 2007 Götz Waschk <waschk@mandriva.org> 1.9.15-1mdv2008.0
+ Revision: 30144
- new version


* Thu Feb 01 2007 Götz Waschk <waschk@mandriva.org> 1.9.13-1mdv2007.1
+ Revision: 115833
- new version

* Mon Jan 29 2007 Götz Waschk <waschk@mandriva.org> 1.9.12-1mdv2007.1
+ Revision: 115207
- new version

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 1.9.11-2mdv2007.1
+ Revision: 88215
- update file list
- Import python-kiwi

* Tue Oct 10 2006 Götz Waschk <waschk@mandriva.org> 1.9.11-1mdv2007.1
- New version 1.9.11

* Sat Sep 16 2006 Götz Waschk <waschk@mandriva.org> 1.9.10-1mdv2007.0
- New version 1.9.10

* Sat Aug 26 2006 Götz Waschk <waschk@mandriva.org> 1.9.9-1mdv2007.0
- update file list
- new source URL
- New release 1.9.9

* Fri Jul 21 2006 Götz Waschk <waschk@mandriva.org> 1.9.8-1mdv2007.0
- Rebuild

* Sat May 06 2006 Götz Waschk <waschk@mandriva.org> 1.9.8-2mdk
- fix buildrequires

* Fri May 05 2006 Götz Waschk <waschk@mandriva.org> 1.9.8-1mdk
- initial package

