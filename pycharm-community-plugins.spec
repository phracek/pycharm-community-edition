# setting some global constants
%global appname pycharm-community
%global plugins_dir plugins

# Disable build-id symlinks to avoid conflicts
%global _build_id_links none
# don't strip bundled binaries
%global __strip /bin/true
# dont repack jars
%global __jar_repack %{nil}
# disable rpath checks
%define __brp_check_rpaths %{nil}
# do not bytecompile python scripts
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
# do not automatically detect and export provides and dependencies on bundled libraries and executables
%global __provides_exclude_from %{_javadir}/%{appname}/%{plugins_dir}/.*
%global __requires_exclude_from %{_javadir}/%{appname}/%{plugins_dir}/.*

# https://plugins.jetbrains.com/plugin/8183-gitlink/versions
%global repmapper_version 3.3.6
%global repmapper_id 146766
%global repmapper_name GitLink
%global repmapper_archive %{repmapper_name}-%{repmapper_version}

# https://plugins.jetbrains.com/plugin/1800-database-navigator/versions
%global dbnavigator_version 3.3.1555.0
%global dbnavigator_id 159245
%global dbnavigator_name DBNavigator
%global dbnavigator_archive DBN-20.0

# https://plugins.jetbrains.com/plugin/7792-yaml-ansible-support/versions
%global ansible_version 0.11.2
%global ansible_id 100135
%global ansible_name intellij-ansible
%global ansible_archive %{ansible_name}-%{ansible_version}

# https://plugins.jetbrains.com/plugin/12552-rpm-spec-file/versions
%global rpm_spec_file_version 2.0.0
%global rpm_spec_file_id 153070
%global rpm_spec_file_name intellij-rpmspec
%global rpm_spec_file_archive %{rpm_spec_file_name}-%{rpm_spec_file_version}

# https://plugins.jetbrains.com/plugin/7724-docker/versions
%global docker_integration_version 213.7172.6
%global docker_integration_id 160440
%global docker_integration_name Docker
%global docker_integration_archive %{docker_integration_name}-%{docker_integration_version}

# https://plugins.jetbrains.com/plugin/7896-markdown-navigator-enhanced/versions
%global idea_multimarkdown_version 3.0.202.112
%global idea_multimarkdown_id 97563
%global idea_multimarkdown_name idea-multimarkdown
%global idea_multimarkdown_archive %{idea_multimarkdown_name}.%{idea_multimarkdown_version}

# https://plugins.jetbrains.com/plugin/164-ideavim/versions
%global ideavim_version 1.10.0
%global ideavim_id 158788
%global ideavim_name IdeaVim
%global ideavim_archive %{ideavim_name}-%{ideavim_version}

# https://plugins.jetbrains.com/plugin/6981-ini/versions
%global ini_version 213.5744.190
%global ini_id 147080
%global ini_name ini4idea
%global ini_archive %{ini_name}-%{ini_version}

# https://plugins.jetbrains.com/plugin/7499-gittoolbox/versions
%global git_tool_box_version 212.8.8
%global git_tool_box_id 160954
%global git_tool_box_name gittoolbox
%global git_tool_box_archive %{git_tool_box_name}-%{git_tool_box_version}

# https://plugins.jetbrains.com/plugin/7495--ignore/versions
%global ignore_plugin_version 4.3.0
%global ignore_plugin_id 141256
%global ignore_plugin_name .ignore
%global ignore_plugin_archive ignore-%{ignore_plugin_version}

# https://plugins.jetbrains.com/plugin/8182-rust/versions
%global rust_version 0.4.166.4486-213
%global rust_id 161597
%global rust_name intellij-rust
%global rust_archive %{rust_name}-%{rust_version}

Name:          %{appname}-plugins
Version:       2021.3.3
Release:       2%{?dist}

Summary:       Plugins for intelligent Python IDE
License:       ASL 2.0
URL:           http://www.jetbrains.com/pycharm/

Source0:       https://github.com/phracek/pycharm-community-edition/raw/master/copr-workaround.tar.xz
Source1:       https://plugins.jetbrains.com/files/8183/%{repmapper_id}/%{repmapper_archive}.zip#/%{repmapper_name}-%{repmapper_version}.zip
Source2:       https://plugins.jetbrains.com/files/1800/%{dbnavigator_id}/%{dbnavigator_archive}.zip#/%{dbnavigator_name}-%{dbnavigator_version}.zip
Source3:       https://plugins.jetbrains.com/files/7792/%{ansible_id}/%{ansible_archive}.zip#/%{ansible_name}-%{ansible_version}.zip
Source4:       https://plugins.jetbrains.com/files/12552/%{rpm_spec_file_id}/%{rpm_spec_file_archive}.zip#/%{rpm_spec_file_name}-%{rpm_spec_file_version}.zip
Source5:       https://plugins.jetbrains.com/files/7724/%{docker_integration_id}/%{docker_integration_archive}.zip#/%{docker_integration_name}-%{docker_integration_version}.zip
Source6:       https://plugins.jetbrains.com/files/7896/%{idea_multimarkdown_id}/%{idea_multimarkdown_archive}.zip#/%{idea_multimarkdown_name}-%{idea_multimarkdown_version}.zip
Source7:       https://plugins.jetbrains.com/files/164/%{ideavim_id}/%{ideavim_archive}.zip#/%{ideavim_name}-%{ideavim_version}.zip
Source8:       https://plugins.jetbrains.com/files/6981/%{ini_id}/%{ini_archive}.zip#/%{ini_name}-%{ini_version}.zip
Source9:       https://plugins.jetbrains.com/files/7499/%{git_tool_box_id}/%{git_tool_box_archive}.zip#/%{git_tool_box_name}-%{git_tool_box_version}.zip
Source10:      https://plugins.jetbrains.com/files/7495/%{ignore_plugin_id}/%{ignore_plugin_archive}.zip#/%{ignore_plugin_name}-%{ignore_plugin_version}.zip
Source11:      https://plugins.jetbrains.com/files/8182/%{rust_id}/%{rust_archive}.zip#/%{rust_name}-%{rust_version}.zip

%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: javapackages-tools
%else
BuildRequires: javapackages-filesystem
%endif

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
cp -arf ./%{repmapper_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{dbnavigator_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ansible_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{rpm_spec_file_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{docker_integration_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{idea_multimarkdown_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ideavim_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ini_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{git_tool_box_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ignore_plugin_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{rust_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/

%files
%{_javadir}/%{appname}/%{plugins_dir}/%{repmapper_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{dbnavigator_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ansible_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{rpm_spec_file_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{docker_integration_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{idea_multimarkdown_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ideavim_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ini_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{git_tool_box_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ignore_plugin_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{rust_name}

%changelog
* Wed Mar 23 2022 Petr Hracek <phracek@redhat.com> - 2021.3.3-2
- Added png icons to resolve https://pagure.io/copr/copr/issue/2039.

* Fri Mar 18 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.3.3-1
- Updated plugins to latest supported releases.

* Mon Jan 31 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.3.2-1
- Updated plugins to latest supported releases.

* Tue Jan 04 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.3.1-1
- Updated plugins to latest supported releases.

* Sat Nov 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2.3-2
- Fixed issue with multilib on Fedora 35+.

* Mon Oct 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2.3-1
- Updated plugins to latest supported releases.

* Wed Sep 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2.2-1
- Updated plugins to latest supported releases.

* Fri Aug 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2.1-1
- Updated plugins to latest supported releases.

* Fri Jul 30 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2-3
- Fixed issues with native indexer.
- Removed more bundled trialware plugins.

* Thu Jul 29 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2-2
- Fixed issue with dependencies.

* Thu Jul 29 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2-1
- Updated plugins to latest supported releases.

* Wed Jun 30 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.3-1
- Updated plugins to latest supported releases.
- Removed obsolete GitLab integration plugin.
- Added RPM SPEC File plugin.

* Thu Jun 03 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.2-2
- Fixed Rawhide build.

* Thu Jun 03 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.2-1
- Updated plugins to latest supported releases.

* Sat Apr 24 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.1-3
- Removed trialware plugin CodeWithMe.

* Sat Apr 24 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.1-2
- Allow simultaneous installation of Community and Professional editions.

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
