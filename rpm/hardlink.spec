Name:       hardlink
Summary:    replaces multiple copies of a file with hardlinks
Version:    0.3.2
Release:    2
Group:      Applications
License:    MIT
URL:        https://salsa.debian.org/jak/hardlink
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  make
# 2.34 integrates *a* hardlink, 2.37 has *this* hardlink
Conflicts: util-linux >= 2.34

%description
hardlink is a tool which replaces multiple copies of a file with hardlinks.
Inspiration came from http://code.google.com/p/hardlinkpy/, but no code has
been used.

This version was originally written in Python as well, but performance issues
on large data sets caused it to be rewritten in C.

This is also available in util-linux version 2.37 (2.34 ships a hardlink, but
not this hardlink), so cannot be installed alongside these versions.

%if "%{?vendor}" == "chum"
Type: console-application
PackagerName: nephros
DeveloperName: Julian Andres Klode
Categories:
 - Utility
Custom:
  PackagingRepo: https://github.com/sailfishos-chum/hardlink
  Repo: https://salsa.debian.org/jak/hardlink
%endif

%prep
%setup -q -n %{name}-%{version}/upstream

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -D -m 755 hardlink %{buildroot}/%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
