%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           notify-python
Version:        0.1.1
Release:        10%{?dist}
Summary:        Python bindings for libnotify

Group:          Development/Languages
# No version specified, just COPYING.
License:        LGPLv2+
Source0:        http://www.galago-project.org/files/releases/source/notify-python/notify-python-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel, pkgconfig, libnotify-devel, pygtk2-devel
BuildRequires:  gtk2-devel, dbus-devel, dbus-glib-devel

Requires:   libnotify >= 0.4.3
Requires:   desktop-notification-daemon

%global pypkgname pynotify

%description
Python bindings for libnotify

%prep
%setup -q

# WARNING - we touch src/pynotify.override in build because upstream did not rebuild pynotify.c
# from the input definitions, this forces pynotify.c to be regenerated, at some point this can be removed

%build
export PYTHON=%{__python}
%configure
touch src/pynotify.override
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
# remove unnecessary la file
rm $RPM_BUILD_ROOT/%{python_sitearch}/gtk-2.0/%{pypkgname}/_%{pypkgname}.la

 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS README ChangeLog 
%{python_sitearch}/gtk-2.0/%{pypkgname}
%{_datadir}/pygtk/2.0/defs/%{pypkgname}.defs
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Feb 25 2010 John Dennis <jdennis@redhat.com> - 0.1.1-10
- spec file clean-ups reported during RHEL-6 import review
  Related: #555835
  replace define with global
  remove URL tag, there is no project URL, it had been pointing to a page with package specification
  remove unnecessary use of CFLAGS
  export PYTHON environment variable pointing to interpreter
  install COPYING AUTHORS NEWS README ChangeLog into docdir

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.1.1-9
- Use bzipped upstream tarball.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  1 2009 John Dennis <jdennis@redhat.com> - 0.1.1-7
- change requires of notification-daemon to desktop-notification-daemon as per bug #500586

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.1-5
- Rebuild for Python 2.6

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1.1-4
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.1-3
- Autorebuild for GCC 4.3

* Fri Jan  4 2008  <jdennis@redhat.com> - 0.1.1-2
- Resolves bug# 427499: attach_to_status_icon not created
  force regeneration of pynotify.c

* Wed Jan  2 2008 John Dennis <jdennis@redhat.com> - 0.1.1-1
- upgrade to current upstream
- no longer remove package config file (notify-python.pc), resolves bug #427001

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.1.0-4
- rebuild for python 2.5

* Tue Aug 15 2006 Luke Macken <lmacken@redhat.com> - 0.1.0-3
- Add notify-python-0.1.0-attach_to_status_icon.patch to allow the attaching
  notifications to status icons.

* Thu Jul 20 2006 John Dennis <jdennis@redhat.com> - 0.1.0-2
- change use of python_sitelib to python_sitearch, add BuildRequires

* Wed Jul 19 2006 John Dennis <jdennis@redhat.com> - 0.1.0-1
- Initial build

