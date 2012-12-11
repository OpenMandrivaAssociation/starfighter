%define	oname	Starfighter

Name:		starfighter
Version:	1.2
Release:	%mkrel 1
Summary:	Project: Starfighter
Group:		Games/Arcade
License:	GPL
URL:		http://www.parallelrealities.co.uk/starfighter.php
Source0:	%{name}-%{version}.tar.gz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		starfighter-1.2-sfmt.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel

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

%prep
%setup -q
%patch0 -p1

%build
%setup_compile_flags
%define Werror_cflags %nil
%make DATADIR="%{_gamesdatadir}/%{name}/" OPTFLAGS="%{optflags} -O3"

%install
%__rm -rf %{buildroot}
%makeinstall_std DATADIR="%{_gamesdatadir}/%{name}/" BINDIR="%{_gamesbindir}/"

%__install -d %{buildroot}%{_datadir}/applications
%__cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
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

%__install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
%__install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
%__install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%clean
%__rm -rf %{buildroot}

%files
%doc docs/*
%{_gamesdatadir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesbindir}/*


%changelog
* Sun Apr 08 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2-1
+ Revision: 789853
- New version 1.2, spec cleanup

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-8mdv2011.0
+ Revision: 614976
- the mass rebuild of 2010.1 packages

* Sat May 01 2010 Funda Wang <fwang@mandriva.org> 1.1-7mdv2010.1
+ Revision: 541405
- fix build with format check

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.1-6mdv2009.0
+ Revision: 218426
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Jul 09 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1-6mdv2008.0
+ Revision: 50360
- drop debian menu
  rebuild
- Import starfighter



* Thu Aug 17 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.1-5mdv2007.0
- xdg menu
- fix group

* Fri Dec 23 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.1-4mdk
- rebuild
- %%mkrel

* Fri Aug 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1-3mdk
- rebuild for new menu
- don't bzip2 icons in src.rpm
- fix buildrequires (lib64..)

* Tue Jun  8 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1-2mdk
- rebuild for new g++

* Mon Sep 01 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1-1mdk
- 1.1
- license is now GPL
- regenerated P0

* Sun Aug 03 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.00-5mdk
- changed description (thx, Adam Williamson & Charles A. Edwards)

* Sat Aug 02 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.00-4mdk
- corrected url

* Mon Jun 02 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.00-3mdk
- change summary to macro to avoid the use of the -debug package's summary
  in menu item

* Wed May 28 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.00-2mdk
- fix summary and name, it's Project: Starfighter not only Starfighter

* Wed May 21 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.00-1mdk
- initial mdk release
