#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs working, not busy /dev/audio!)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Video
%define	pnam	Capture-V4l
Summary:	Perl Video::Capture::V4l module
Summary(pl):	Modu³ Perla Video::Capture::V4l
Name:		perl-Video-Capture-V4l
Version:	0.222
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fc959604bbcdc90c715d0f91405b6025
Patch0:		%{name}-make.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to the Video4linux framegrabber interface.

%description -l pl
Perlowy interfejs do urz±dzeñ Video4linux.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_archlib},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Video
%dir %{perl_vendorarch}/auto/Video
%dir %{perl_vendorarch}/auto/Video/*
%dir %{perl_vendorarch}/auto/Video/Capture/V4l
%dir %{perl_vendorarch}/auto/Video/Capture/VBI
%{perl_vendorarch}/auto/Video/*/*.bs
%{perl_vendorarch}/auto/Video/*/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Video/*/*.so
%attr(755,root,root) %{perl_vendorarch}/auto/Video/*/*/*.so
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
