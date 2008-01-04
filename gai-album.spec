%define name gai-album
%define version 0.7
%define release %mkrel 6

Name: %name
Summary: Displays the front CD cover of the album played by XMMS
Version: %{version}
Release: %{release}
License: GPL
Url: http://gai.sf.net
Group: Sound
Source: http://prdownloads.sourceforge.net/gai/%{name}-%{version}.tar.bz2
Source10:   %{name}-16.png
Source11:   %{name}-32.png
Source12:   %{name}-48.png
Patch: gai-album-0.7-rox-install.patch
BuildRoot: %{_tmppath}/build-root-%{name}
BuildRequires: xmms-devel
BuildRequires: libgai-devel >= 0.5.3

%description
A GAI applet displaying the front CD cover of the album played by
XMMS. 

This applet can be used in the GNOME and ROX Panels and as a
WindowMaker dockapp. Other panels and Window Managers will be
supported soon.

%prep
%setup -q 
%patch -p1

%build
%configure2_5x
%make 

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib/* %buildroot%_libdir/
%endif
install -m644 %SOURCE10 -D %{buildroot}/%_miconsdir/%name.png
install -m644 %SOURCE11 -D %{buildroot}/%_iconsdir/%name.png
install -m644 %SOURCE12 -D %{buildroot}/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > %{buildroot}/%{_menudir}/%{name} 
?package(%name): command="%{_bindir}/%name" icon="%name.png" \
                needs="X11" section="Multimedia/Sound" \
 title="Gai-album" longtitle="Xmms cover viewer" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gai-Album
Comment=Xmms cover viewer
Exec=%{_bindir}/%{name}
Icon=%name
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;
StartupNotify=true
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root,0755)
%doc README README.gai
%{_bindir}/*
%{_libdir}/bonobo/servers/GNOME_%{name}Applet.server
%_libdir/apps/*
%_datadir/applications/mandriva*
%{_menudir}/%name
%{_datadir}/pixmaps/*
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png


