Summary:	UNIX to DOS text file format converter
Name:		unix2dos
Version:	2.2
Release:	12
License:	distributable
Group:		Text tools 
Source0:	http://ftp.topnz.ac.nz/FTP/Linux/%{name}-2.2.src.tar.bz2
Patch0:		%{name}-mkstemp.patch
Patch1:		%{name}-%{version}-segfault.patch
Patch2:		%{name}-%{version}-manpage.patch
URL:		https://www.mandriva.com

%description
A utility that converts plain text files in UNIX format to DOS format.

%prep

%setup -q -c
%patch0 -p1 -b .sec
%patch1 -p1 -b .segf
%patch2 -p1 -b .man
perl -pi -e "s,^#endif.*,#endif,g;s,^#else.*,#else,g" *.[ch]

%build
gcc %{optflags} -o %{name} unix2dos.c

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m755 %{name} %{buildroot}%{_bindir}
install -m644 %{name}.1 %{buildroot}%{_mandir}/man1

%clean

%files
%defattr(-,root,root,0755)
%doc COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/*/*



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-10mdv2011.0
+ Revision: 615360
- the mass rebuild of 2010.1 packages

* Sat Dec 05 2009 Jérôme Brenier <incubusss@mandriva.org> 2.2-9mdv2010.1
+ Revision: 473903
- number the first patch macro

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.2-7mdv2009.0
+ Revision: 255167
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.2-5mdv2008.1
+ Revision: 128767
- kill re-definition of %%buildroot on Pixel's request
- fix URL


* Thu Jun 02 2005 Sebastien Savarin <plouf@mandriva.org> 2.2-5mdk
- Rebuild for new gcc

* Fri Apr 02 2004 Daouda LO <daouda@mandrakesoft.com> 2.2-4mdk
- rebuild

* Mon Jan 27 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.2-3mdk
- build release
- added P1 & P2 from RH
- added a "fake" URL to make mr. lint shut up
- fix license
- misc spec file fixes

* Wed Sep 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.2-2mdk
- rebuild

* Wed Jan 31 2001 Daouda Lo <daouda@mandrakesoft.com> 2.2-1mdk
- first mdk package

* Fri Nov 17 2000 Tim Powers <timp@redhat.com>
- patched to use mkstemp, not much had to be done.

* Thu Nov 16 2000 Tim Powers <timp@redhat.com>
- minor spec file cleanups
- built for 7.1
- use predefined RPM macros whenever possible
- use RPM_OPT_FLAGS when building

* Wed Jul 07 1999 Peter Soos <sp@osb.hu> 
- Added Hungarian "Summary:" and "%%description" 
- Corrected the file and directory attributes to rebuild the package 
  under RedHat Linux 6.0

* Thu Jul 09 1998 Arkadiusz Mikkkkkkiewicz <misiek@misiek.eu.org> 
- Recompiled under RedHat Linux 5.1 
- Small changes in %%build and %%files 
- Added "Vendor:" 
- Added Polish "Summary:" and "%%description"

* Thu Jun 18 1998 Peter Soos <sp@osb.hu> 
- Corrected the spec file for rpm 2.5

* Fri Dec 05 1997 Peter Soos <sp@osb.hu> 
- Recompiled under RedHat Linux 5.0

