#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
Summary:	CGI Perl module - simple CGI interface class
Summary(pl):	Modu� Perla CGI - prosta klasa interfejsu do CGI
Name:		perl-CGI
Version:	3.25
Release:	1
Epoch:		1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}.pm-%{version}.tar.gz
# Source0-md5:	9aad2b7d0398bbd037b2f73e534378a1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.3-0.20030610.20.2
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	perl-FCGI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(FCGI)

%description
CGI is an easy-to-use Perl5 library for writing World Wide Web CGI
scripts. This is replacement for usually outdated CGI module from perl
distribution.

%description -l pl
CGI jest modu�em do prostego i szybkiego pisania aplikacji dla WWW -
skrypt�w CGI. Pakiet ten zawiera zamiennik dla zazwyczaj starej wersji
modu�u CGI kt�ra jest dostarczana razem z perlem.

%package examples
Summary:	Examples for the CGI module
Summary(pl):	Przyk�ady u�ycia modu�u CGI
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}

%description examples
Examples for the CGI module.

%description examples -l pl
Przyk�ady u�ycia modu�u CGI.

%prep
%setup -q -n %{pdir}.pm-%{version}

%{__sed} -i -e 's|/usr/local/bin/perl|/usr/bin/perl|g' examples/*.cgi

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
