#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	CGI
%include	/usr/lib/rpm/macros.perl
Summary:	CGI Perl module - simple CGI interface class
Summary(pl.UTF-8):	Moduł Perla CGI - prosta klasa interfejsu do CGI
Name:		perl-CGI
Version:	4.42
Release:	1
Epoch:		1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEEJO/CGI-%{version}.tar.gz
# Source0-md5:	4f71703059f9a941cf7e8f547f950795
URL:		http://search.cpan.org/dist/CGI/
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.3-0.20030610.20.2
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl-Encode
BuildRequires:	perl-FCGI >= 0.67
BuildRequires:	perl-HTML-Parser >= 3.69
BuildRequires:	perl-Test-Deep >= 0.11
BuildRequires:	perl-Test-NoWarnings >= 1.04
BuildRequires:	perl-Test-Simple >= 0.98
BuildRequires:	perl-Test-Warn >= 0.30
%endif
Requires:	perl(File::Spec) >= 0.82
Requires:	perl-HTML-Parser >= 3.69
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl	FCGI

%description
CGI is an easy-to-use Perl5 library for writing World Wide Web CGI
scripts. This is replacement for usually outdated CGI module from perl
distribution.

%description -l pl.UTF-8
CGI jest modułem do prostego i szybkiego pisania aplikacji dla WWW -
skryptów CGI. Pakiet ten zawiera zamiennik dla zazwyczaj starej wersji
modułu CGI która jest dostarczana razem z perlem.

%package examples
Summary:	Examples for the CGI module
Summary(pl.UTF-8):	Przykłady użycia modułu CGI
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description examples
Examples for the CGI module.

%description examples -l pl.UTF-8
Przykłady użycia modułu CGI.

%prep
%setup -q -n %{pdir}-%{version}

%{__sed} -i -e 's|/usr/local/bin/perl|/usr/bin/perl|g' examples/*.{cgi,pl}

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/CGI.pod \
	$RPM_BUILD_ROOT%{perl_vendorlib}/CGI/HTML/Functions.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/CGI.pm
%{perl_vendorlib}/Fh.pm
%{perl_vendorlib}/CGI/*.pm
%{perl_vendorlib}/CGI/File
%{perl_vendorlib}/CGI/HTML
%{_mandir}/man3/CGI*.3pm*

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.cgi
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.gif
