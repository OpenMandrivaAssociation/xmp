Name:		xmp
Version:	4.0.7
Release:	2
Summary:	A multi-format module player
Group:		Sound
License:	GPLV2+
URL:		http://xmp.sourceforge.net/
Source0:	http://downloads.sourceforge.net/xmp/xmp-%{version}.tar.gz
# use pulseaudio output by default
Patch0:		xmp-4.0.6-pulse.patch
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libxmp)
BuildRequires:	pkgconfig(libpulse)

%description
This is the Extended Module Player, a portable module player that plays
over 90 mainstream and obscure module formats, including Protracker MOD,
Fasttracker II XM, Scream Tracker 3 S3M and Impulse Tracker IT files.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--enable-pulseaudio
%make

%install
%makeinstall_std

%files
%doc Changelog CREDITS README
%dir %{_sysconfdir}/xmp/
%config(noreplace) %{_sysconfdir}/xmp/*.conf
%{_bindir}/xmp
%{_mandir}/man1/xmp.1*

