%define name unix2dos 
%define version 2.2
%define release %mkrel 5

Summary:	Unix2dos - UNIX to DOS text file format converter
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	distributable
Group:		Text tools 
Source0:	http://ftp.topnz.ac.nz/FTP/Linux/%{name}-2.2.src.tar.bz2
Patch0:		%{name}-mkstemp.patch
Patch1:		%{name}-%{version}-segfault.patch
Patch2:		%{name}-%{version}-manpage.patch
URL:		http://www.mandriva.com

%description
A utility that converts plain text files in UNIX format to DOS format.

%prep

%setup -q -c
%patch -p1 -b .sec
%patch1 -p1 -b .segf
%patch2 -p1 -b .man
perl -pi -e "s,^#endif.*,#endif,g;s,^#else.*,#else,g" *.[ch]

%build
gcc %{optflags} -o %{name} unix2dos.c

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m755 %{name} %{buildroot}%{_bindir}
install -m644 %{name}.1 %{buildroot}%{_mandir}/man1

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/*/*

