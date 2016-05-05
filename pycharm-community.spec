# don't strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%global __strip /bin/true
# dont repack jars
%global __jar_repack %{nil}
# there are some python 2 and python 3 scripts so there is no way out to bytecompile them ^_^
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%if 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%global bash_version 1.5.5.145
%global go_lang_version 0.10.1296
%global markdown_version 0.9.7
%global cpp_tools_version 0.8.8
%global markdown_support 2016.1.20160405.143
%global ansible_version 0.9.3
%global git_lab_integration_version 1.0.6

Name:          pycharm-community
Version:       2016.1.2
Release:       2%{?dist}
Summary:       Intelligent Python IDE
Group:         Development/Tools
License:       ASL 2.0
URL:           http://www.jetbrains.com/pycharm/
Source0:       http://download.jetbrains.com/python/%{name}-%{version}.tar.gz
Source1:       BashSupport-%{bash_version}.zip
Source2:       CppTools-%{cpp_tools_version}.zip
Source3:       Go-%{go_lang_version}.zip
Source4:       idea-markdown-%{markdown_version}.zip
Source5:       markdown-%{markdown_support}.zip
Source6:       intellij-ansible-%{ansible_version}.zip
Source7:       gitlab-integration-plugin-%{git_lab_integration_version}.zip
Source101:     pycharm.xml
Source102:     pycharm.desktop
Source103:     pycharm-community.appdata.xml
Patch1:        pycharm-community-MaxPermSize.patch
BuildRequires: desktop-file-utils
BuildRequires: python2-devel
%if %{with python3}
BuildRequires: python3-devel
%endif
Requires:      java

%description
The intelligent Python IDE with unique code assistance and analysis,
for productive Python development on all levels

%package plugins
Summary:       Plugins for intelligent Python IDE
Group:         System Environment/Libraties
Requires:      %{name}
Requires:      %{name} = %{version}

%description plugins
Intelligent Python IDE contains several plugins. This package
contains plugins like BashSupport, CppTools, GoLang, Markdown, Idea Markdown
Intellij Ansible, GitLab integration plugin.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%setup -q -n %{name}-%{version} -D -T -a 1
%setup -q -n %{name}-%{version} -D -T -a 2
%setup -q -n %{name}-%{version} -D -T -a 3
%setup -q -n %{name}-%{version} -D -T -a 4
%setup -q -n %{name}-%{version} -D -T -a 5
%setup -q -n %{name}-%{version} -D -T -a 6
%setup -q -n %{name}-%{version} -D -T -a 7

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_bindir}

cp -arf ./{lib,bin,help,helpers,plugins} %{buildroot}%{_javadir}/%{name}/
# Move all plugins to /usr/share/java/pycharm-community/plugins directory
cp -arf ./{BashSupport,CppTools} %{buildroot}%{_javadir}/%{name}/plugins/
cp -arf ./{idea-markdown,intellij-ansible,markdown} %{buildroot}%{_javadir}/%{name}/plugins/
cp -arf ./{gitlab-integration-plugin,Go} %{buildroot}%{_javadir}/%{name}/plugins/

rm -f %{buildroot}%{_javadir}/%{name}/bin/fsnotifier{,-arm}
# this will be in docs
rm -f %{buildroot}%{_javadir}/help/*.pdf
cp -af ./bin/pycharm.png %{buildroot}%{_datadir}/pixmaps/pycharm.png
cp -af %{SOURCE101} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
cp -af %{SOURCE102} %{buildroot}%{_datadir}/pycharm.desktop
cp -a %{SOURCE103} %{buildroot}%{_datadir}/appdata
ln -s %{_javadir}/%{name}/bin/pycharm.sh %{buildroot}%{_bindir}/pycharm
desktop-file-install                          \
--add-category="Development"                  \
--delete-original                             \
--dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/pycharm.desktop

%files
%defattr(-,root,root)
%doc *.txt
%doc license/
%doc help/*.pdf
%dir %{_datadir}/%{name}
%{_datadir}/applications/pycharm.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/pycharm.png
%{_datadir}/appdata/pycharm-community.appdata.xml
%{_javadir}/%{name}/*
%{_bindir}/pycharm


%files plugins
%defattr(-,root,root)
%dir %{_javadir}/%{name}/plugins/{BashSupport,CppTools}
%{_javadir}/%{name}/plugins/{BashSupport,CppTools}/*
%dir %{_javadir}/%{name}/plugins/{idea-markdown,intellij-ansible,markdown}
%{_javadir}/%{name}/plugins/{idea-markdown,intellij-ansible,markdown}/*
%dir %{_javadir}/%{name}/plugins/{gitlab-integration-plugin,Go}
%{_javadir}/%{name}/plugins/{gitlab-integration-plugin,Go}/*

%changelog
* Thu May 05 2016 Petr Hracek <phracek@redhat.com> - 2016.1.2-2
- Add package pycharm-community-plugins which contains
  BashSupport, CppTools, markdown, Go, gitlab-integration

* Mon Apr 11 2016 Petr Hracek <phracek@redhat.com> - 2016.1.2-1
- Update to the latest version 2016.1.2

* Thu Apr 07 2016 Petr Hracek <phracek@redhat.com> - 2016.1.1-1
- Update to the latest version 2016.1.1

* Thu Mar 24 2016 Petr Hracek <phracek@redhat.com> - 2016.1-1
- Update to the latest version 2016.1

* Fri Jan 29 2016 Petr Hracek <phracek@redhat.com> - 5.0.4-1
- Update to the latest version, 5.0.4

* Mon Jan 04 2016 Petr Hracek <phracek@redhat.com> - 5.0.3-1
- update to the latest version, 5.0.3

* Fri Dec 11 2015 Allan Lewis <allanlewis@users.noreply.github.com> - 5.0.2-1
- update to the latest version, 5.0.2

* Tue Nov 17 2015 Allan Lewis <allanlewis@users.noreply.github.com> - 5.0.1-1
- update to the latest version, 5.0.1

* Thu Nov 05 2015 Petr Hracek <phracek@redhat.com> - 5.0-2
- Rebuild for Fedora 23

* Tue Nov 03 2015 Petr Hracek <phracek@redhat.com> - 5.0-1
- update to the latest version 5.0

* Tue Sep 08 2015 Petr Hracek <phracek@redhat.com> - 4.5.4-1
- update to the latest version 4.5.4

* Wed Jul 15 2015 Petr Hracek <phracek@redhat.com> - 4.5.3-1
- update to the latest version 4.5.3

* Tue Jun 30 2015 Petr Hracek <phracek@redhat.com> - 4.5.2-2
- pycharm.desktop fix done by Allan Lewis

* Mon Jun 29 2015 Allan Lewis <allanlewis@users.noreply.github.com> - 4.5.2-1
- update to the latest version 4.5.2

* Mon May 25 2015 Petr Hracek <phracek@redhat.com> - 4.5.1-1
- update to the latest version 4.5.1

* Thu Apr 16 2015 Petr Hracek <phracek@redhat.com> - 4.5-1
- update to the latest version 4.5

* Thu Apr 16 2015 Petr Hracek <phracek@redhat.com> - 4.0.6-1
- update to the latest version 4.0.6

* Wed Mar 25 2015 Petr Hracek <phracek@redhat.com> - 4.0.5-2
- Add metadata for Gnome Software Center

* Fri Mar 13 2015 Jiri Popelka <jpopelka@redhat.com> - 4.0.5-1
- update to the latest version 4.0.5

* Wed Feb 25 2015 Petr Hracek <phracek@redhat.com> - 4.0.4-2
- supports EPEL 7

* Tue Jan 20 2015 Petr Hracek <phracek@redhat.com> - 4.0.4-1
- update to the latest version 4.0.4

* Wed Dec 17 2014 Petr Hracek <phracek@redhat.com> - 4.0.3-1
- update to the latest version 4.0.3

* Tue Dec 16 2014 Petr Hracek <phracek@redhat.com> - 4.0.2-1
- update to the latest version 4.0.2

* Mon Dec 01 2014 Petr Hracek <phracek@redhat.com> - 4.0.1-1
- update to the latest version 4.0.1

* Fri Nov 21 2014 Petr Hracek <phracek@redhat.com> - 4.0-1
- new upstream version 4.0

* Fri Nov 07 2014 Tomas Hozza <thozza@redhat.com> - 3.4.1-3
- Install the icon with name used in .desktop file

* Thu Jul 31 2014 Tomas Tomecek <ttomecek@redhat.com> - 3.4.1-2
- new upstream version 3.4.1
- sanitize specfile

* Mon Jun 09 2014 Petr Hracek <phracek@redhat.com> - 3.4.1-1
- New upstream version

* Wed May 14 2014 Petr Hracek <phracek@redhat.com> - 3.1.3-1
- Initial package
