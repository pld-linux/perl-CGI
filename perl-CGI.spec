%include	/usr/lib/rpm/macros.perl
Summary:	CGI perl module
Summary(pl):	Modu³ perla CGI
Name:		perl-CGI
Version:	2.78
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	 ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI.pm-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(FCGI)" "perl(Apache)"

%description
CGI is an easy-to-use Perl5 library for writing World Wide Web CGI scripts.
This is replacement for usually outdated CGI module from perl distribution.

%description -l pl
CGI jest modu³em to prostego i szybkiego pisania aplikacji dla WWW - skryptów
CGI. Pakiet ten zawiera zamiennik dla zazwyczaj starej wersji modu³u CGI która
jest dostarczana razem z perlem.

%prep
%setup -q -n CGI.pm-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc *.gz
%doc %{_mandir}/man3/*
%{perl_privlib}/CGI.pm
%{perl_privlib}/CGI
