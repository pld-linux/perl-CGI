#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
Summary:	CGI Perl module - simple CGI interface class
Summary(pl.UTF-8):	Moduł Perla CGI - prosta klasa interfejsu do CGI
Name:		perl-CGI
Version:	3.58
Release:	1
Epoch:		1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/MARKSTOS/%{pdir}.pm-%{version}.tar.gz
# Source0-md5:	2c06cdb9a794edb106c0b4267d30bbe5
URL:		http://search.cpan.org/dist/CGI.pm/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.3-0.20030610.20.2
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	perl-Encode
BuildRequires:	perl-FCGI >= 0.67
BuildRequires:	perl-Test-Simple >= 0.98
BuildRequires:	perl(File::Spec) >= 0.82
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(FCGI)

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
%setup -q -n %{pdir}.pm-%{version}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README *.html
%{perl_vendorlib}/CGI.pm
%{perl_vendorlib}/CGI/*.pm
%{_mandir}/man3/CGI*.3pm*

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.cgi
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.gif
%{_examplesdir}/%{name}-%{version}/*.html
%{_examplesdir}/%{name}-%{version}/*.xbm
%{_examplesdir}/%{name}-%{version}/WORLD_WRITABLE
