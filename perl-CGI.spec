#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	CGI
Summary:	CGI Perl module - simple CGI interface class
Summary(pl):	Modu³ Perla CGI - prosta klasa interfejsu do CGI
Name:		perl-CGI
Version:	3.04
Release:	2
Epoch:		1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}.pm-%{version}.tar.gz
# Source0-md5:	abeca476bd3c2119e489c1a4fe6c3ed2
BuildRequires:	rpm-perlprov >= 4.3-0.20030610.20.2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(FCGI)

%description
CGI is an easy-to-use Perl5 library for writing World Wide Web CGI
scripts. This is replacement for usually outdated CGI module from perl
distribution.

%description -l pl
CGI jest modu³em to prostego i szybkiego pisania aplikacji dla WWW -
skryptów CGI. Pakiet ten zawiera zamiennik dla zazwyczaj starej wersji
modu³u CGI która jest dostarczana razem z perlem.

%package examples
Summary:	Examples for the CGI module
Summary(pl):	Przyk³ady u¿ycia modu³u CGI
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}

%description examples
Examples for the CGI module.

%description examples -l pl
Przyk³ady u¿ycia modu³u CGI.

%prep
%setup -q -n %{pnam}.pm-%{version}

%{__perl} -pi -e 's|/usr/local/bin/perl|/usr/bin/perl|g' examples/*.cgi

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README *.html
%{perl_vendorlib}/CGI.pm
%{perl_vendorlib}/CGI/*
%{_mandir}/man3/*

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.cgi
%{_examplesdir}/%{name}-%{version}/*.[!c]*
%{_examplesdir}/%{name}-%{version}/WORLD*
