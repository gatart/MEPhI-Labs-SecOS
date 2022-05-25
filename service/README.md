# Cервис управления файловым пространством swap
## Выполнил Таламанов Георгий, Б19-515
## Тестовое задание

Разработать сервис, который выполняет мониторинг состояния файла подкачки каждые 30 секунд. 
Если swap заполнен более чем наполовину, создаёт ещё один swap-файл, 
который удваивает существующее пространство swap.

## Создание RPM-пакета из сценария Bash

```
[labs@localhost ~]$ cd
[labs@localhost ~]$ rpmdev-setuptree
[labs@localhost ~]$ cd ~/rpmbuild/SOURCES/
[labs@localhost SOURCES]$ mkdir swap-control-1.0/
[labs@localhost SOURCES]$ cd swap-control-1.0/
[labs@localhost swap-control-1.0]$ nano swap-control.service
[labs@localhost swap-control-1.0]$ nano swap-control
[labs@localhost swap-control-1.0]$ chmod +x nano swap-control
[labs@localhost swap-control-1.0]$ nano swap-control.8
[labs@localhost swap-control-1.0]$ gzip -k swap-control.8
[labs@localhost swap-control-1.0]$ cd ~/rpmbuild/SOURCES/
[labs@localhost SOURCES]$ tar -cvzf swap-control-1.0.tar.gz swap-control-1.0/
swap-control-1.0/
swap-control-1.0/swap-control.service
swap-control-1.0/swap-control.8
swap-control-1.0/swap-control.8.tar.gz
swap-control-1.0/swap-control
[labs@localhost SOURCES]$ cd ../SPECS/
[labs@localhost SPECS]$ nano swap-control.spec 
[labs@localhost SPECS]$ rpmbuild -ba swap-control.spec
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.RULIoS
+ umask 022
+ cd /home/labs/rpmbuild/BUILD
+ cd /home/labs/rpmbuild/BUILD
+ rm -rf swap-control-1.0
+ /usr/bin/gzip -dc /home/labs/rpmbuild/SOURCES/swap-control-1.0.tar.gz
+ /usr/bin/tar -xof -
+ STATUS=0
+ '[' 0 -ne 0 ']'
+ cd swap-control-1.0
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.6imK3S
+ umask 022
+ cd /home/labs/rpmbuild/BUILD
+ '[' /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64 '!=' / ']'
+ rm -rf /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64
++ dirname /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64
+ mkdir -p /home/labs/rpmbuild/BUILDROOT
+ mkdir /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64
+ cd swap-control-1.0
+ mkdir -p /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/usr/bin
+ mkdir -p /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/etc/systemd/system
+ mkdir -p /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/usr/share/man/man8
+ install -m 755 swap-control /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/usr/bin
+ install -m 644 swap-control.service /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/etc/systemd/system
+ install -m 644 swap-control.8.tar.gz /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/usr/share/man/man8
+ install -d /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -d /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib
+ install -d /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/etc/selinux/targeted/contexts/users
+ install -m 644 /home/labs/rpmbuild/SOURCES/swap_control.pp /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/labs/rpmbuild/SOURCES/swap_control.if /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib
+ '[' noarch = noarch ']'
+ case "${QA_CHECK_RPATHS:-}" in
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-ldconfig
/sbin/ldconfig: Warning: ignoring configuration file that cannot be opened: /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64/etc/ld.so.conf: No such file or directory
+ /usr/lib/rpm/brp-compress
+ /usr/lib/rpm/brp-strip /usr/bin/strip
+ /usr/lib/rpm/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
+ /usr/lib/rpm/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile '' 1
+ /usr/lib/rpm/brp-python-hardlink
+ PYTHON3=/usr/libexec/platform-python
+ /usr/lib/rpm/redhat/brp-mangle-shebangs
Processing files: swap-control-1.0-1.el8.noarch
Provides: swap-control = 1.0-1.el8
Requires(interp): /bin/sh /bin/sh
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires(post): /bin/sh libselinux-utils policycoreutils policycoreutils-python selinux-policy-base >= 3.14.3-80 selinux-policy-targeted >= 3.14.3-80
Requires(postun): /bin/sh
Requires: /bin/bash
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64
Wrote: /home/labs/rpmbuild/SRPMS/swap-control-1.0-1.el8.src.rpm
Wrote: /home/labs/rpmbuild/RPMS/noarch/swap-control-1.0-1.el8.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.wGq3gR
+ umask 022
+ cd /home/labs/rpmbuild/BUILD
+ cd swap-control-1.0
+ /usr/bin/rm -rf /home/labs/rpmbuild/BUILDROOT/swap-control-1.0-1.el8.x86_64
+ exit 0
```

## Настройка политики SELinux

```
[labs@localhost SOURCES]$ sepolicy generate --init swap-control

***************************************
Warning /home/labs/rpmbuild/SOURCES/swap-control does not exist
***************************************

Created the following files:
/home/labs/rpmbuild/SOURCES/swap_control.te # Type Enforcement file
/home/labs/rpmbuild/SOURCES/swap_control.if # Interface file
/home/labs/rpmbuild/SOURCES/swap_control.fc # File Contexts file
/home/labs/rpmbuild/SOURCES/swap_control_selinux.spec # Spec file
/home/labs/rpmbuild/SOURCES/swap_control.sh # Setup Script
[labs@localhost SOURCES]$ nano swap_control.te 
[labs@localhost SOURCES]$ nano swap_control.if 
[labs@localhost SOURCES]$ nano swap_control.fc 
[labs@localhost SOURCES]$ sudo ./swap_control.sh 
Building and Loading Policy
+ make -f /usr/share/selinux/devel/Makefile swap_control.pp
Compiling targeted swap_control module
Creating targeted swap_control.pp policy package
rm tmp/swap_control.mod tmp/swap_control.mod.fc
+ /usr/sbin/semodule -i swap_control.pp
+ sepolicy manpage -p . -d swap_control_t
./swap_control_selinux.8
+ /sbin/restorecon -F -R -v /home/labs/rpmbuild/SOURCES/swap-control
++ pwd
+ pwd=/home/labs/rpmbuild/SOURCES
+ rpmbuild --define '_sourcedir /home/labs/rpmbuild/SOURCES' --define '_specdir /home/labs/rpmbuild/SOURCES' --define '_builddir /home/labs/rpmbuild/SOURCES' --define '_srcrpmdir /home/labs/rpmbuild/SOURCES' --define '_rpmdir /home/labs/rpmbuild/SOURCES' --define '_buildrootdir /home/labs/rpmbuild/SOURCES/.build' -ba swap_control_selinux.spec
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.NDQWYm
+ umask 022
+ cd /home/labs/rpmbuild/SOURCES
+ '[' /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64 '!=' / ']'
+ rm -rf /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64
++ dirname /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64
+ mkdir -p /home/labs/rpmbuild/SOURCES/.build
+ mkdir /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64
+ install -d /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/labs/rpmbuild/SOURCES/swap_control.pp /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -d /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib
+ install -m 644 /home/labs/rpmbuild/SOURCES/swap_control.if /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib/
+ install -d /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64/usr/share/man/man8/
+ install -m 644 /home/labs/rpmbuild/SOURCES/swap_control_selinux.8 /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64/usr/share/man/man8/swap_control_selinux.8
+ install -d /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64/etc/selinux/targeted/contexts/users/
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-ldconfig
/sbin/ldconfig: Warning: ignoring configuration file that cannot be opened: /etc/ld.so.conf: No such file or directory
+ /usr/lib/rpm/brp-compress
+ /usr/lib/rpm/brp-strip /usr/bin/strip
+ /usr/lib/rpm/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
+ /usr/lib/rpm/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile '' 1
+ /usr/lib/rpm/brp-python-hardlink
+ PYTHON3=/usr/libexec/platform-python
+ /usr/lib/rpm/redhat/brp-mangle-shebangs
Processing files: swap_control_selinux-1.0-1.el8.noarch
Provides: swap_control_selinux = 1.0-1.el8
Requires(interp): /bin/sh /bin/sh
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires(post): /bin/sh policycoreutils selinux-policy-base >= 3.14.3-80
Requires(postun): /bin/sh policycoreutils
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64
Wrote: /home/labs/rpmbuild/SOURCES/swap_control_selinux-1.0-1.el8.src.rpm
Wrote: /home/labs/rpmbuild/SOURCES/noarch/swap_control_selinux-1.0-1.el8.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.ve3iql
+ umask 022
+ cd /home/labs/rpmbuild/SOURCES
+ /usr/bin/rm -rf /home/labs/rpmbuild/SOURCES/.build/swap_control_selinux-1.0-1.el8.x86_64
+ exit 0
```

## Электронная цифровая подпись RPM-пакета

```
[labs@localhost rpmbuild]$ gpg2 --gen-key
[labs@localhost rpmbuild]$ gpg2 --export -a 'Talamanov George' > ~/rpmbuild/RPM-GPG-KEY-Talamanov-George
[labs@localhost rpmbuild]$ nano ~/.rpmmacros 
[labs@localhost rpmbuild]$ rpm --addsign ~/rpmbuild/RPMS/*/*.rpm
/home/labs/rpmbuild/RPMS/noarch/swap-control-1.0-1.el8.noarch.rpm:
```

## Создание RPM-репозитория

```
[labs@localhost rpmbuild]$ sudo mkdir -p /var/www/html/swap-control-repo/
[labs@localhost rpmbuild]$ sudo cp ~/rpmbuild/RPMS/noarch/swap-control-1.0-1.el8.noarch.rpm /var/www/html/swap-control-repo/
[labs@localhost rpmbuild]$ sudo cp ~/rpmbuild/RPM-GPG-KEY-Talamanov-George /var/www/html/swap-control-repo/
[labs@localhost rpmbuild]$ sudo createrepo -v /var/www/html/swap-control-repo/
06:42:37: Version: 0.17.2 (Features: DeltaRPM LegacyWeakdeps )
06:42:37: Signal handler setup
06:42:37: Thread pool ready
Directory walk started
06:42:37: Adding pkg: /var/www/html/swap-control-repo/swap-control-1.0-1.el8.noarch.rpm
06:42:37: Dir to scan: /var/www/html/swap-control-repo/.repodata
06:42:37: Package count: 1
Directory walk done - 1 packages
Temporary output repo path: /var/www/html/swap-control-repo/.repodata/
06:42:37: Creating .xml.gz files
06:42:37: Setting number of packages
Preparing sqlite DBs
06:42:37: Creating databases
06:42:37: Thread pool user data ready
Pool started (with 5 workers)
Pool finished
06:42:37: Generating repomd.xml
06:42:37: Old repodata doesn't exists: Cannot rename /var/www/html/swap-control-repo/repodata/ -> /var/www/html/swap-control-repo/repodata.old.19407.20220525064237.860091: No such file or directory
06:42:37: Renamed /var/www/html/swap-control-repo/.repodata/ -> /var/www/html/swap-control-repo/repodata/
06:42:37: Memory cleanup
06:42:37: All done
[labs@localhost service]$ sudo yum install /var/www/html/swap-control-repo/swap-control-1.0-1.el8.noarch.rpm 
Last metadata expiration check: 2:00:15 ago on Wed 25 May 2022 07:48:20 AM PDT.
Package swap-control-1.0-1.el8.noarch is already installed.
Dependencies resolved.
Nothing to do.
Complete!
```

## Демонтрация работы сервиса 

```
[labs@localhost SOURCES]$ pstree
systemd─┬─ModemManager───2*[{ModemManager}]
        ├─NetworkManager───2*[{NetworkManager}]
        ├─VGAuthService
        ├─abrt-dbus───2*[{abrt-dbus}]
        ├─2*[abrt-dump-journ]
        ├─abrtd───2*[{abrtd}]
        ├─accounts-daemon───2*[{accounts-daemon}]
        ├─alsactl
        ├─atd
        ├─auditd─┬─sedispatch
        │        └─2*[{auditd}]
        ├─avahi-daemon───avahi-daemon
        ├─chronyd
        ├─colord───2*[{colord}]
        ├─crond
        ├─cupsd
        ├─dbus-daemon
        ├─dnsmasq───dnsmasq
        ├─firewalld───{firewalld}
        ├─fwupd───4*[{fwupd}]
        ├─gdm─┬─gdm-session-wor─┬─gdm-wayland-ses─┬─gnome-session-b─┬─abrt-applet───3*[{abrt-applet}]
        │     │                 │                 │                 ├─gnome-shell─┬─Xwayland───8*[{Xwayland}]
        │     │                 │                 │                 │             ├─ibus-daemon─┬─ibus-dconf───3*[{ibus-dconf}]
        │     │                 │                 │                 │             │             ├─ibus-engine-sim───2*[{ibus-engine-sim}]
        │     │                 │                 │                 │             │             ├─ibus-extension-───3*[{ibus-extension-}]
        │     │                 │                 │                 │             │             └─2*[{ibus-daemon}]
        │     │                 │                 │                 │             └─14*[{gnome-shell}]
        │     │                 │                 │                 ├─gnome-software───3*[{gnome-software}]
        │     │                 │                 │                 ├─gsd-a11y-settin───3*[{gsd-a11y-settin}]
        │     │                 │                 │                 ├─gsd-account───3*[{gsd-account}]
        │     │                 │                 │                 ├─gsd-clipboard───2*[{gsd-clipboard}]
        │     │                 │                 │                 ├─gsd-color───3*[{gsd-color}]
        │     │                 │                 │                 ├─gsd-datetime───3*[{gsd-datetime}]
        │     │                 │                 │                 ├─gsd-disk-utilit───2*[{gsd-disk-utilit}]
        │     │                 │                 │                 ├─gsd-housekeepin───3*[{gsd-housekeepin}]
        │     │                 │                 │                 ├─gsd-keyboard───3*[{gsd-keyboard}]
        │     │                 │                 │                 ├─gsd-media-keys───3*[{gsd-media-keys}]
        │     │                 │                 │                 ├─gsd-mouse───3*[{gsd-mouse}]
        │     │                 │                 │                 ├─gsd-power───3*[{gsd-power}]
        │     │                 │                 │                 ├─gsd-print-notif───2*[{gsd-print-notif}]
        │     │                 │                 │                 ├─gsd-rfkill───2*[{gsd-rfkill}]
        │     │                 │                 │                 ├─gsd-screensaver───2*[{gsd-screensaver}]
        │     │                 │                 │                 ├─gsd-sharing───3*[{gsd-sharing}]
        │     │                 │                 │                 ├─gsd-smartcard───5*[{gsd-smartcard}]
        │     │                 │                 │                 ├─gsd-sound───3*[{gsd-sound}]
        │     │                 │                 │                 ├─gsd-wacom───3*[{gsd-wacom}]
        │     │                 │                 │                 ├─gsd-xsettings───3*[{gsd-xsettings}]
        │     │                 │                 │                 ├─tracker-miner-a───4*[{tracker-miner-a}]
        │     │                 │                 │                 ├─tracker-miner-f───4*[{tracker-miner-f}]
        │     │                 │                 │                 └─3*[{gnome-session-b}]
        │     │                 │                 └─2*[{gdm-wayland-ses}]
        │     │                 └─2*[{gdm-session-wor}]
        │     └─2*[{gdm}]
        ├─gnome-keyring-d───3*[{gnome-keyring-d}]
        ├─gsd-printer───2*[{gsd-printer}]
        ├─gssproxy───5*[{gssproxy}]
        ├─haveged
        ├─httpd─┬─httpd
        │       ├─httpd───80*[{httpd}]
        │       └─2*[httpd───64*[{httpd}]]
        ├─ibus-x11───10*[{ibus-x11}]
        ├─irqbalance───{irqbalance}
        ├─ksmtuned───sleep
        ├─lsmd
        ├─mcelog
        ├─packagekitd───2*[{packagekitd}]
        ├─polkitd───5*[{polkitd}]
        ├─rhsmcertd
        ├─rpcbind
        ├─rsyslogd───2*[{rsyslogd}]
        ├─rtkit-daemon───2*[{rtkit-daemon}]
        ├─smartd
        ├─sshd
        ├─sssd─┬─sssd_be
        │      └─sssd_nss
        ├─sssd_kcm
        ├─swap-control.sh───swap-control.sh─┬─cut
        │                                   ├─free
        │                                   ├─tail
        │                                   └─tr
        ├─systemd─┬─(sd-pam)
        │         ├─at-spi-bus-laun─┬─dbus-daemon
        │         │                 └─3*[{at-spi-bus-laun}]
        │         ├─at-spi2-registr───2*[{at-spi2-registr}]
        │         ├─dbus-daemon
        │         ├─dconf-service───2*[{dconf-service}]
        │         ├─evolution-addre─┬─evolution-addre───5*[{evolution-addre}]
        │         │                 └─4*[{evolution-addre}]
        │         ├─evolution-calen─┬─evolution-calen───8*[{evolution-calen}]
        │         │                 └─4*[{evolution-calen}]
        │         ├─evolution-sourc───3*[{evolution-sourc}]
        │         ├─gnome-shell-cal───5*[{gnome-shell-cal}]
        │         ├─gnome-terminal-─┬─bash───pstree
        │         │                 ├─bash───nano
        │         │                 ├─bash
        │         │                 └─3*[{gnome-terminal-}]
        │         ├─goa-daemon───3*[{goa-daemon}]
        │         ├─goa-identity-se───3*[{goa-identity-se}]
        │         ├─gvfs-afc-volume───3*[{gvfs-afc-volume}]
        │         ├─gvfs-goa-volume───2*[{gvfs-goa-volume}]
        │         ├─gvfs-gphoto2-vo───2*[{gvfs-gphoto2-vo}]
        │         ├─gvfs-mtp-volume───2*[{gvfs-mtp-volume}]
        │         ├─gvfs-udisks2-vo───3*[{gvfs-udisks2-vo}]
        │         ├─gvfsd───2*[{gvfsd}]
        │         ├─gvfsd-fuse───5*[{gvfsd-fuse}]
        │         ├─ibus-portal───2*[{ibus-portal}]
        │         ├─pulseaudio───2*[{pulseaudio}]
        │         ├─tracker-store───4*[{tracker-store}]
        │         └─xdg-permission-───2*[{xdg-permission-}]
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-machine
        ├─systemd-udevd
        ├─tuned───4*[{tuned}]
        ├─udisksd───4*[{udisksd}]
        ├─upowerd───2*[{upowerd}]
        ├─vmtoolsd───{vmtoolsd}
        ├─vmtoolsd───3*[{vmtoolsd}]
        └─wpa_supplicant
[labs@localhost SOURCES]$ sudo systemctl start swap-control
[labs@localhost SOURCES]$ sudo systemctl status swap-control
● swap-control.service - Swap control service
   Loaded: loaded (/usr/lib/systemd/system/swap-control.service; enabled; vendor preset: disabled)
   Active: active (running) since Wed 2022-05-25 09:14:38 PDT; 14s ago
 Main PID: 7335 (swap-control.sh)
    Tasks: 6 (limit: 23516)
   Memory: 1.8M
   CGroup: /system.slice/swap-control.service
           ├─7335 /bin/bash /usr/bin/swap-control.sh
           ├─7370 /bin/bash /usr/bin/swap-control.sh
           ├─7371 free -ms 30
           ├─7372 tail -1
           ├─7373 tr -s    
           └─7374 cut -d  -f3
```

