%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	CGI
Summary:	CGI Perl module
Summary(cs):	Modul CGI pro Perl
Summary(da):	Perlmodul CGI
Summary(de):	CGI Perl Modul
Summary(es):	M�dulo de Perl CGI
Summary(fr):	Module Perl CGI
Summary(it):	Modulo di Perl CGI
Summary(ja):	CGI Perl �⥸�塼��
Summary(ko):	CGI �� ����
Summary(no):	Perlmodul CGI
Summary(pl):	Modu� Perla CGI
Summary(pt):	M�dulo de Perl CGI
Summary(pt_BR):	M�dulo Perl CGI
Summary(ru):	������ ��� Perl CGI
Summary(sv):	CGI Perlmodul
Summary(uk):	������ ��� Perl CGI
Summary(zh_CN):	CGI Perl ģ��
Name:		perl-CGI
Version:	2.80
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}.pm-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(FCGI)" "perl(Apache)"

%description
CGI is an easy-to-use Perl5 library for writing World Wide Web CGI
scripts. This is replacement for usually outdated CGI module from perl
distribution.

%description -l pl
CGI jest modu�em to prostego i szybkiego pisania aplikacji dla WWW -
skrypt�w CGI. Pakiet ten zawiera zamiennik dla zazwyczaj starej wersji
modu�u CGI kt�ra jest dostarczana razem z perlem.

%prep
%setup -q -n %{pnam}.pm-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc %{_mandir}/man3/*
%{perl_privlib}/CGI.pm
%{perl_privlib}/CGI
