#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
#

Name:       harbour-file-browser-beta

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    File Browser for Sailfish OS
Version:    2.0.0
Release:    0
Group:      Qt/Qt
License:    GPLv3+
URL:        https://github.com/karip/harbour-file-browser
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-file-browser.yaml
AutoReqProv:    0
Requires:   libsailfishapp
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(sailfishapp)
BuildRequires:  qt5-qttools-linguist
BuildRequires:  desktop-file-utils

%description
File Browser for Sailfish OS. Browse files on the phone.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
export FILEBROWSER_VERSION=%{version}
export FILEBROWSER_HARBOUR_COMPLIANCE=off
# << build pre

%qtc_qmake5

%qtc_make %{?_smp_mflags}

# >> build post
unset FILEBROWSER_VERSION
unset FILEBROWSER_HARBOUR_COMPLIANCE
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%defattr(644,root,root,755)
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/qml
%{_datadir}/%{name}/i18n
%attr(755,root,root) %{_bindir}/%{name}
# >> files
# << files
