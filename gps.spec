Summary:	Ghost Port Scan
Name:		gps
Version:	0.7.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	http://gps.sourceforge.net/release/%{name}-%{version}.tar.gz
URL:		http://gps.sourceforge.net
BuildRequires:	libnet-devel
BuildRequires:	libcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ghost Port Scan is to provide administrators and pen-testers with a tool that
allow them to easily test firewalls and get information from a remote host.
GPS is a port scanner and a firewall rules disclosure (FWRD) tool, which uses
IP spoofing, ARP poisoning and some other stratagems in order to perform a
stealth and untrackable information collect.

%prep
%setup 	-q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gps
