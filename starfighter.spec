%define	name	starfighter
%define	oname	Starfighter
%define	version	1.1
%define release	6
%define	Summary	Project: Starfighter

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
URL:		http://www.parallelrealities.co.uk/starfighter.php
Source0:	%{name}-%{version}-1.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		%{name}-1.1-mdkconf.patch.bz2
License:	GPL
Group:		Games/Arcade
Summary:	%{Summary}
BuildRequires:	SDL-devel SDL_mixer-devel SDL_image-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%{oname} is a is a Space/Arcade game which uses the SDL
libraries. 

The story:
After decades of war one company, who had gained powerful
supplying both sides with weaponary, steps forwards and
crushes both warring factions in one swift movement.
Using far superior weaponary and AI craft, the company
was completely unstoppable and now no one can stand in
their way. Thousands began to perish under the iron fist
of the company. The people cried out for a saviour, for
someone to light this dark hour... and someone did.

Features:

26 missions over 4 star systems
Primary and Secondary Weapons (including a laser cannon and a charge
weapon) 
A weapon powerup system
Wingmates
Missions with Primary and Secondary Objectives
A Variety of Missions (Protect, Destroy, etc)
13 different music tracks
Boss battles

%prep
%setup -q
%patch0 -p1 -b .orig

%build
%make DATADIR="%{_gamesdatadir}/%{name}/" OPTFLAGS="%{optflags} -O3"

%install
rm -rf %{buildroot}
%{makeinstall_std} DATADIR="%{buildroot}%{_gamesdatadir}/%{name}/" BINDIR="%{buildroot}%{_gamesbindir}/"

install -d %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=%{Summary}
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc docs/*
%{_gamesdatadir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/*
