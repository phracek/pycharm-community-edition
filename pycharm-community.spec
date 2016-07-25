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
%global bash_version 1.5.8.145
%global go_lang_version 0.11.1295
%global markdown_version 0.9.7
%global cpp_tools_version 0.8.8
%global markdown_support 2016.1.20160405
%global ansible_version 0.9.3
%global git_lab_integration_version 1.0.6
%global docker_integration 2.2.1
%global idea_multimarkdown_version 1.6.1
%global ideavim_version 0.44-297
%global editor_config_version 145.258.3
%global ini_version 145.258.2

Name:          pycharm-community
Version:       2016.1.4
Release:       6%{?dist}
Summary:       Intelligent Python IDE
Group:         Development/Tools
License:       ASL 2.0
URL:           http://www.jetbrains.com/pycharm/
Source0:       http://download.jetbrains.com/python/%{name}-%{version}.tar.gz
#Source1 https://plugins.jetbrains.com/plugin/download?pr=idea&updateId=26120
Source1:       BashSupport-%{bash_version}.zip
#Source2 https://plugins.jetbrains.com/plugin/download?pr=&updateId=19624
Source2:       CppTools-%{cpp_tools_version}.zip
#Source3 https://plugins.jetbrains.com/plugin/download?pr=idea_ce&updateId=25366
Source3:       Go-%{go_lang_version}.zip
#Source4 https://github.com/nicoulaj/idea-markdown/archive/0.9.7.zip
Source4:       idea-markdown-%{markdown_version}.zip
#Source5 https://plugins.jetbrains.com/plugin/download?pr=idea_ce&updateId=25156
Source5:       markdown-%{markdown_support}.zip
#Source6 https://plugins.jetbrains.com/plugin/download?pr=&updateId=25063
Source6:       intellij-ansible-%{ansible_version}.zip
#Source7 https://plugins.jetbrains.com/plugin/download?pr=&updateId=17542
Source7:       gitlab-integration-plugin-%{git_lab_integration_version}.zip
#Source8 https://plugins.jetbrains.com/plugin/download?pr=&updateId=25297
Source8:       Docker-plugin-%{docker_integration}.jar
#Source9 https://plugins.jetbrains.com/plugin/download?pr=idea&updateId=25621
Source9:       idea-multimarkdown.%{idea_multimarkdown_version}.zip
#Source10 https://plugins.jetbrains.com/plugin/download?pr=idea&updateId=22030
Source10:      ideavim-%{ideavim_version}.zip
#Source11 https://plugins.jetbrains.com/plugin/download?pr=&updateId=24766
Source11:      editorconfig-%{editor_config_version}.zip
#Source13 https://plugins.jetbrains.com/plugin/download?pr=&updateId=24756
Source13:      ini4idea-%{ini_version}.zip
Source101:     pycharm.xml
Source102:     pycharm.desktop
Source103:     pycharm-community.appdata.xml
Patch2:        pycharm-community-pytest-init-whitespace.patch
Patch3:        pycharm-community-pytest-parametrize.patch
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
%patch2 -p1
%patch3 -p1
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
%setup -q -n %{name}-%{version} -D -T -a 13

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
%dir %{_javadir}/%{name}/%{plugins_dir}/git4idea/*
%{_javadir}/%{name}/%{plugins_dir}/git4idea/*
%dir %{_javadir}/%{name}/%{plugins_dir}/github/*
%{_javadir}/%{name}/%{plugins_dir}/github/*
%dir %{_javadir}/%{name}/%{plugins_dir}/hg4idea/*
%{_javadir}/%{name}/%{plugins_dir}/hg4idea/*
%dir %{_javadir}/%{name}/%{plugins_dir}/cvsIntegration/*
%{_javadir}/%{name}/%{plugins_dir}/cvsIntegration/*
%dir %{_javadir}/%{name}/%{plugins_dir}/ipnb/*
%{_javadir}/%{name}/%{plugins_dir}/ipnb/*
%dir %{_javadir}/%{name}/%{plugins_dir}/python-rest/*
%{_javadir}/%{name}/%{plugins_dir}/python-rest/*
%dir %{_javadir}/%{name}/%{plugins_dir}/rest/*
%{_javadir}/%{name}/%{plugins_dir}/rest/*
%dir %{_javadir}/%{name}/%{plugins_dir}/settings-repository/*
%{_javadir}/%{name}/%{plugins_dir}/settings-repository/*
%dir %{_javadir}/%{name}/%{plugins_dir}/svn4idea/*
%{_javadir}/%{name}/%{plugins_dir}/svn4idea/*
%dir %{_javadir}/%{name}/%{plugins_dir}/tasks/*
%{_javadir}/%{name}/%{plugins_dir}/tasks/*
%dir %{_javadir}/%{name}/%{plugins_dir}/terminal/*
%{_javadir}/%{name}/%{plugins_dir}/terminal/*
%exclude %{_javadir}/%{name}/%{plugins_dir}/{BashSupport,CppTools,idea-markdown}/*
%exclude %{_javadir}/%{name}/%{plugins_dir}/{intellij-ansible,markdown,gitlab-integration-plugin}/*
%exclude %{_javadir}/%{name}/%{plugins_dir}/{Go,IdeaVim,idea-multimarkdown,editorconfig,ini4idea}/*
%exclude %{_javadir}/%{name}/%{plugins_dir}/Docker-plugin.jar
%{_bindir}/pycharm


%files plugins
%defattr(-,root,root)
%dir %{_javadir}/%{name}/%{plugins_dir}/BashSupport
%{_javadir}/%{name}/%{plugins_dir}/BashSupport/*
%dir %{_javadir}/%{name}/%{plugins_dir}/CppTools
%{_javadir}/%{name}/%{plugins_dir}/CppTools/*
%dir %{_javadir}/%{name}/%{plugins_dir}/idea-markdown
%{_javadir}/%{name}/%{plugins_dir}/idea-markdown/*
%dir %{_javadir}/%{name}/%{plugins_dir}/intellij-ansible
%{_javadir}/%{name}/%{plugins_dir}/intellij-ansible/*
%dir %{_javadir}/%{name}/%{plugins_dir}/markdown
%{_javadir}/%{name}/%{plugins_dir}/markdown/*
%dir %{_javadir}/%{name}/%{plugins_dir}/gitlab-integration-plugin
%{_javadir}/%{name}/%{plugins_dir}/gitlab-integration-plugin/*
%dir %{_javadir}/%{name}/%{plugins_dir}/Go
%{_javadir}/%{name}/%{plugins_dir}/Go/*
%dir %{_javadir}/%{name}/%{plugins_dir}/IdeaVim
%{_javadir}/%{name}/%{plugins_dir}/IdeaVim/*
%dir %{_javadir}/%{name}/%{plugins_dir}/idea-multimarkdown
%{_javadir}/%{name}/%{plugins_dir}/idea-multimarkdown/*
%{_javadir}/%{name}/%{plugins_dir}/Docker-plugin.jar
%dir %{_javadir}/%{name}/%{plugins_dir}/editorconfig
%{_javadir}/%{name}/%{plugins_dir}/editorconfig/*
%dir %{_javadir}/%{name}/%{plugins_dir}/ini4idea
%{_javadir}/%{name}/%{plugins_dir}/ini4idea/*

%changelog
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
