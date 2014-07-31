# dont strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%define __strip /bin/true
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
Name:		pycharm-community
Version:	3.4
Release:	1%{?dist}
Summary:	PyCharm 3
Group:      Applications/Development
License:    Apache2
URL:		http://www.jetbrains.com/pycharm/
Source0:    http://download.jetbrains.com/python/%{name}-%{version}.tar.gz
Source1:    pycharm.xml
Source2:    pycharm.desktop
Source3:    pycharm.sh
BuildRequires: desktop-file-utils python3-devel python2-devel
Requires: java

%description
The intelligent Python IDE with unique code assistance and analysis,
for productive Python development on all levels

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_javadir}/%{name}/{bin,lib,help,plugins}
mkdir -p %{buildroot}%{_javadir}/%{name}/helpers
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_bindir}

cp -af ./lib/* %{buildroot}%{_javadir}/%{name}/lib
cp -af ./help/* %{buildroot}%{_javadir}/%{name}/help
cp -af ./helpers/* %{buildroot}%{_javadir}/%{name}/helpers
cp -af ./plugins/* %{buildroot}%{_javadir}/%{name}/plugins
cp -af ./bin/* %{buildroot}%{_javadir}/%{name}/bin
cp -af ./bin/pycharm.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp -af %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
cp -af %{SOURCE2} %{buildroot}%{_datadir}/pycharm.desktop
cp -af %{SOURCE3} %{buildroot}%{_bindir}/pycharm
desktop-file-install                          \
--add-category="Development"                       \
--delete-original                             \
--dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/pycharm.desktop

%files
%defattr(-,root,root)
%doc *.txt 
%{_datadir}/applications/pycharm.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%dir %{_javadir}/%{name}
%dir %{_javadir}/%{name}/bin
%dir %{_javadir}/%{name}/lib
%dir %{_javadir}/%{name}/help
%dir %{_javadir}/%{name}/plugins
%dir %{_javadir}/%{name}/helpers
%{_javadir}/%{name}/*
%{_bindir}/pycharm
%dir %{_datadir}/%{name}


%changelog
* Mon Jun 09 2014 Petr Hracek <phracek@redhat.com> - 3.4-1
- New upstream version

* Wed May 14 2014 Petr Hracek <phracek@redhat.com> - 3.1.3-1
- Initial package


