Name:		pam_script
Version:	0.1.11
Release:	%mkrel 1
URL:		http://freshmeat.net/projects/pam_script
Source:		http://www.upfrontsystems.co.za/Members/izak/libpam-script_%{version}.tar.gz
Summary:	PAM module to executes a script at the start and end of a session
License:	GPL+
Group:		System/Libraries
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
