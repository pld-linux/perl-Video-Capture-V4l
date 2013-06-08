#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs working, not busy /dev/audio!)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Video
%define		pnam	Capture-V4l
Summary:	Video::Capture::V4l - Perl interface to the Video4linux framegrabber interface
Summary(pl.UTF-8):	Video::Capture::V4l - perlowy interfejs do urządzeń Video4linux
Name:		perl-Video-Capture-V4l
Version:	0.902
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Video/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6d8aa6df54e981b30a2fbc3ea453e0db
Patch0:		%{name}-make.patch
URL:		http://search.cpan.org/dist/Video-Capture-V4l/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to the Video4linux framegrabber interface.

%description -l pl.UTF-8
Perlowy interfejs do urządzeń Video4linux.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Video/*/*.so
%{perl_vendorarch}/auto/Video/*/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Video/*/*/*.so
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
