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

%global ansible_version 0.9.4
%global ansible_id 27616

%global bash_version 1.5.8.162
%global bash_id 26121

%global cpp_tools_version 0.8.8
%global cpp_tools_id 19624

%global docker_integration_version 2.3.3
%global docker_integration_id 27617

%global editor_config_version 145.258.3
%global editor_config_id 24766

%global git_lab_integration_version 1.0.6
%global git_lab_integration_id 17542

%global go_lang_version 0.11.1295
%global go_lang_id 25366

%global idea_multimarkdown_version 2.0.0
%global idea_multimarkdown_id 27484

%global ideavim_version 0.46
%global ideavim_id 26968

%global ini_version 162.1121.34
%global ini_id 27026

%global markdown_support_version 2016.2.20160713
%global markdown_support_id 27141

%global git_tool_box_version 16.3.0
%global git_tool_box_id 28596

%global markdown_version 0.9.7

Name:          pycharm-community
Version:       2016.3
Release:       1%{?dist}
Summary:       Intelligent Python IDE
License:       ASL 2.0
URL:           http://www.jetbrains.com/pycharm/

Source0:       http://download.jetbrains.com/python/%{name}-%{version}.tar.gz

Source1:       https://plugins.jetbrains.com/files/4230/%{bash_id}/BashSupport-%{bash_version}.zip#/BashSupport-%{bash_version}.zip
Source2:       https://plugins.jetbrains.com/files/1373/%{cpp_tools_id}/CppTools.zip#/CppTools-%{cpp_tools_version}.zip
Source3:       https://plugins.jetbrains.com/files/5047/%{go_lang_id}/Go-%{go_lang_version}.zip#/Go-%{go_lang_version}.zip
Source4:       https://github.com/nicoulaj/idea-markdown/archive/%{markdown_version}.zip#/idea-markdown-%{markdown_version}.zip
Source5:       https://plugins.jetbrains.com/files/7793/%{markdown_support_id}/markdown-%{markdown_support_version}.zip#/markdown-%{markdown_support_version}.zip
Source6:       https://plugins.jetbrains.com/files/7792/%{ansible_id}/intellij-ansible.zip#/intellij-ansible-%{ansible_version}.zip
Source7:       https://plugins.jetbrains.com/files/7447/%{git_lab_integration_id}/gitlab-integration-plugin.zip#/gitlab-integration-plugin-%{git_lab_integration_version}.zip
Source8:       https://plugins.jetbrains.com/files/7724/%{docker_integration_id}/Docker-plugin.jar#/Docker-plugin-%{docker_integration_version}.jar
Source9:       https://plugins.jetbrains.com/files/7896/%{idea_multimarkdown_id}/idea-multimarkdown.%{idea_multimarkdown_version}.zip#/idea-multimarkdown-%{idea_multimarkdown_version}.zip
Source10:      https://plugins.jetbrains.com/files/164/%{ideavim_id}/IdeaVim-%{ideavim_version}.zip#/ideavim-%{ideavim_version}.zip
Source11:      https://plugins.jetbrains.com/files/7294/%{editor_config_id}/editorconfig-%{editor_config_version}.zip#/editorconfig-%{editor_config_version}.zip
Source12:      https://plugins.jetbrains.com/files/6981/%{ini_id}/ini4idea-%{ini_version}.zip#/ini4idea-%{ini_version}.zip
Source13:      https://plugins.jetbrains.com/files/7499/%{git_tool_box_id}/GitToolBox-%{git_tool_box_version}.zip#/GitToolBox-%{git_tool_box_version}.zip

Source101:     pycharm.xml
Source102:     pycharm.desktop
Source103:     pycharm-community.appdata.xml

BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/appstream-util
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
Requires:      %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:       Documentation for intelligent Python IDE
BuildArch:     noarch

%description plugins
Intelligent Python IDE contains several plugins. This package
contains plugins like BashSupport, CppTools, GoLang, Markdown, Idea Markdown
Intellij Ansible, GitLab integration plugin.

%description doc
This package contains documentation for Intelligent Python IDE.

%prep
%setup -q -n %{name}-%{version}
%setup -q -n %{name}-%{version} -D -T -a 1
%setup -q -n %{name}-%{version} -D -T -a 2
%setup -q -n %{name}-%{version} -D -T -a 3
%setup -q -n %{name}-%{version} -D -T -a 4
%setup -q -n %{name}-%{version} -D -T -a 5
%setup -q -n %{name}-%{version} -D -T -a 6
%setup -q -n %{name}-%{version} -D -T -a 7
%setup -q -n %{name}-%{version} -D -T -a 9
%setup -q -n %{name}-%{version} -D -T -a 10
%setup -q -n %{name}-%{version} -D -T -a 11
%setup -q -n %{name}-%{version} -D -T -a 12

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_bindir}

mv idea-markdown-%{markdown_version} idea-markdown
cp -arf ./{lib,bin,help,helpers,plugins} %{buildroot}%{_javadir}/%{name}/
# Move all plugins to /usr/share/java/pycharm-community/plugins directory
cp -arf ./BashSupport %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./CppTools %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./Go %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./idea-markdown %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./markdown %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./intellij-ansible %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./gitlab-integration-plugin %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./idea-multimarkdown %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./IdeaVim %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./editorconfig %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -arf ./ini4idea %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/
cp -af %{SOURCE8} %{buildroot}%{_javadir}/%{name}/%{plugins_dir}/Docker-plugin.jar

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

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/pycharm-community.appdata.xml

%files
%{_datadir}/applications/pycharm.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/pycharm.png
%{_datadir}/appdata/pycharm-community.appdata.xml
%{_javadir}/%{name}
%exclude %{_javadir}/%{name}/%{plugins_dir}/{BashSupport,CppTools,idea-markdown}
%exclude %{_javadir}/%{name}/%{plugins_dir}/{intellij-ansible,markdown,gitlab-integration-plugin}
%exclude %{_javadir}/%{name}/%{plugins_dir}/{Go,IdeaVim,idea-multimarkdown,editorconfig,ini4idea}
%exclude %{_javadir}/%{name}/%{plugins_dir}/Docker-plugin.jar
%{_bindir}/pycharm

%post
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files plugins
%{_javadir}/%{name}/%{plugins_dir}/BashSupport
%{_javadir}/%{name}/%{plugins_dir}/CppTools
%{_javadir}/%{name}/%{plugins_dir}/idea-markdown
%{_javadir}/%{name}/%{plugins_dir}/intellij-ansible
%{_javadir}/%{name}/%{plugins_dir}/markdown
%{_javadir}/%{name}/%{plugins_dir}/gitlab-integration-plugin
%{_javadir}/%{name}/%{plugins_dir}/Go
%{_javadir}/%{name}/%{plugins_dir}/IdeaVim
%{_javadir}/%{name}/%{plugins_dir}/idea-multimarkdown
%{_javadir}/%{name}/%{plugins_dir}/Docker-plugin.jar
%{_javadir}/%{name}/%{plugins_dir}/editorconfig
%{_javadir}/%{name}/%{plugins_dir}/ini4idea

%files doc
%doc *.txt
%doc help/*.pdf
%license license/

%changelog
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
