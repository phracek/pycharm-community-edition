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
%global repmapper_version 4.5.3
%global repmapper_id 839423
%global repmapper_name GitLink
%global repmapper_archive %{repmapper_name}-%{repmapper_version}

# https://plugins.jetbrains.com/plugin/12552-rpm-spec-file/versions
%global rpm_spec_file_version 2.3.0
%global rpm_spec_file_id 810018
%global rpm_spec_file_name intellij-rpmspec
%global rpm_spec_file_archive %{rpm_spec_file_name}-%{rpm_spec_file_version}

# https://plugins.jetbrains.com/plugin/7724-docker/versions
%global docker_integration_version 252.27397.129
%global docker_integration_id 884806
%global docker_integration_name clouds-docker-impl
%global docker_integration_archive %{docker_integration_name}-%{docker_integration_version}

# https://plugins.jetbrains.com/plugin/164-ideavim/versions
%global ideavim_version 2.27.2
%global ideavim_id 835262
%global ideavim_name IdeaVIM
%global ideavim_archive %{ideavim_name}-%{ideavim_version}

# https://plugins.jetbrains.com/plugin/6981-ini/versions
%global ini_version 252.27397.129
%global ini_id 884814
%global ini_name ini
%global ini_archive %{ini_name}-%{ini_version}

# https://plugins.jetbrains.com/plugin/7566-settings-repository/versions
%global settings_repository_version 252.23892.201
%global settings_repository_id 796427
%global settings_repository_name settingsRepository
%global settings_repository_archive %{settings_repository_name}-%{settings_repository_version}

# https://plugins.jetbrains.com/plugin/7495--ignore/versions
%global ignore_plugin_version 4.5.6
%global ignore_plugin_id 678216
%global ignore_plugin_name ignore
%global ignore_plugin_archive ignore-%{ignore_plugin_version}

# https://plugins.jetbrains.com/plugin/9525--env-files/versions
%global env_files_version 252.23892.201
%global env_files_id 796325
%global env_files_name dotenv
%global env_files_archive %{env_files_name}-%{env_files_version}

# https://plugins.jetbrains.com/plugin/22282-jetbrains-ai-assistant/versions
%global ai_assistant_version 252.27397.130
%global ai_assistant_id 884745
%global ai_assistant_name ml-llm
%global ai_assistant_archive %{ai_assistant_name}-%{ai_assistant_version}

Name:          %{appname}-plugins
Version:       2025.2.4
Release:       1%{?dist}

Summary:       Plugins for intelligent Python IDE
License:       Apache-2.0
URL:           http://www.jetbrains.com/pycharm/

Source0:       https://github.com/phracek/pycharm-community-edition/raw/master/copr-workaround.tar.xz
Source1:       https://plugins.jetbrains.com/files/8183/%{repmapper_id}/%{repmapper_archive}.zip#/%{repmapper_name}-%{repmapper_version}.zip
Source2:       https://plugins.jetbrains.com/files/12552/%{rpm_spec_file_id}/%{rpm_spec_file_archive}.zip#/%{rpm_spec_file_name}-%{rpm_spec_file_version}.zip
Source3:       https://plugins.jetbrains.com/files/7724/%{docker_integration_id}/%{docker_integration_archive}.zip#/%{docker_integration_name}-%{docker_integration_version}.zip
Source4:       https://plugins.jetbrains.com/files/164/%{ideavim_id}/%{ideavim_archive}.zip#/%{ideavim_name}-%{ideavim_version}.zip
Source5:       https://plugins.jetbrains.com/files/6981/%{ini_id}/%{ini_archive}.zip#/%{ini_name}-%{ini_version}.zip
Source6:       https://plugins.jetbrains.com/files/7566/%{settings_repository_id}/%{settings_repository_archive}.zip#/%{settings_repository_name}-%{settings_repository_version}.zip
Source7:       https://plugins.jetbrains.com/files/7495/%{ignore_plugin_id}/%{ignore_plugin_archive}.zip#/%{ignore_plugin_name}-%{ignore_plugin_version}.zip
Source8:       https://plugins.jetbrains.com/files/9525/%{env_files_id}/%{env_files_archive}.zip#/%{env_files_name}-%{env_files_version}.zip
Source9:       https://plugins.jetbrains.com/files/22282/%{ai_assistant_id}/%{ai_assistant_archive}.zip#/%{ai_assistant_name}-%{ai_assistant_version}.zip

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
%setup -q -n %{appname}-%{version} -D -T -a 9

%install
mkdir -p %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}

# Move all plugins to /usr/share/java/pycharm-community/plugins directory
cp -arf ./%{repmapper_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{rpm_spec_file_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{docker_integration_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ideavim_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ini_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{settings_repository_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ignore_plugin_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{env_files_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./%{ai_assistant_name} %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/

%files
%{_javadir}/%{appname}/%{plugins_dir}/%{repmapper_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{rpm_spec_file_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{docker_integration_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ideavim_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ini_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{settings_repository_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ignore_plugin_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{env_files_name}
%{_javadir}/%{appname}/%{plugins_dir}/%{ai_assistant_name}

%changelog
* Fri Oct 31 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.2.4-1
- Docker from 252.26830.99 to 252.27397.129.
- Ini from 252.26830.99 to 252.27397.129.
- JetBrains AI Assistant from 252.26830.99 to 252.27397.130.

* Fri Oct 03 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.2.3-1
- GitLink from 4.5.2 to 4.5.3.
- Docker from 252.23892.515 to 252.26830.99.
- Ini from 252.23892.449 to 252.26830.99.
- JetBrains AI Assistant from 252.23892.530 to 252.26830.99.

* Mon Aug 25 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.2.0.1-1
- Docker from 252.23892.419 to 252.23892.515.
- IdeaVim from 2.26.0 to 2.27.2.
- Ini from 252.23892.419 to 252.23892.449.
- JetBrains AI Assistant from 252.23892.419 to 252.23892.530.
- Remove YAML/Ansible support. Since the last supported PyCharm version is 2022.1.4.

* Tue Aug 05 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.2-1
- RPM SPEC File from 2.2.0 to 2.3.0.
- Docker from 251.26927.70 to 252.23892.419.
- Ini from 251.26927.70 to 252.23892.419.
- Settings Repository from 251.25410.28 to 252.23892.201.
- .env files from 251.23774.318 to 252.23892.201.
- JetBrains AI Assistant from 251.26094.80.26 to 252.23892.419.

* Tue Jul 22 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.1.3.1-1
- Docker from 251.25410.67 to 251.26927.70.
- IdeaVim from 2.24.0 to 2.26.0.
- Ini from 251.25410.24 to 251.26927.70.
- JetBrains AI Assistant from 251.23774.42.28.7 to 251.26094.80.26.

* Mon May 19 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.1.1-1
- Docker from 251.23774.426 to 251.25410.67.
- IdeaVim from 2.22.0 to 2.24.0.
- Ini from 251.23774.318 to 251.25410.24.
- Settings Repository from 251.23774.318 to 251.25410.28.
- JetBrains AI Assistant from 251.23774.42.28.2 to 251.23774.42.28.7.

* Tue Apr 22 2025 Petr Hracek <phracek@redhat.com> - 2025.1-4
- Fix the archive typo in env-files and JetBrains AI Assistant

* Tue Apr 22 2025 Petr Hracek <phracek@redhat.com> - 2025.1-3
- Fix typo in env-files definition

* Tue Apr 22 2025 Petr Hracek <phracek@redhat.com> - 2025.1-2
- Added plugin env-files
- Added plugin JetBrains AI Assistant

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
