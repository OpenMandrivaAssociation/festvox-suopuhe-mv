
%define name	festvox-suopuhe-mv
%define version	20041119
%define rel	4
%define release	%mkrel %rel

Summary:	Festival Voice - Finnish male speaker (hy_fi_mv)
Name:		%name
Version:	%version
Release:	%release
License:	LGPL
Group:		Sound
URL:		http://phon.joensuu.fi/suopuhe/
Source:		http://phon.joensuu.fi/suopuhe/tulosaineisto/hy_fi_mv_diphone-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Requires:	festvox-suopuhe-common
# other festvox packages seem to provide these:
Provides:	festival-voice
Provides:	festival-voice-finnish
Provides:	festival-voice-fi_FI
# per Mandriva locale-specific package policy:
Requires:	locales-fi

%description
This is a Finnish male speaker for the Festival speech synthesis
system. It was developed as part of the Suopuhe project at
the universities of Helsinki and Joensuu.

%prep
%setup -q -n festival

%install
rm -rf %{buildroot}

install -d -m755 %{buildroot}%{_datadir}/festival/voices/finnish/hy_fi_mv_diphone
cp -a lib/voices/finnish/hy_fi_mv_diphone/group \
	%{buildroot}%{_datadir}/festival/voices/finnish/hy_fi_mv_diphone

ln -s ../suopuhe.common %{buildroot}%{_datadir}/festival/voices/finnish/hy_fi_mv_diphone/festvox

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc lib/voices/finnish/hy_fi_mv_diphone/README.mv
%{_datadir}/festival/voices/finnish/hy_fi_mv_diphone

