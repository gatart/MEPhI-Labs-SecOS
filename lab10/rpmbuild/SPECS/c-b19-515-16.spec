Name:          c-b19-515-16
Version:       1.0
Release:       1%{?dist}
Summary:       Программа студента Talamanov George группы B19-515
Group:         Testing
License:       GPL
URL:           https://github.com/gatart/my-c-rpm-package
Source:       %{name}-%{version}.tar.gz
BuildRequires: gcc

%global debug_package %{nil}

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-b19-515-16 c-b19-515-16.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b19-515-16 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/noarch/b19-515-16-1.0-1.el8.noarch.rpm --force

%files
%{_bindir}/c-b19-515-16

%changelog
* Thu Oct 16 2012 Talamanov
- Added %{_bindir}/c-b19-515-16
