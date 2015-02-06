%define oname Starfighter

Summary:	Project: Starfighter
Name:		starfighter
Version:	1.2
Release:	3
License:	GPLv2+
Group:		Games/Arcade
Url:		http://www.parallelrealities.co.uk/starfighter.php
Source0:	%{name}-%{version}.tar.gz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		starfighter-1.2-sfmt.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)

%description
Project: Starfighter is a is a Space/Arcade game which uses SDL libraries.

The story:
After decades of war one company, who had gained powerful supplying both
sides with weaponary, steps forwards and crushes both warring factions in
one swift movement. Using far superior weaponary and AI craft, the company
was completely unstoppable and now no one can stand in their way. Thousands
began to perish under the iron fist of the company. The people cried out
for a saviour, for someone to light this dark hour... and someone did.

Features:
- 26 missions over 4 star systems
- Primary and Secondary Weapons (including a laser cannon and a charge weapon)
- A weapon powerup system
- Wingmates
- Missions with Primary and Secondary Objectives
- A Variety of Missions (Protect, Destroy, etc)
- 13 different music tracks
- Boss battles

%files
%doc docs/*
%{_gamesdatadir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesbindir}/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

find . -perm 0600 | xargs chmod 0644
chmod 0644 docs/*

%build
%setup_compile_flags
%define Werror_cflags %nil
%make DATADIR="%{_gamesdatadir}/%{name}/" OPTFLAGS="%{optflags} -O3"

%install
%makeinstall_std DATADIR="%{_gamesdatadir}/%{name}/" BINDIR="%{_gamesbindir}/"

install -d %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=%{summary}
Comment=Space/Arcade game
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png


