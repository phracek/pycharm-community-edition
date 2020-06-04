# dont repack jars
%global __jar_repack %{nil}

%global appname pycharm-community
%global plugins_dir plugins

%global ansible_version 0.9.5
%global ansible_id 35585

%global bash_version 1.7.18.201
%global bash_id 85527

%global repmapper_version 3.3.3
%global repmapper_id 79011

%global docker_integration_version 201.7846.6
%global docker_integration_id 86237

%global git_lab_integration_version 1.1.2
%global git_lab_integration_id 52232

%global idea_multimarkdown_version 3.0.197.72
%global idea_multimarkdown_id 78997

%global ideavim_version 0.57
%global ideavim_id 85009

%global ini_version 201.6668.60
%global ini_id 82401

%global git_tool_box_version 201.3.1
%global git_tool_box_id 87151

%global ignore_plugin_version 3.2.3.201
%global ignore_plugin_id 83042

%global dbnavigator_version 3.2.0627.0
%global dbnavigator_id 84035

%global rust_version 0.2.123.3132-201
%global rust_id 87728

Name:          %{appname}-plugins
Version:       2020.1.2
Release:       1%{?dist}

Summary:       Plugins for intelligent Python IDE
License:       ASL 2.0
URL:           http://www.jetbrains.com/pycharm/

Source0:       https://plugins.jetbrains.com/files/4230/%{bash_id}/BashSupport-%{bash_version}.zip#/BashSupport-%{bash_version}.zip
Source1:       https://plugins.jetbrains.com/files/8183/%{repmapper_id}/GitLink-%{repmapper_version}.zip#/GitLink-%{repmapper_version}.zip
Source2:       https://plugins.jetbrains.com/files/1800/%{dbnavigator_id}/DBN-18.0.zip#/DBN-%{dbnavigator_version}.zip
Source3:       https://plugins.jetbrains.com/files/7792/%{ansible_id}/intellij-ansible-%{ansible_version}.zip#/intellij-ansible-%{ansible_version}.zip
Source4:       https://plugins.jetbrains.com/files/7447/%{git_lab_integration_id}/gitlab-integration-plugin-%{git_lab_integration_version}.zip#/gitlab-integration-plugin-%{git_lab_integration_version}.zip
Source5:       https://plugins.jetbrains.com/files/7724/%{docker_integration_id}/Docker.zip#/Docker-plugin-%{docker_integration_version}.zip
Source6:       https://plugins.jetbrains.com/files/7896/%{idea_multimarkdown_id}/idea-multimarkdown.%{idea_multimarkdown_version}.zip#/idea-multimarkdown-%{idea_multimarkdown_version}.zip
Source7:       https://plugins.jetbrains.com/files/164/%{ideavim_id}/IdeaVim-%{ideavim_version}.zip#/IdeaVim-%{ideavim_version}.zip
Source8:       https://plugins.jetbrains.com/files/6981/%{ini_id}/ini4idea.zip#/ini4idea-%{ini_version}.zip
Source9:       https://plugins.jetbrains.com/files/7499/%{git_tool_box_id}/GitToolBox-%{git_tool_box_version}.zip#/GitToolBox-%{git_tool_box_version}.zip
Source10:      https://plugins.jetbrains.com/files/7495/%{ignore_plugin_id}/idea-gitignore-%{ignore_plugin_version}.zip#/GitIgnore-%{ignore_plugin_version}.zip
Source11:      https://plugins.jetbrains.com/files/8182/%{rust_id}/intellij-rust-%{rust_version}.zip#/intellij-rust-%{rust_version}.zip

Requires:      %{appname} = %{version}
BuildArch:     noarch

%description
Intelligent Python IDE contains several plugins. This package
contains plugins like BashSupport, RemoteRepositoryMapper, GoLang, Markdown,
Idea Markdown, Intellij Ansible, GitLab integration plugin, etc.

%prep
%setup -q -c -n %{appname}-%{version} -T
%setup -q -n %{appname}-%{version} -D -T -a 0
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
cp -arf ./BashSupport %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./GitLink %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./DBNavigator %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./intellij-ansible %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./gitlab-integration-plugin %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./idea-multimarkdown %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./IdeaVim %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./ini4idea %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./GitToolBox %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./Docker %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./idea-gitignore %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/
cp -arf ./intellij-rust %{buildroot}%{_javadir}/%{appname}/%{plugins_dir}/

%files
%{_javadir}/%{appname}/%{plugins_dir}/*

%changelog
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
