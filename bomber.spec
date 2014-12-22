%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Arcade bombing game
Name:		bomber
Epoch:		1
Version:	14.12.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/bomber/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
Bomber is a single player arcade game.

The player is invading various cities in a plane that is decreasing in height.
The goal of the game is to destroy all the buildings and advance to the next
level. Each level gets a bit harder by increasing the speed of the plane and
the height of the buildings.

%files
%{_kde_bindir}/bomber
%{_kde_applicationsdir}/bomber.desktop
%{_kde_appsdir}/bomber
%{_kde_datadir}/config.kcfg/bomber.kcfg
%{_kde_docdir}/HTML/en/bomber
%{_kde_iconsdir}/hicolor/*/apps/bomber.*
%{_datadir}/apps/appdata/bomber.appdata.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
