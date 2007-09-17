%define name xmp
%define version 2.2.1
%define release %mkrel 1

Summary: A multi-format module player
Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.gz
URL: http://xmp.sourceforge.net/
License: GPL
Group: Sound
BuildRequires: libalsa-devel, audacious-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
The Extended Module Player is a modplayer for Unix-like systems that plays
over 70 mainstream and obscure module formats from Amiga, Atari, Acorn,
Apple IIgs  and PC, including Protracker (MOD), Scream Tracker 3 (S3M),
Fast Tracker II (XM) and Impulse Tracker (IT) files.

%package audacious
Summary: xmp plugin for Audacious
Group: Sound
Requires: audacious

%description audacious
The Extended Module Player is a modplayer for Unix-like systems that plays
over 70 mainstream and obscure module formats from Amiga, Atari, Acorn,
Apple IIgs  and PC, including Protracker (MOD), Scream Tracker 3 (S3M),
Fast Tracker II (XM) and Impulse Tracker (IT) files.

This package contains the xmp plugin for the Audacious media player.

%prep
rm -rf %{buildroot}

%setup -q -n %{name}-%{version}

%build
%configure2_5x --enable-audacious-plugin
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README docs/README* docs/COPYING docs/CREDITS docs/ChangeLog
%config(noreplace) %_sysconfdir/*
%{_bindir}/xmp
%{_mandir}/man1/xmp.1*

%files audacious
%defattr(-,root,root)
%doc README docs/COPYING docs/ChangeLog docs/CREDITS
%{_libdir}/audacious/Input/*
