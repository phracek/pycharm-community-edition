# Disable build-id symlinks to avoid conflicts
%global _build_id_links none
# don't strip bundled binaries
%global __strip /bin/true
# dont repack jars
%global __jar_repack %{nil}
# do not bytecompile python scripts
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%global appname pycharm-community
%global plugins_dir plugins

# https://plugins.jetbrains.com/plugin/8183-gitlink/versions
%global repmapper_version 3.3.4
%global repmapper_id 115043

# https://plugins.jetbrains.com/plugin/1800-database-navigator/versions
%global dbnavigator_version 3.2.3225.0
%global dbnavigator_id 117158

# https://plugins.jetbrains.com/plugin/7792-yaml-ansible-support/versions
%global ansible_version 0.11.2
%global ansible_id 100135

# https://plugins.jetbrains.com/plugin/7447-gitlab-integration-plugin/versions
%global git_lab_integration_version 1.1.2
%global git_lab_integration_id 52232

# https://plugins.jetbrains.com/plugin/7724-docker/versions
%global docker_integration_version 211.7142.13
%global docker_integration_id 117745

# https://plugins.jetbrains.com/plugin/7896-markdown-navigator-enhanced/versions
%global idea_multimarkdown_version 3.0.202.112
%global idea_multimarkdown_id 97563

# https://plugins.jetbrains.com/plugin/164-ideavim/versions
%global ideavim_version 0.66
%global ideavim_id 116376

# https://plugins.jetbrains.com/plugin/6981-ini/versions
%global ini_version 211.6693.44
%global ini_id 115238

# https://plugins.jetbrains.com/plugin/7499-gittoolbox/versions
%global git_tool_box_version 203.5.8
%global git_tool_box_id 117592

# https://plugins.jetbrains.com/plugin/7495--ignore/versions
%global ignore_plugin_version 4.1.0
%global ignore_plugin_id 116929

# https://plugins.jetbrains.com/plugin/8182-rust/versions
%global rust_version 0.3.145.3797-211
%global rust_id 116769

Name:          %{appname}-plugins
Version:       2021.1.1
Release:       1%{?dist}

Summary:       Plugins for intelligent Python IDE
License:       ASL 2.0
URL:           http://www.jetbrains.com/pycharm/

Source0:       https://github.com/phracek/pycharm-community-edition/raw/master/copr-workaround.tar.xz
Source1:       https://plugins.jetbrains.com/files/8183/%{repmapper_id}/GitLink-%{repmapper_version}.zip#/GitLink-%{repmapper_version}.zip
Source2:       https://plugins.jetbrains.com/files/1800/%{dbnavigator_id}/DBN-20.0.zip#/DBN-%{dbnavigator_version}.zip
Source3:       https://plugins.jetbrains.com/files/7792/%{ansible_id}/intellij-ansible-%{ansible_version}.zip#/intellij-ansible-%{ansible_version}.zip
Source4:       https://plugins.jetbrains.com/files/7447/%{git_lab_integration_id}/gitlab-integration-plugin-%{git_lab_integration_version}.zip#/gitlab-integration-plugin-%{git_lab_integration_version}.zip
Source5:       https://plugins.jetbrains.com/files/7724/%{docker_integration_id}/Docker-%{docker_integration_version}.zip#/Docker-plugin-%{docker_integration_version}.zip
Source6:       https://plugins.jetbrains.com/files/7896/%{idea_multimarkdown_id}/idea-multimarkdown.%{idea_multimarkdown_version}.zip#/idea-multimarkdown-%{idea_multimarkdown_version}.zip
Source7:       https://plugins.jetbrains.com/files/164/%{ideavim_id}/IdeaVim-%{ideavim_version}.zip#/IdeaVim-%{ideavim_version}.zip
Source8:       https://plugins.jetbrains.com/files/6981/%{ini_id}/ini4idea-%{ini_version}.zip#/ini4idea-%{ini_version}.zip
Source9:       https://plugins.jetbrains.com/files/7499/%{git_tool_box_id}/GitToolBox-%{git_tool_box_version}.zip#/GitToolBox-%{git_tool_box_version}.zip
Source10:      https://plugins.jetbrains.com/files/7495/%{ignore_plugin_id}/.ignore-%{ignore_plugin_version}.zip#/GitIgnore-%{ignore_plugin_version}.zip
Source11:      https://plugins.jetbrains.com/files/8182/%{rust_id}/intellij-rust-%{rust_version}.zip#/intellij-rust-%{rust_version}.zip

Requires:      %{appname}%{?_isa} = %{?epoch:%{epoch}:}%{version}

ExclusiveArch: x86_64

%description
Intelligent Python IDE contains several plugins. This package
contains plugins like RemoteRepositoryMapper, GoLang, Markdown,
Idea Markdown, Intellij Ansible, GitLab integration plugin, etc.

%prep
%setup -q -c -n %{appname}-%{version} -T
%setup -q -n %{appname}-%{version} -D -T -a 1
%setup -q -n %{appname}-%{version} -D -T -a 2
%setup -q -n %{appname}-%{version} -D -T -a 3
%setup -q -n %{appname}-%{version} -D -T -a 4
%setup -q -n %{appname}-%{version} -D -T -a 5
%setup -q -n %{appname}-%{version} -D -T -a 6
%setup -q -n %{appname}-%{version} -D -T -a 7
%setup -q -n %{appname}-%{version} -D -T -a 8
%setup -q -n %{appname}-%{version} -D -T -a 9
%setup -q -n %{appname}-%{version} -D -T -a 10
%setup -q -n %{appname}-%{version} -D -T -a 11

%install
mkdir -p %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}

# Move all plugins to /usr/share/java/pycharm-community/plugins directory
cp -arf ./GitLink %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./DBNavigator %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./intellij-ansible %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./gitlab-integration-plugin %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./idea-multimarkdown %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./IdeaVim %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./ini4idea %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./GitToolBox %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./Docker %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./.ignore %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./intellij-rust %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/

%files
%{_javadir}/%{appname}/%{plugins_dir}/GitLink
%{_javadir}/%{appname}/%{plugins_dir}/DBNavigator
%{_javadir}/%{appname}/%{plugins_dir}/intellij-ansible
%{_javadir}/%{appname}/%{plugins_dir}/gitlab-integration-plugin
%{_javadir}/%{appname}/%{plugins_dir}/idea-multimarkdown
%{_javadir}/%{appname}/%{plugins_dir}/IdeaVim
%{_javadir}/%{appname}/%{plugins_dir}/ini4idea
%{_javadir}/%{appname}/%{plugins_dir}/GitToolBox
%{_javadir}/%{appname}/%{plugins_dir}/Docker
%{_javadir}/%{appname}/%{plugins_dir}/.ignore
%{_javadir}/%{appname}/%{plugins_dir}/intellij-rust

%changelog
* Sat Apr 24 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.1-1
- Updated plugins to latest supported releases.

* Mon Apr 05 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.5-2
- Marked plugins subpackage as arch-dependent.

* Mon Apr 05 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.5-1
- Updated plugins to latest supported releases.

* Sat Jan 30 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.3-1
- Updated plugins to latest supported releases.

* Thu Dec 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.2-2
- Fixed issue with the plugins subpackage.

* Thu Dec 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.2-1
- Updated plugins to latest supported releases.

* Tue Dec 22 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.1-1
- Updated plugins to latest supported releases.

* Fri Nov 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.2.4-1
- Updated plugins to latest supported releases.

* Mon Oct 19 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.2.3-1
- Updated plugins to latest supported releases.

* Sun Sep 20 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.2.2-1
- Updated plugins to latest supported releases.

* Wed Sep 02 2020 Petr Hracek <phracek@redhat.com> - 2020.2.1-2
- Fix typo in pycharm-community.app.xml file

* Thu Aug 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.2.1-1
- Updated plugins to latest supported releases.

* Thu Jul 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1.4-1
- Updated plugins to latest supported releases.

* Thu Jul 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1.3-1
- Updated plugins to latest supported releases.

* Thu Jun 04 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1.2-1
- Updated plugins to latest supported releases.

* Sun May 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1.1-1
- Updated plugins to latest supported releases.

* Mon Apr 13 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1-1
- Updated plugins to latest supported releases.

* Fri Mar 20 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3.4-1
- Updated plugins to latest supported releases.

* Mon Mar 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3.3-2
- Removed duplicates.

* Sun Feb 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3.3-1
- Updated plugins to latest supported releases.
