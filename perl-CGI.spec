#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	CGI
Summary:	CGI Perl module
Summary(cs):	Modul CGI pro Perl
Summary(da):	Perlmodul CGI
Summary(de):	CGI Perl Modul
Summary(es):	Módulo de Perl CGI
Summary(fr):	Module Perl CGI
Summary(it):	Modulo di Perl CGI
Summary(ja):	CGI Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	CGI ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul CGI
Summary(pl):	Modu³ Perla CGI
Summary(pt):	Módulo de Perl CGI
Summary(pt_BR):	Módulo Perl CGI
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl CGI
Summary(sv):	CGI Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl CGI
Summary(zh_CN):	CGI Perl Ä£¿é
Name:		perl-CGI
Version:	2.99
Release:	1
Epoch:		1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}.pm-%{version}.tar.gz
# Source0-md5:	8f12c0d0462409ab33447a44dbaefe2b
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(FCGI)' 'perl(Apache) 'perl(Apache::compat)' 'perl(mod_perl)'

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

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
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
