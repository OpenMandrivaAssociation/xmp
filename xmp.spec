%define name xmp
%define version 3.2.0
%define release %mkrel 1
%define build_audacious 0

Summary: A multi-format module player
Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.gz
URL: http://xmp.sourceforge.net/
License: GPLv2+
Group: Sound
BuildRequires: libalsa-devel
BuildRequires: pulseaudio-devel
BuildRequires: xmms-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
The Extended Module Player is a modplayer for Unix-like systems that plays
over 70 mainstream and obscure module formats from Amiga, Atari, Acorn,
Apple IIgs  and PC, including Protracker (MOD), Scream Tracker 3 (S3M),
Fast Tracker II (XM) and Impulse Tracker (IT) files.

%if %build_audacious
%package audacious
Summary: Xmp plugin for Audacious
Group: Sound
Requires: audacious
BuildRequires: audacious-devel

%description audacious
The Extended Module Player is a modplayer for Unix-like systems that plays
over 70 mainstream and obscure module formats from Amiga, Atari, Acorn,
Apple IIgs  and PC, including Protracker (MOD), Scream Tracker 3 (S3M),
Fast Tracker II (XM) and Impulse Tracker (IT) files.

This package contains the xmp plugin for the Audacious media player.
%endif

%package xmms
Summary: Xmp plugin for XMMS
Group: Sound
Requires: xmms

%description xmms
The Extended Module Player is a modplayer for Unix-like systems that plays
over 70 mainstream and obscure module formats from Amiga, Atari, Acorn,
Apple IIgs  and PC, including Protracker (MOD), Scream Tracker 3 (S3M),
Fast Tracker II (XM) and Impulse Tracker (IT) files.

This package contains the xmp plugin for the XMMS media player.

%prep
%setup -q -n %name-%version

%build
%configure2_5x --enable-pulseaudio  --enable-xmms-plugin \
%if %build_audacious
--enable-audacious-plugin
%endif

%make

%install
rm -rf %{buildroot}
mkdir -p %buildroot%_libdir/{audacious,xmms}/Input
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README docs/README* docs/COPYING docs/CREDITS docs/ChangeLog
%config(noreplace) %_sysconfdir/*
%{_bindir}/xmp
%{_mandir}/man1/xmp.1*

%if %build_audacious
%files audacious
%defattr(-,root,root)
%doc README docs/COPYING docs/ChangeLog docs/CREDITS
%{_libdir}/audacious/Input/*
%endif

%files xmms
%defattr(-,root,root)
%doc README docs/COPYING docs/ChangeLog docs/CREDITS
%{_libdir}/xmms/Input/*
