%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Arcade bombing game
Name:		bomber
Epoch:		1
Version:	15.08.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/bomber/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	libkdegames4-devel
BuildRequires:	cmake(ECM)

%description
Bomber is a single player arcade game.

The player is invading various cities in a plane that is decreasing in height.
The goal of the game is to destroy all the buildings and advance to the next
level. Each level gets a bit harder by increasing the speed of the plane and
the height of the buildings.

%files
%{_bindir}/bomber
%{_datadir}/applications/org.kde.bomber.desktop
%{_datadir}/bomber
%{_datadir}/config.kcfg/bomber.kcfg
%{_datadir}/icons/hicolor/*/apps/bomber.*
%{_datadir}/appdata/bomber.appdata.xml
%{_datadir}/kxmlgui5/bomber
%doc %{_docdir}/HTML/en/bomber

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
