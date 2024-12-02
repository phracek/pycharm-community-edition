# setting some global constants
%global appname pycharm-community
%global plugins_dir plugins

# disable debuginfo subpackage
%global debug_package %{nil}

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
%global repmapper_version 4.5.2
%global repmapper_id 599893
%global repmapper_name GitLink
%global repmapper_archive %{repmapper_name}-%{repmapper_version}

# https://plugins.jetbrains.com/plugin/7792-yaml-ansible-support/versions # The latest support 2022.1.4
%global ansible_version 0.11.2
%global ansible_id 100135
%global ansible_name intellij-ansible
%global ansible_archive %{ansible_name}-%{ansible_version}

# https://plugins.jetbrains.com/plugin/12552-rpm-spec-file/versions
%global rpm_spec_file_version 2.2.0
%global rpm_spec_file_id 373650
%global rpm_spec_file_name intellij-rpmspec
%global rpm_spec_file_archive %{rpm_spec_file_name}-%{rpm_spec_file_version}

# https://plugins.jetbrains.com/plugin/7724-docker/versions
%global docker_integration_version 243.22562.74
%global docker_integration_id 640921
%global docker_integration_name clouds-docker-impl
%global docker_integration_archive %{docker_integration_name}-%{docker_integration_version}

# https://plugins.jetbrains.com/plugin/164-ideavim/versions
%global ideavim_version 2.17.0
%global ideavim_id 635855
%global ideavim_name IdeaVIM
%global ideavim_archive %{ideavim_name}-%{ideavim_version}

# https://plugins.jetbrains.com/plugin/6981-ini/versions
%global ini_version 243.22562.74
%global ini_id 640935
%global ini_name ini
%global ini_archive %{ini_name}-%{ini_version}

# https://plugins.jetbrains.com/plugin/7566-settings-repository/versions
%global settings_repository_version 243.21565.122
%global settings_repository_id 630048
%global settings_repository_name settingsRepository
%global settings_repository_archive %{settings_repository_name}-%{settings_repository_version}

# https://plugins.jetbrains.com/plugin/7495--ignore/versions
%global ignore_plugin_version 4.5.4
%global ignore_plugin_id 619859
%global ignore_plugin_name ignore
%global ignore_plugin_archive ignore-%{ignore_plugin_version}

Name:          %{appname}-plugins
Version:       2024.3
Release:       4%{?dist}

Summary:       Plugins for intelligent Python IDE
License:       Apache-2.0
URL:           http://www.jetbrains.com/pycharm/

Source0:       https://github.com/phracek/pycharm-community-edition/raw/master/copr-workaround.tar.xz
Source1:       https://plugins.jetbrains.com/files/8183/%{repmapper_id}/%{repmapper_archive}.zip#/%{repmapper_name}-%{repmapper_version}.zip
Source2:       https://plugins.jetbrains.com/files/7792/%{ansible_id}/%{ansible_archive}.zip#/%{ansible_name}-%{ansible_version}.zip
Source3:       https://plugins.jetbrains.com/files/12552/%{rpm_spec_file_id}/%{rpm_spec_file_archive}.zip#/%{rpm_spec_file_name}-%{rpm_spec_file_version}.zip
Source4:       https://plugins.jetbrains.com/files/7724/%{docker_integration_id}/%{docker_integration_archive}.zip#/%{docker_integration_name}-%{docker_integration_version}.zip
Source5:       https://plugins.jetbrains.com/files/164/%{ideavim_id}/%{ideavim_archive}.zip#/%{ideavim_name}-%{ideavim_version}.zip
Source6:       https://plugins.jetbrains.com/files/6981/%{ini_id}/%{ini_archive}.zip#/%{ini_name}-%{ini_version}.zip
Source7:       https://plugins.jetbrains.com/files/7566/%{settings_repository_id}/%{settings_repository_archive}.zip#/%{settings_repository_name}-%{settings_repository_version}.zip
Source8:       https://plugins.jetbrains.com/files/7495/%{ignore_plugin_id}/%{ignore_plugin_archive}.zip#/%{ignore_plugin_name}-%{ignore_plugin_version}.zip
#Source9:       https://plugins.jetbrains.com/files/1800/%{dbnavigator_id}/%{dbnavigator_archive}.zip#/%{dbnavigator_name}-%{dbnavigator_version}.zip

%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: javapackages-tools
%else
BuildRequires: javapackages-filesystem
%endif

Requires:      %{appname}%{?_isa} = %{?epoch:%{epoch}:}%{version}

ExclusiveArch: x86_64

%description
Intelligent Python IDE contains several plugins. This package
contains plugins like RemoteRepositoryMapper, GoLang, SPEC,
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

%install
mkdir -p %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}

# Move all plugins to /usr/share/java/pycharm-community/plugins directory
cp -arf ./%{repmapper_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ansible_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{rpm_spec_file_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{docker_integration_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ideavim_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ini_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{settings_repository_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ignore_plugin_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/

%files
%{_javadir}/%{appname}/%{plugins_dir}/%{repmapper_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ansible_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{rpm_spec_file_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{docker_integration_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ideavim_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ini_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{settings_repository_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ignore_plugin_name}

%changelog
* Mon Dec 02 2024 Petr Hracek <phracek@redhat.com> - 2024.3-4
- Fix changelog

* Mon Dec 02 2024 Petr Hracek <phracek@redhat.com> - 2024.3-3
- add global debug_package directive

* Mon Dec 02 2024 Petr Hracek <phracek@redhat.com> - 2024.3-2
- Fix plugins

* Mon Dec 02 2024 Petr Hracek <phracek@redhat.com> - 2024.3-1
- Update plugins to latest supported release
- Rust is deprecated

* Mon Mar 04 2024 Petr Hracek <phracek@redhat.com> - 2023.3.3-4
- Fix import sources for ppc64le

* Mon Mar 04 2024 Petr Hracek <phracek@redhat.com> - 2023.3.3-3
- Add support for ppc64le

* Mon Feb 26 2024 Petr Hracek <phracek@redhat.com> - 2023.3.3-2
- Fix typo in changelog

* Mon Feb 26 2024 Petr Hracek <phracek@redhat.com> - 2023.3.3-1
- Updated plugins to latest supported releases.

* Thu Jul 13 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.1.4-1
- Updated plugins to latest supported releases.

* Thu Jun 22 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.1.3-1
- Updated plugins to latest supported releases.

* Tue May 23 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.1.2-1
- Updated plugins to latest supported releases.

* Tue Apr 04 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.1-2
- Fixed dependency issue on EPEL.

* Fri Mar 31 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.1-1
- Updated plugins to latest supported releases.
- Removed GitToolBox plugin (requires a paid subscription now).
- Added Settings Repository plugin.

* Tue Mar 14 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.3.3-1
- Updated plugins to latest supported releases.

* Sat Feb 04 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.3.2-1
- Updated plugins to latest supported releases.

* Thu Dec 29 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.3.1-1
- Updated plugins to latest supported releases.

* Fri Dec 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.3-1
- Updated plugins to latest supported releases.

* Sat Oct 15 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.2.3-1
- Updated plugins to latest supported releases.

* Sat Sep 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.2.2-1
- Updated plugins to latest supported releases.

* Tue Aug 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.2.1-1
- Updated plugins to latest supported releases.

* Tue Jul 26 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1.4-1
- Updated to latest snapshot.

* Thu Jun 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1.3-1
- Updated plugins to latest supported releases.

* Thu Jun 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1.2-1
- Updated plugins to latest supported releases.

* Thu May 12 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1.1-1
- Updated plugins to latest supported releases.
- Removed no longer supported by upstream plugins.

* Wed Apr 20 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1-1
- Updated plugins to latest supported releases.

* Wed Mar 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.3.3-3
- Rebuilt.

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
