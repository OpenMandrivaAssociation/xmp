%define name xmp
%define version 2.2.0
%define prerel rc1
%define release %mkrel 0.%prerel.1

Summary: A multi-format module player
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://helllabs.org/xmp/testing/%{name}-%{version}-%{prerel}.tar.gz
Patch0: %{name}-%{version}-destdir.patch
URL: http://xmp.sourceforge.net/
License: GPL
Group: Sound
BuildRequires: libalsa-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
The Extended Module Player is a modplayer for Unix-like systems that plays
over 70 mainstream and obscure module formats from Amiga, Atari, Acorn,
Apple IIgs  and PC, including Protracker (MOD), Scream Tracker 3 (S3M),
Fast Tracker II (XM) and Impulse Tracker (IT) files.

%prep
rm -rf %{buildroot}

%setup -q -n %{name}-%{version}-%{prerel}
%patch0 -p0 -b .destdir

%build
%configure2_5x
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %buildroot%{_mandir}/man1/xxmp.1*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README docs/README* docs/COPYING docs/CREDITS docs/ChangeLog
%config(noreplace) %_sysconfdir/*
%{_bindir}/xmp
%{_mandir}/man1/xmp.1*
