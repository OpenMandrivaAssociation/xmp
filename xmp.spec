%define name xmp
%define version 2.2.0
%define prerel pre6
%define release %mkrel 0.%prerel.1

Summary: Extended Module Player
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://helllabs.org/xmp/testing/%{name}-%{version}-%{prerel}.tar.gz
URL: http://xmp.sourceforge.net/
License: GPL
Group: Sound
BuildRequires: libalsa-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
xmp is a tracked music player that recognizes XM, MOD, NST, WOW, S3M, STM, 669,
PTM, OKT, MTM, FAR, ALM, RAD, AMD and ALM modules. xmp can play modules using
the OSS sequencer (for Gravis Ultrasound and AWE32) and software mixing (for
/dev/dsp and file output).

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}-%{version}-%{prerel}

%build
%configure2_5x --disable-xmms
make

%install
rm -rf $RPM_BUILD_ROOT
make install DEST_DIR=$RPM_BUILD_ROOT BIN_DIR=$RPM_BUILD_ROOT%{_bindir} MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README docs/README* docs/COPYING docs/CREDITS docs/ChangeLog
%config(noreplace) %_sysconfdir/*
%{_bindir}/*
%{_mandir}/*/*
