#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	Digest
Summary:	IO::Digest - calculate digests while reading or writing
Summary(pl):	IO::Digest - wyliczanie sum kontrolnych podczas odczytu lub zapisu
Name:		perl-IO-Digest
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0448841e0559c2c19c7e8001ef087e26
Patch0:		%{name}-noninteractive.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-PerlIO-via-dynamic
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IO::Digest Perl module allows you to calculate digests while
reading or writing file handles. This avoids the case you need to
reread the same content to compute the digests after written a file.

%description -l pl
Modu³ Perla IO::Digest umo¿liwia wyliczanie sum kontrolnych podczas
odczytu z lub zapisu do pliku. Pozwala to unikn±æ ponownego odczytu
tej samej zawarto¶ci przy obliczaniu sum kontrolnych po zapisie do
pliku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/IO/Digest.pm
%{_mandir}/man3/*
