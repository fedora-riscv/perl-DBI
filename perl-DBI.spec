Name:           perl-DBI
Version:        1.51
Release: 	1%{?dist}
Summary:        A database access API for perl

Group:          Development/Libraries
License:        GPL or Artistic
URL:            http://dbi.perl.org/
Source0:        http://www.cpan.org/authors/id/T/TI/TIMB/DBI-%{version}.tar.gz
Source1:        filter-requires-dbi.sh
Patch0:         perl-DBI-1.37-prever.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%define __perl_requires %{SOURCE1}

%description 
DBI is a database access Application Programming Interface (API) for
the Perl Language. The DBI API Specification defines a set of
functions, variables and conventions that provide a consistent
database interface independent of the actual database being used.


%prep
%setup -q -n DBI-%{version} 
%patch0 -p1
chmod 644 ex/*

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

# Remove Win32 specific files and man pages to avoid unwanted dependencies
rm -rf $RPM_BUILD_ROOT%{perl_vendorarch}/{Win32,DBI/W32ODBC.pm}
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/{DBI::W32ODBC.3pm,Win32::DBIODBC.3pm}

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README ex/
%{_bindir}/dbipro*
%{perl_vendorarch}/*.p*
%{perl_vendorarch}/Bundle/
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBI/
%{perl_vendorarch}/auto/DBI/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*


%changelog
* Mon Jul 17 2006 Jason Vas Dias <jvdias@redhat.com> - 1.51-1
- Upgrade to 1.51

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.50-3
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.50-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.50-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 1.50-2
- rebuild for new perl-5.8.8 / gcc / glibc

* Mon Dec 19 2005 Jason Vas Dias<jvdias@redhat.com> - 1.50-1
- upgrade to 1.50

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Wed Apr 13 2005 Jose Pedro Oliveira <jpo@di.uminho.pt> - 1.48-4
- (#154762)
- License information: GPL or Artistic
- Removed the Time::HiRes building requirement (see Changes)
- Removed the empty .bs file
- Corrected file permissions

* Mon Apr 04 2005 Warren Togami <wtogami@redhat.com> 1.48-3
- filter perl(Apache) (#153673)

* Fri Apr 01 2005 Robert Scheck <redhat@linuxnetz.de> 1.48-2
- spec file cleanup (#153164)

* Thu Mar 31 2005 Warren Togami <wtogami@redhat.com> 1.48-1
- 1.48

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 1.40-1
- update to 1.40

* Fri Dec 19 2003 Chip Turner <cturner@redhat.com> 1.39-1
- update to 1.39

* Mon Jul  7 2003 Chip Turner <cturner@redhat.com> 1.37-1
- upgrade to 1.37

* Wed Apr  2 2003 Chip Turner <cturner@redhat.com> 1.32-6
- add buildrequires on perl-Time-HiRes

* Tue Feb 18 2003 Chip Turner <cturner@redhat.com>
- update dependency filter to remove dependency on perl(Apache) that
- crept in (#82927)

* Mon Jan 27 2003 Chip Turner <cturner@redhat.com>
- version bump and rebuild

* Sat Dec 14 2002 Chip Turner <cturner@redhat.com>
- don't use rpm internal dep generator

* Wed Nov 20 2002 Chip Turner <cturner@redhat.com>
- rebuild

* Wed Aug  7 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.30-1
- 1.30. 

* Tue Jun 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.28-1
- 1.28
- Building it also fixes #66304

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun  5 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.23-2
- Tweak dependency finder - filter out a dependency found within the 
  doc section of a module

* Tue Jun  4 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.23-1
- 1.23
- Some changes to integrate with new Perl
- Update URL

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May  7 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.21-2
- Rebuild

* Fri Feb 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.21-1
- 1.21

* Fri Feb  8 2002 Chip Turner <cturner@redhat.com>
- filter out "soft" dependencies: perl(RPC::PlClient) and perl(Win32::ODBC)

* Thu Feb  7 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.201-2
- Rebuild

* Tue Jan 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.201-1
- 1.201

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jan  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.20-1
- 1.20
- Proper URL

* Sat Jun 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 1.18

* Wed May 30 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 1.16
- change group to Applications/Databases from Applications/CPAN

* Tue May  1 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 1.15

* Tue Feb 27 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Cleanups

* Thu Nov 30 2000 Trond Eivind Glomsrød <teg@redhat.com>
- build for main distribution
- use %%{_tmppath}
- change name of specfile
- don't use a find script to generate file lists
- general cleanup
- add descriptive summary and description


* Mon Aug 14 2000 Tim Powers <timp@redhat.com>
- Spec file was autogenerated. 
