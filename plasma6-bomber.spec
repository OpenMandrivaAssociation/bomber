#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Arcade bombing game
Name:		plasma6-bomber
Version:	24.05.2
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/bomber/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/bomber/-/archive/%{gitbranch}/bomber-%{gitbranchd}.tar.bz2#/bomber-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/bomber-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	pkgconfig(phonon4qt6)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6Quick)

%description
Bomber is a single player arcade game.

The player is invading various cities in a plane that is decreasing in height.
The goal of the game is to destroy all the buildings and advance to the next
level. Each level gets a bit harder by increasing the speed of the plane and
the height of the buildings.

%files -f bomber.lang
%{_bindir}/bomber
%{_datadir}/applications/org.kde.bomber.desktop
%{_datadir}/bomber
%{_datadir}/config.kcfg/bomber.kcfg
%{_datadir}/icons/hicolor/*/apps/bomber.*
%{_datadir}/metainfo/org.kde.bomber.appdata.xml

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n bomber-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang bomber --with-html
