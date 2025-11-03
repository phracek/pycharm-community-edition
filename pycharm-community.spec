# setting some global constants
%global appname pycharm

# disable debuginfo subpackage
%global debug_package %{nil}
# Disable build-id symlinks to avoid conflicts
%global _build_id_links none
# don't strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%global __strip /bin/true
# dont repack jars
%global __jar_repack %{nil}
# disable rpath checks
%define __brp_check_rpaths %{nil}
# there are some python 2 and python 3 scripts so there is no way out to bytecompile them ^_^
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
# do not automatically detect and export provides and dependencies on bundled libraries and executables
%global __provides_exclude_from %{_javadir}/%{name}/jbr/.*|%{_javadir}/%{name}/lib/.*|%{_javadir}/%{name}/plugins/.*
%global __requires_exclude_from %{_javadir}/%{name}/jbr/.*|%{_javadir}/%{name}/lib/.*|%{_javadir}/%{name}/plugins/.*

Name:          %{appname}-community
Version:       2025.2.4
Release:       1%{?dist}

Summary:       Intelligent Python IDE
License:       Apache-2.0
URL:           https://www.jetbrains.com/%{appname}/

Source0:       https://download.jetbrains.com/python/%{name}-%{version}.tar.gz

Source101:     %{name}.xml
Source102:     %{name}.desktop
Source103:     %{name}.metainfo.xml

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: librsvg2-tools
BuildRequires: python3-devel

Requires:      hicolor-icon-theme

%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: javapackages-tools
Requires:      javapackages-tools
%else
BuildRequires: javapackages-filesystem
Requires:      javapackages-filesystem
%endif

ExclusiveArch: x86_64 aarch64 ppc64le

Obsoletes:     %{name}-jre < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The intelligent Python IDE with unique code assistance and analysis,
for productive Python development on all levels

%package doc
Summary:       Documentation for intelligent Python IDE
BuildArch:     noarch
Requires:      %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description doc
This package contains documentation for the Intelligent Python IDE.

%prep
%autosetup

# Removing trialware plugins...
rm -rf plugins/{cwm-plugin,cwm-plugin-projector,marketplace,space}

# Patching shebangs...
%if 0%{?fedora}
%py3_shebang_fix bin
%else
find bin -type f -name "*.py" -exec sed -e 's@/usr/bin/env python.*@%{__python3}@g' -i "{}" \;
%endif

%install
# Installing application...
install -d %{buildroot}%{_javadir}/%{name}
cp -arf ./{bin,jbr,lib,plugins,build.txt,product-info.json} %{buildroot}%{_javadir}/%{name}/

# Installing icons...
install -d %{buildroot}%{_datadir}/pixmaps
install -m 0644 -p bin/%{appname}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 0644 -p bin/%{appname}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Creating additional PNG icons on the fly...
for size in 16 22 24 32 48 64 128 256; do
    dest=%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
    install -d ${dest}
    rsvg-convert -w ${size} -h ${size} bin/%{appname}.svg -o ${dest}/%{name}.png
    chmod 0644 ${dest}/%{name}.png
    touch -r bin/%{appname}.svg ${dest}/%{name}.png
done

# Installing metainfo...
install -d %{buildroot}%{_metainfodir}
install -m 0644 -p %{SOURCE103} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

# Installing launcher...
install -d %{buildroot}%{_bindir}
ln -s %{_javadir}/%{name}/bin/%{appname} %{buildroot}%{_bindir}/%{name}

# Installing desktop file...
install -d %{buildroot}%{_datadir}/applications
install -m 0644 -p %{SOURCE102} %{buildroot}%{_datadir}/applications/%{name}.desktop

# Installing mime package...
install -d %{buildroot}%{_datadir}/mime/packages
install -m 0644 -p %{SOURCE101} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

# Patch Python shebangs
tail -n +2 %{buildroot}%{_datadir}/java/pycharm-community/plugins/python-ce/helpers/pycodestyle-2.10.0.py
sed -i '1 i #!/usr/bin/env python3' %{buildroot}%{_datadir}/java/pycharm-community/plugins/python-ce/helpers/pycodestyle-2.10.0.py

tail -n +2 %{buildroot}%{_datadir}/java/pycharm-community/plugins/python-ce/helpers/pycodestyle.py
sed -i '1 i #!/usr/bin/env python3' %{buildroot}%{_datadir}/java/pycharm-community/plugins/python-ce/helpers/pycodestyle.py

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license license/*
%{_javadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/%{name}.metainfo.xml

%files doc
%doc help/
%doc Install-Linux-tar.txt

%changelog
* Fri Oct 31 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.2.4-1
- Update to 2025.2.4

* Fri Oct 03 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.2.3-1
- Update to 2025.2.3

* Mon Aug 25 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.2.0.1-1
- Update to 2025.2.0.1

* Tue Aug 05 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.2-1
- Update to 2025.2

* Tue Jul 22 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.1.3.1-1
- Update to 2025.1.3.1

* Mon May 19 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.1.1-1
- Update to 2025.1.1

* Tue Apr 22 2025 Petr Hracek <phracek@redhat.com> - 2025.1-4
- Fix the archive typo in env-files and JetBrains AI Assistant

* Tue Apr 22 2025 Petr Hracek <phracek@redhat.com>  - 2025.1-3
- Fix typo in env-files

* Tue Apr 22 2025 Petr Hracek <phracek@redhat.com>  - 2025.1-2
- Add plugin env-files
- Add plugin JetBrains AI Assistant
- Fix plugins

* Fri Apr 18 2025 Elkhan Mammadli <elkhan.mammadli@protonmail.com> - 2025.1-1
- Fix warning about using native launcher.
- Update to 2025.1.

* Mon Dec 02 2024 Petr Hracek <phracek@redhat.com> - 2024.3-4
- Fix changelog

* Mon Dec 02 2024 Petr Hracek <phracek@redhat.com> - 2024.3-3
- add global debug_package directive

* Mon Dec 02 2024 Petr Hracek <phracek@redhat.com> - 2024.3-2
- Fix plugins

* Mon Dec 02 2024 Petr Hracek <phracek@redhat.com> - 2024.3-1
- Updated to version 2024.3

* Mon Mar 04 2024 Petr Hracek <phracek@redhat.com> - 2023.3.3-4
- Fix import sources for ppc64le

* Mon Mar 04 2024 Petr Hracek <phracek@redhat.com> - 2023.3.3-3
- Add support for ppc64le

* Mon Feb 26 2024 Petr Hracek <phracek@redhat.com> - 2023.3.3-2
- Fix typo in changelog

* Mon Feb 26 2024 Petr Hracek <phracek@redhat.com> - 2023.3.3-1
- Updated to version 2023.3.3.

* Thu Jul 13 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.1.4-1
- Updated to version 2023.1.4.

* Thu Jun 22 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.1.3-1
- Updated to version 2023.1.3.

* Tue May 23 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.1.2-1
- Updated to version 2023.1.2.

* Tue Apr 04 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.1-2
- Fixed dependency issue on EPEL.

* Fri Mar 31 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2023.1-1
- Updated to version 2023.1.

* Tue Mar 14 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.3.3-1
- Updated to version 2022.3.3.

* Sat Feb 04 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.3.2-1
- Updated to version 2022.3.2.

* Thu Dec 29 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.3.1-1
- Updated to version 2022.3.1.

* Fri Dec 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.3-1
- Updated to version 2022.3.

* Sat Oct 15 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.2.3-1
- Updated to version 2022.2.3.

* Sat Sep 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.2.2-1
- Updated to version 2022.2.2.

* Tue Aug 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.2.1-1
- Updated to version 2022.2.1.

* Tue Jul 26 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1.4-1
- Updated to version 2022.1.4.

* Thu Jun 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1.3-1
- Updated to version 2022.1.3.

* Thu Jun 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1.2-1
- Updated to version 2022.1.2.

* Thu May 12 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1.1-1
- Updated to version 2022.1.1.

* Wed Apr 20 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1-1
- Updated to version 2022.1.

* Wed Mar 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.3.3-3
- Rebuilt.

* Wed Mar 23 2022 Petr Hracek <phracek@redhat.com> - 2021.3.3-2
- Added png icons to resolve https://pagure.io/copr/copr/issue/2039.

* Fri Mar 18 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.3.3-1
- Updated to version 2021.3.3.

* Mon Jan 31 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.3.2-1
- Updated to version 2021.3.2.

* Tue Jan 04 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.3.1-1
- Updated to version 2021.3.1.

* Sat Nov 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2.3-2
- Fixed issue with multilib on Fedora 35+.

* Mon Oct 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2.3-1
- Updated to version 2021.2.3.

* Wed Sep 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2.2-1
- Updated to version 2021.2.2.

* Fri Aug 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2.1-1
- Updated to version 2021.2.1.

* Fri Jul 30 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2-3
- Fixed issues with native indexer.
- Removed more bundled trialware plugins.

* Thu Jul 29 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2-2
- Fixed issue with dependencies.

* Thu Jul 29 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.2-1
- Updated to version 2021.2.

* Wed Jun 30 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.3-1
- Updated to version 2021.1.3.

* Thu Jun 03 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.2-2
- Fixed Rawhide build.

* Thu Jun 03 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.2-1
- Updated to version 2021.1.2.

* Sat Apr 24 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.1-3
- Removed trialware plugin CodeWithMe.

* Sat Apr 24 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.1-2
- Allow simultaneous installation of Community and Professional editions.

* Sat Apr 24 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.1.1-1
- Updated to version 2021.1.1.
- Performed major SPEC cleanup.

* Mon Apr 05 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.5-2
- Marked plugins subpackage as arch-dependent.

* Mon Apr 05 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.5-1
- Updated to version 2020.3.5.

* Sat Jan 30 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.3-1
- Updated to version 2020.3.3.

* Thu Dec 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.2-2
- Fixed issue with the plugins subpackage.

* Thu Dec 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.2-1
- Updated to version 2020.3.2.

* Tue Dec 22 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.3.1-1
- Updated to version 2020.3.1.

* Fri Nov 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.2.4-1
- Updated to version 2020.2.4.

* Mon Oct 19 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.2.3-1
- Updated to version 2020.2.3.

* Sun Sep 20 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.2.2-1
- Updated to version 2020.2.2.

* Wed Sep 02 2020 Petr Hracek <phracek@redhat.com> - 2020.2.1-2
- Fix typo in pycharm-community.app.xml

* Thu Aug 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.2.1-1
- Updated to version 2020.2.1.

* Thu Jul 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1.4-1
- Updated to version 2020.1.4.

* Thu Jul 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1.3-1
- Updated to version 2020.1.3.

* Thu Jun 04 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1.2-1
- Updated to version 2020.1.2.

* Sun May 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1.1-1
- Updated to version 2020.1.1.

* Mon Apr 13 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1-1
- Updated to version 2020.1.

* Fri Mar 20 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3.4-1
- Updated to version 2019.3.4.

* Sun Feb 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3.3-1
- Updated to version 2019.3.3.

* Wed Jan 22 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3.2-1
- Updated to version 2019.3.2.
- Updated plugins.

* Fri Dec 20 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3.1-1
- Updated to version 2019.3.1.
- Updated plugins.

* Wed Nov 27 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.2.5-1
- Updated to version 2019.2.5.
- Updated plugins.

* Thu Nov 14 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.2.4-2
- Updated plugins.
- Fixed bogus date in changelog.

* Tue Nov 05 2019 Petr Hracek <phracek@redhat.com> - 2019.2.4-1
- Update to version 2019.2.4

* Thu Sep 26 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.2.3-1
- Updated to version 2019.2.3.
- Updated plugins.

* Wed Sep 11 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.2.2-1
- Updated to version 2019.2.2.
- Updated plugins.

* Tue Aug 27 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.2.1-1
- Updated to version 2019.2.1.
- Updated plugins.

* Sat Jun 01 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.1.3-1
- Updated to version 2019.1.3.
- Updated plugins.

* Sun May 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.1.2-2
- Resolved issue with plugins. Thanks to ForNeVeR.

* Sat May 11 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.1.2-1
- Updated to version 2019.1.2.
- Updated plugins.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.1.1-1
- Updated to version 2019.1.1.
- Updated plugins.

* Thu Feb 28 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.3.5-1
- Updated to version 2018.3.5.
- Updated plugins.

* Mon Feb 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.3.4-1
- Updated to version 2018.3.4.
- Updated plugins.

* Sun Jan 13 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.3.3-1
- Updated to version 2018.3.3.
- Updated plugins.

* Fri Dec 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.3.2-1
- Updated to version 2018.3.2.
- Updated plugins.

* Wed Dec 05 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.3.1-1
- Updated to version 2018.3.1.
- Updated plugins.

* Fri Nov 23 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.3-1
- Updated to version 2018.3.
- Updated plugins.

* Sat Nov 17 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.2.5-1
- Updated to version 2018.2.5.
- Updated plugins.

* Thu Oct 25 2018 Petr Hracek <phracek@redhat.com> - 2018.2.4-2
- Build for Fedora 29 and rawhide

* Mon Sep 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.2.4-1
- Updated to version 2018.2.4.

* Sat Sep 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.2.3-1
- Updated to version 2018.2.3.

* Thu Aug 23 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2018.2.2-1
- Updated to version 2018.2.2.

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
