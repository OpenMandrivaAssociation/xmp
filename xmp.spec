Summary:	A multi-format module player
Name:	xmp
Version:	4.2.0
Release:	2
License:	GPLv2+
Group:	Sound
Url:	https://xmp.sourceforge.net/
Source0:	https://downloads.sourceforge.net/xmp/%{name}-%{version}.tar.gz
Patch0:	xmp-4.2.0-use-fixed-array-for-sound-drivers.patch
Patch1:	xmp-4.2.0-drop-unused-linked-list-code.patch
Patch2:	xmp-4.2.0-constify-struct-player_mode.patch
Patch3:	xmp-4.2.0-use-specific-driver-function-for-description.patch
Patch4:	xmp-4.2.0-update-COPYING-file.patch
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libxmp) >= 4.4.0
BuildRequires:	pkgconfig(libpulse-simple)
BuildRequires:	pkgconfig(sndio)

%description
This is the Extended Module Player, a portable module player that plays
over 90 mainstream and obscure module formats, including Protracker MOD,
Fasttracker II XM, Scream Tracker 3 S3M and Impulse Tracker IT files.

%files
%doc Changelog CREDITS README
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%configure --enable-pulseaudio --disable-oss
%make_build


%install
%make_install

