Summary:	A multi-format module player
Name:	xmp
Version:	4.3.1
Release:	1
License:	GPLv2+
Group:	Sound
Url:	https://xmp.sourceforge.net/
Source0:	https://downloads.sourceforge.net/xmp/%{name}-%{version}.tar.gz
# dropped (no longer applies): Patch0:	xmp-4.3.1-use-fixed-array-for-sound-drivers.patch
# dropped (no longer applies): Patch1:	xmp-4.3.1-drop-unused-linked-list-code.patch
# dropped (no longer applies): Patch2:	xmp-4.3.1-constify-struct-player_mode.patch
# dropped (no longer applies): Patch3:	xmp-4.3.1-use-specific-driver-function-for-description.patch
# dropped (no longer applies): Patch4:	xmp-4.3.1-update-COPYING-file.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
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

