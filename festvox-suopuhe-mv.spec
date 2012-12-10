
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 20041119-4mdv2011.0
+ Revision: 618276
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 20041119-3mdv2010.0
+ Revision: 428717
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 20041119-2mdv2009.0
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Anssi Hannula <anssi@mandriva.org> 20041119-2mdv2008.0
+ Revision: 77424
- rebuild


* Sun Aug 06 2006 Anssi Hannula <anssi@mandriva.org> 20041119-1mdv2007.0
- initial Mandriva release

