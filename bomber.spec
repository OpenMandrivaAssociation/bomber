%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Arcade bombing game
Name:		bomber
Epoch:		1
Version:	23.08.5
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		https://www.kde.org/applications/games/bomber/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)

%description
Bomber is a single player arcade game.

The player is invading various cities in a plane that is decreasing in height.
The goal of the game is to destroy all the buildings and advance to the next
level. Each level gets a bit harder by increasing the speed of the plane and
the height of the buildings.

%files -f %{name}.lang
%{_bindir}/bomber
%{_datadir}/applications/org.kde.bomber.desktop
%{_datadir}/bomber
%{_datadir}/config.kcfg/bomber.kcfg
%{_datadir}/icons/hicolor/*/apps/bomber.*
%{_datadir}/metainfo/org.kde.bomber.appdata.xml

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
