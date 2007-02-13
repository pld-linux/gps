Summary:	Ghost Port Scan
Summary(pl.UTF-8):	Ghost Port Scan - ukrywający się skaner portów
Name:		gps
Version:	0.9.3
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://gps.sourceforge.net/release/%{name}-%{version}-FRC.tar.gz
# Source0-md5:	49b0727c0188f75ec2790fef817fa107
URL:		http://gps.sourceforge.net/
Patch0:		%{name}-libnet1.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnet1-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ghost Port Scan is to provide administrators and pen-testers with a
tool that allow them to easily test firewalls and get information from
a remote host. GPS is a port scanner and a firewall rules disclosure
(FWRD) tool, which uses IP spoofing, ARP poisoning and some other
stratagems in order to perform a stealth and untrackable information
collect.

%description -l pl.UTF-8
Ghost Port Scan to narzędzie dla administratorów i testerów do łatwego
testowania firewalli i wyciągania informacji o zdalnych hostach. GPS
jest skanerem portów i wykrywaczem regułek firewalla, używającym
fałszowania IP (IP spoofing) i ARP (ARP poisoning) oraz innych
sposobów, aby zgromadzić informacje w sposób niewidzialny i niemożliwy
do wyśledzenia.

%prep
%setup 	-q -n %{name}-%{version}-FRC
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gps
