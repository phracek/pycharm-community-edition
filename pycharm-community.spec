# disable debuginfo subpackage
%global debug_package %{nil}
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

%global plugins_dir plugins

%global ansible_version 0.9.5
%global ansible_id 35585

%global bash_version 1.6.13.182
%global bash_id 46357

%global repmapper_version 2.3.1
%global repmapper_id 44337

%global docker_integration_version 182.3684.90
%global docker_integration_id 48047

%global editor_config_version 182.2949.6
%global editor_config_id 46642

%global git_lab_integration_version 1.0.6
%global git_lab_integration_id 17542

%global idea_multimarkdown_version 2.5.4
%global idea_multimarkdown_id 46921

%global ideavim_version 0.49
%global ideavim_id 41383

%global ini_version 182.3911.19
%global ini_id 48384

%global markdown_support_version 182.2371
%global markdown_support_id 45898

%global git_tool_box_version 182.1.1
%global git_tool_box_id 47855

%global ignore_plugin_version 3.0.0.182
%global ignore_plugin_id 48021

%global dbnavigator_version 3.0.8222.0
%global dbnavigator_id 46638

%global rust_version 0.2.0.2103-182
%global rust_id 48624

Name:          pycharm-community
Version:       2018.2.1
Release:       1%{?dist}

Summary:       Intelligent Python IDE
License:       ASL 2.0
URL:           http://www.jetbrains.com/pycharm/

Source0:       http://download.jetbrains.com/python/%{name}-%{version}.tar.gz
Source1:       https://plugins.jetbrains.com/files/4230/%{bash_id}/BashSupport-%{bash_version}.zip#/BashSupport-%{bash_version}.zip
Source2:       https://plugins.jetbrains.com/files/8183/%{repmapper_id}/GitLink-%{repmapper_version}.zip#/GitLink-%{repmapper_version}.zip
Source3:       https://plugins.jetbrains.com/files/1800/%{dbnavigator_id}/DBN-18.0.zip#/DBN-%{dbnavigator_version}.zip
Source4:       https://plugins.jetbrains.com/files/7793/%{markdown_support_id}/markdown-%{markdown_support_version}.zip#/markdown-%{markdown_support_version}.zip
Source5:       https://plugins.jetbrains.com/files/7792/%{ansible_id}/intellij-ansible-%{ansible_version}.zip#/intellij-ansible-%{ansible_version}.zip
Source6:       https://plugins.jetbrains.com/files/7447/%{git_lab_integration_id}/gitlab-integration-plugin.zip#/gitlab-integration-plugin-%{git_lab_integration_version}.zip
Source7:       https://plugins.jetbrains.com/files/7724/%{docker_integration_id}/Docker-%{docker_integration_version}.zip#/Docker-plugin-%{docker_integration_version}.zip
Source8:       https://plugins.jetbrains.com/files/7896/%{idea_multimarkdown_id}/idea-multimarkdown.%{idea_multimarkdown_version}.zip#/idea-multimarkdown-%{idea_multimarkdown_version}.zip
Source9:       https://plugins.jetbrains.com/files/164/%{ideavim_id}/IdeaVim-%{ideavim_version}.zip#/IdeaVim-%{ideavim_version}.zip
Source10:      https://plugins.jetbrains.com/files/7294/%{editor_config_id}/editorconfig-%{editor_config_version}.zip#/editorconfig-%{editor_config_version}.zip
Source11:      https://plugins.jetbrains.com/files/6981/%{ini_id}/ini4idea-%{ini_version}.zip#/ini4idea-%{ini_version}.zip
Source12:      https://plugins.jetbrains.com/files/7499/%{git_tool_box_id}/GitToolBox-%{git_tool_box_version}.zip#/GitToolBox-%{git_tool_box_version}.zip
Source13:      https://plugins.jetbrains.com/files/7495/%{ignore_plugin_id}/idea-gitignore-%{ignore_plugin_version}.zip#/GitIgnore-%{ignore_plugin_version}.zip
Source14:      https://plugins.jetbrains.com/files/8182/%{rust_id}/intellij-rust-%{rust_version}.zip#/intellij-rust-%{rust_version}.zip

Source101:     pycharm.xml
Source102:     pycharm-community.desktop
Source103:     pycharm-community.appdata.xml

BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/appstream-util
BuildRequires: python2-devel
%if %{with python3}
BuildRequires: python3-devel
%endif
Requires:      java
%ifarch x86_64
%if 0%{?fedora}
Recommends:    %{name}-jre%{?_isa} = %{version}-%{release}
%else
Requires:      %{name}-jre%{?_isa} = %{version}-%{release}
%endif
%endif

%description
The intelligent Python IDE with unique code assistance and analysis,
for productive Python development on all levels

%package plugins
Summary:       Plugins for intelligent Python IDE
Requires:      %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:       Documentation for intelligent Python IDE
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%ifarch x86_64
%package jre
Summary:       Patched OpenJDK for intelligent Python IDE by JetBrains
Requires:      %{name}%{?_isa} = %{version}-%{release}
%endif

%description plugins
Intelligent Python IDE contains several plugins. This package
contains plugins like BashSupport, RemoteRepositoryMapper, GoLang, Markdown,
Idea Markdown, Intellij Ansible, GitLab integration plugin, etc.

%description doc
This package contains documentation for Intelligent Python IDE.

%ifarch x86_64
%description jre
This package contains patched OpenJDK designed specially for Intelligent
Python IDE by JetBrains, Inc.
%endif

%prep
%setup -q -n %{name}-%{version}
%setup -q -n %{name}-%{version} -D -T -a 1
%setup -q -n %{name}-%{version} -D -T -a 2
%setup -q -n %{name}-%{version} -D -T -a 3
%setup -q -n %{name}-%{version} -D -T -a 4
%setup -q -n %{name}-%{version} -D -T -a 5
%setup -q -n %{name}-%{version} -D -T -a 6
%setup -q -n %{name}-%{version} -D -T -a 7
%setup -q -n %{name}-%{version} -D -T -a 8
%setup -q -n %{name}-%{version} -D -T -a 9
%setup -q -n %{name}-%{version} -D -T -a 10
%setup -q -n %{name}-%{version} -D -T -a 11
%setup -q -n %{name}-%{version} -D -T -a 12
%setup -q -n %{name}-%{version} -D -T -a 13
%setup -q -n %{name}-%{version} -D -T -a 14

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/metainfo
mkdir -p %{buildroot}%{_bindir}

cp -arf ./{lib,bin,help,helpers,plugins} %{buildroot}%{_javadir}/%{name}/
%ifarch x86_64
cp -arf ./jre64 %{buildroot}%{_javadir}/%{name}/
%endif
# Move all plugins to /usr/share/java/pycharm-community/plugins directory
cp -arf ./BashSupport %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./GitLink %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./DBNavigator %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./markdown %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./intellij-ansible %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./gitlab-integration-plugin %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./idea-multimarkdown %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./IdeaVim %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./editorconfig %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./ini4idea %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./GitToolBox %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./Docker %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./idea-gitignore %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./intellij-rust %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/

rm -f %{buildroot}%{_javadir}/%{name}/bin/fsnotifier{,-arm}
# this will be in docs
rm -f %{buildroot}%{_javadir}/help/*.pdf
cp -af ./bin/pycharm.png %{buildroot}%{_datadir}/pixmaps/pycharm.png
cp -af %{SOURCE101} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
cp -af %{SOURCE102} %{buildroot}%{_datadir}/pycharm-community.desktop
cp -a %{SOURCE103} %{buildroot}%{_datadir}/metainfo
ln -s %{_javadir}/%{name}/bin/pycharm.sh %{buildroot}%{_bindir}/pycharm
desktop-file-install                          \
--add-category="Development"                  \
--delete-original                             \
--dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/pycharm-community.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/pycharm-community.appdata.xml

%files
%{_datadir}/applications/pycharm-community.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/pycharm.png
%{_datadir}/metainfo/pycharm-community.appdata.xml
%{_javadir}/%{name}
%ifarch x86_64
%exclude %{_javadir}/%{name}/jre64
%endif
%exclude %{_javadir}/%{name}/%{plugins_dir}/{BashSupport,GitLink,DBNavigator}
%exclude %{_javadir}/%{name}/%{plugins_dir}/{intellij-ansible,markdown,gitlab-integration-plugin}
%exclude %{_javadir}/%{name}/%{plugins_dir}/{IdeaVim,idea-multimarkdown,editorconfig,ini4idea}
%exclude %{_javadir}/%{name}/%{plugins_dir}/{GitToolBox,Docker,idea-gitignore,intellij-rust}
%{_bindir}/pycharm

%files plugins
%{_javadir}/%{name}/%{plugins_dir}/BashSupport
%{_javadir}/%{name}/%{plugins_dir}/GitLink
%{_javadir}/%{name}/%{plugins_dir}/DBNavigator
%{_javadir}/%{name}/%{plugins_dir}/intellij-ansible
%{_javadir}/%{name}/%{plugins_dir}/markdown
%{_javadir}/%{name}/%{plugins_dir}/gitlab-integration-plugin
%{_javadir}/%{name}/%{plugins_dir}/IdeaVim
%{_javadir}/%{name}/%{plugins_dir}/idea-multimarkdown
%{_javadir}/%{name}/%{plugins_dir}/Docker
%{_javadir}/%{name}/%{plugins_dir}/editorconfig
%{_javadir}/%{name}/%{plugins_dir}/ini4idea
%{_javadir}/%{name}/%{plugins_dir}/GitToolBox
%{_javadir}/%{name}/%{plugins_dir}/idea-gitignore
%{_javadir}/%{name}/%{plugins_dir}/intellij-rust

%files doc
%doc *.txt
%doc help/*.pdf
%license license/

%ifarch x86_64
%files jre
%{_javadir}/%{name}/jre64
%endif

%changelog
* Wed Aug 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.2.1-1
- Updated to version 2018.2.1.

* Fri Aug 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.2-2
- Added -jre subpackage with JRE by JetBrains with fixed fonts.
- Removed obsolete entries from SPEC.
- All plugins updated to latest versions.
- Removed all outdated plugins and added new instead.

* Mon Jul 30 2018 Petr Hracek <phracek@redhat.com> - 2018.2-1
- Update to the latest upstream version 2018.2

* Thu May 17 2018 Petr Hracek <phracek@redhat.com> - 2018.1.3-1
- Update to the latest upstream version, 2018.1.3

* Tue Apr 03 2018 Petr Hracek <phracek@redhat.com> - 2018.1-1
- Update to the latest upstream version, 2018.1

* Tue Mar 13 2018 Petr Hracek <phracek@redhat.com> - 2017.3.4-1
- Update to latest upstream version, 2017.3.4

* Wed Jan 24 2018 Petr Hracek <phracek@redhat.com> - 2017.3.3-1
- Update to latest upstream version, 2017.3.3.

* Tue Jan 09 2018 Petr Hracek <phracek@redhat.com> - 2017.3.2-1
- Update to latest upstream version, 2017.3.2.

* Thu Dec 14 2017 Petr Hracek <phracek@redhat.com> - 2017.3.1-1
- Update to latest upstream version, 2017.3.1.

* Mon Dec 04 2017 Petr Hracek <phracek@redhat.com> - 2017.3-1
- Update to latest upstream version, 2017.3

* Thu Nov 02 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.2.4-1
- Update to latest upstream version, 2017.2.4.

* Wed Sep 06 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.2.3-1
- Update to latest upstream version, 2017.2.3.

* Tue Aug 29 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.2.2-1
- Update to latest upstream version, 2017.2.2.

* Fri Aug 11 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.2.1-3
- Update plugins.

* Thu Aug 10 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.2.1-2
- Revert top-level archive directory change as upstream archive has been fixed.

* Wed Aug 09 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.2.1-1
- Update to latest upstream version, 2017.2.1.

* Wed Jul 26 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.2-1
- Update to latest upstream version, 2017.2.

* Thu Jul 13 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.1.5-1
- Update to latest upstream version, 2017.1.5.

* Fri Jun 16 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.1.4-1
- Update to latest upstream version, 2017.1.4.

* Tue May 30 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.1.3-1
- Update to latest upstream version, 2017.1.3.

* Tue May 02 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.1.2-1
- Update to latest upstream version, 2017.1.2.

* Tue Apr 18 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.1.1-1
- Update to latest upstream version, 2017.1.1.

* Mon Mar 27 2017 Allan Lewis <allanlewis99@gmail.com> - 2017.1-1
- Update to latest upstream version, 2017.1, and update plugins.

* Fri Mar 17 2017 Allan Lewis <allanlewis99@gmail.com> - 2016.3.3-1
- Update to latest upstream version, 2016.3.3, and update plugins.

* Wed Mar 15 2017 Petr Hracek <phracek@redhat.com> - 2016.3.2-4
- Fixing spec file in order to support correct desktop file.

* Wed Mar 15 2017 Petr Hracek <phracek@redhat.com> - 2016.3.2-3
- Fixing desktop file. Thx hugsie.

* Mon Jan 09 2017 Allan Lewis <allanlewis99@gmail.com> - 2016.3.2-2
- Remove obsolete "CppTools" plugin and update "Go" plugin.

* Mon Jan 02 2017 Petr Hracek <phracek@redhat.com> - 2016.3.2-1
- Update to latest upstream version, 2016.3.2.

* Tue Dec 20 2016 Allan Lewis <allanlewis99@gmail.com> - 2016.3.1-1
- Update to latest upstream version, 2016.3.1.

* Fri Dec 9 2016 Allan Lewis <allanlewis99@gmail.com> - 2016.3-2
- Update all plugins to the latest versions

* Mon Nov 28 2016 Petr Hracek <phracek@redhat.com> - 2016.3-1
- Update to the latest upstream version 2016.3

* Mon Oct 17 2016 Petr Hracek <phracek@redhat.com> - 2016.2.3-2
- Add GitToolBox plugin

* Mon Sep 12 2016 Petr Hracek <phracek@redhat.com> - 2016.2.3-1
- Update to the latest upstream version 2016.2.3

* Fri Aug 26 2016 Petr Hracek <phracek@redhat.com> - 2016.2.2-1
- Update to the latest upstream version 2016.2.2

* Thu Aug 25 2016 Petr Hracek <phracek@redhat.com> - 2016.2.1-2
- Update Docker integration, YAML/Ansible support
- Update Markdown support

* Mon Aug 15 2016 Allan Lewis <allanlewis99@gmail.com> - 2016.2.1-1
- Update to latest upstream version, 2016.2.1.

* Wed Jul 27 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 2016.2-2
- Added -doc subpackage. Lots of fixes. Fixed exclusion of plugins.

* Mon Jul 25 2016 Allan Lewis <allanlewis99@gmail.com> - 2016.2-1
- Update to latest upstream version, 2016.2.

* Wed Jul 13 2016 Allan Lewis <allanlewis99@gmail.com> - 2016.1.4-6
- Patch Pytest 'parametrize' skeleton to match Pytest 2.9.2.

* Wed Jul 13 2016 Petr Hracek <phracek@redhat.com> - 2016.1.4-5
- Fix %exclude syntax

* Wed Jun 01 2016 Petr Hracek <phracek@redhat.com> - 2016.1.4-4
- Added plugins EditorConfig, Git4Idea, ini4idea

* Tue May 31 2016 Petr Hracek <phracek@redhat.com> - 2016.1.4-3
- Update Go plugin, Markdown and BashSupport
- CppTools plugin aren't compatible with the latest PyCharm

* Fri May 27 2016 Tomas Hozza <thozza@redhat.com> - 2016.1.4-2
- Don't distribute plugins in the base package

* Fri May 27 2016 Petr Hracek <phracek@redhat.com> - 2016.1.4-1
- Update to the latest version 2016.1.4

* Fri May 20 2016 Petr Hracek <phracek@redhat.com> - 2016.1.3-2
- Update plugins Bash, Docker, MultiMarkdown

* Thu May 12 2016 Petr Hracek <phracek@redhat.com> - 2016.1.3-1
- Update to the latest version 2016.1.3

* Fri May 06 2016 Petr Hracek <phracek@redhat.com> - 2016.1.2-3
- SpecFile rewrite and add support for Docker Integration
- plugin Multimarkdown

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
