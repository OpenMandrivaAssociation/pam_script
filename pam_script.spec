Name:		pam_script
Version:	0.1.12
Release:	%mkrel 4
URL:		http://freshmeat.net/projects/pam_script
Source:		http://www.upfrontsystems.co.za/Members/izak/libpam-script_%{version}.tar.gz
Summary:	PAM module to executes a script at the start and end of a session
License:	GPL+
Group:		System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pam-devel
%description
pam_script is a PAM that executes a script at the start and end of a
session. Any PAM-aware application can use the module to perform
arbitrary operations. It was originally written for cleaning up when a
user logs out.

%prep
%setup -q -n libpam-script-%{version}

%build
%{make}

%install
%{__rm} -Rf %{buildroot}
%{__make} DESTDIR=%{buildroot} plibdir=/%{_lib}/security install
%{__install} -d %{buildroot}%{_mandir}/man5
%{__install} -m0644 pam_script.5 %{buildroot}%{_mandir}/man5

%files
%doc README CREDITS examples
/%{_lib}/security/pam_script.so
%{_mandir}/man5/pam_script.5*


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.12-4mdv2011.0
+ Revision: 614471
- the mass rebuild of 2010.1 packages

* Tue Nov 10 2009 Michael Scherer <misc@mandriva.org> 0.1.12-3mdv2010.1
+ Revision: 463858
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Oct 13 2008 Nicolas Vigier <nvigier@mandriva.com> 0.1.12-1mdv2009.1
+ Revision: 293370
- new version 0.1.12

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.1.11-3mdv2009.0
+ Revision: 254986
- rebuild
- fix no-buildroot-tag

* Tue Dec 04 2007 Nicolas Vigier <nvigier@mandriva.com> 0.1.11-1mdv2008.1
+ Revision: 115405
- import pam_script


