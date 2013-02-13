Name:		bomber
Version:	4.10.0
Release:	1
Epoch:		1
Summary:	Arcade bombing game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/bomber/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
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

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

