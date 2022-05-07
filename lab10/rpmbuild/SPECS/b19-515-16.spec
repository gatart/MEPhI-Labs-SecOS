Name:          b19-515-16
Version:       1.0
Release:       1%{?dist}
Summary:       Программа студента Talamanov George группы B19-515
Group:         Testing
License:       GPL
URL:           https://github.com/gatart/my-rpm-package
Source0:       %{name}-%{version}.tar.gz
BuildRequires: /bin/rm, /bin/mkdir, /bin/cp
Requires:      /bin/bash, /usr/bin/date
BuildArch:     noarch

%description
A test package

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 b19-515-16 %{buildroot}%{_bindir}

%files
%{_bindir}/b19-515-16

%changelog
* Thu Oct 16 2012 Talamanov
- Added %{_bindir}/b19-515-16
