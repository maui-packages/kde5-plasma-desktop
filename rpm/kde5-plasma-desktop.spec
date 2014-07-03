# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kde5-plasma-desktop

# >> macros
# << macros

Summary:    Plasma 5 desktop
Version:    4.98.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kde5-plasma-desktop.yaml
Source101:  kde5-plasma-desktop-rpmlintrc
Requires:   kde5-filesystem
Requires:   kde5-plasma-workspace
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Declarative)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-dpms)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-screensaver)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xevie)
BuildRequires:  pkgconfig(xcb-xf86dri)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xprint)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcb-xv)
BuildRequires:  pkgconfig(xcb-xvmc)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-property)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-reply)
BuildRequires:  kde5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  phonon-qt5-devel
BuildRequires:  kf5-umbrella
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-kdesu-devel
BuildRequires:  kf5-attica-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-krunner-devel
BuildRequires:  kde5-libksysguard-devel
BuildRequires:  kde5-plasma-workspace-devel
BuildRequires:  kde5-kwin-devel
BuildRequires:  kf5-kactivities-libs-devel
BuildRequires:  desktop-file-utils

%description
Plasma 5 desktop


%package shell
Summary:    Plasma desktop shell
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description shell
Plasma desktop shell.


%package doc
Summary:    Documentation and user manuals for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation and user manuals for %{name}


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kde5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kde5_make_install
# << install pre

# >> install post
rm -vf %{buildroot}/%{_kde5_libdir}/libkfontinst{,ui}.so || true
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%dir %{_kde5_datadir}/plasma/shells
%{_kde5_bindir}/kapplymousetheme
%{_kde5_bindir}/kaccess
%{_kde5_bindir}/krdb
%{_kde5_libexecdir}/kcmdatetimehelper
%{_kde5_libexecdir}/knetattach
%{_kde5_libdir}/qml/org/kde/plasma/private
%{_kde5_libdir}/libkdeinit5_kaccess.so
%{_kde5_libdir}/kconf_update_bin/*
%{_kde5_plugindir}/*.so
%{_kde5_datadir}/plasma/*
%exclude %{_kde5_datadir}/plasma/shells/*
%{_kde5_datadir}/kcminput
%{_kde5_datadir}/color-schemes
%{_kde5_datadir}/kconf_update/*
%{_kde5_datadir}/kthememanager
%{_kde5_datadir}/kdisplay
%{_kde5_datadir}/kcontrol
%{_kde5_datadir}/kcmkeys
%{_kde5_datadir}/kcm_componentchooser
%{_kde5_datadir}/kcm_phonon
%{_kde5_datadir}/kcmkeyboard
%{_kde5_datadir}/ksmserver
%{_kde5_sysconfdir}/dbus-1/system.d/*.conf
%{_kde5_sysconfdir}/xdg/*.knsrc
%{_datadir}/kservices5/*
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/*
%{_datadir}/polkit-1/actions/*.policy
# >> files
# << files

%files shell
%defattr(-,root,root,-)
%{_kde5_datadir}/plasma/shells/org.kde.plasma.desktop/*
# >> files shell
# << files shell

%files doc
%defattr(-,root,root,-)
%{_datadir}/doc/HTML/en/*
# >> files doc
# << files doc
