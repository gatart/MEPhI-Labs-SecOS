%define relabel_files() restorecon -R -v /usr/bin & restorecon -R -v /usr/lib/systemd/system

%define selinux_policy_version 3.14.3-80

Name:		swap-control
Version: 	1.0
Release:	1%{?dist}
Summary:	Program by Talamanov George MEPhI 2022
Group:		Testing
License:	GPL
URL:		https://github.com/gatart/MEPhI-Labs-SecOS
Source0:	%{name}-%{version}.tar.gz
Source1:	swap_control.pp
Source2:	swap_control.if
BuildRequires:	/bin/rm, /bin/mkdir, /bin/cp, /bin/sudo, selinux-policy, selinux-policy-devel
Requires:	/bin/bash
Requires(post): selinux-policy-base >= %{selinux_policy_version}, selinux-policy-targeted >= %{selinux_policy_version}, policycoreutils, policycoreutils-python-utils libselinux-utils
BuildArch:      noarch

%description
Service create new swap partion when swap file is over half.
Working in a custom domain policy

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/systemd/system
mkdir -p %{buildroot}%{_mandir}/man8
install -m 755 swap-control.sh %{buildroot}%{_bindir}
install -m 644 swap-control.service %{buildroot}/etc/systemd/system
install -m 644 swap-control.8.tar.gz %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -d %{buildroot}/etc/selinux/targeted/contexts/users
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/selinux/devel/include/contrib

%post
semodule -n -i %{_datadir}/selinux/packages/swap_control.pp
if /usr/sbin/selinuxenabled; then
    /usr/sbin/load_policy
    %relabel_files
fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r swap-control
    if /usr/sbin/selinuxenabled; then
       /usr/sbin/load_policy
       %relabel_files
    fi;
fi;
exit 0

%files
%{_bindir}/swap-control.sh
/etc/systemd/system/swap-control.service
%{_mandir}/man8/swap-control.8.tar.gz
%defattr(-, root, root, 0755)
%attr(0600, root, root)
%{_datadir}/selinux/packages/swap_control.pp
%{_datadir}/selinux/devel/include/contrib/swap_control.if

%changelog
* Mon May 23 2022 <labs>
- Added %{_bindir}/swap-control.spec
