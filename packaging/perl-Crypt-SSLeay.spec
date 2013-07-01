#
# spec file for package perl-Crypt-SSLeay
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           perl-Crypt-SSLeay
%define cpan_name Crypt-SSLeay
Summary:        OpenSSL support for LWP
Version:        0.64
Release:        0
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Perl
Url:            http://search.cpan.org/dist/Crypt-SSLeay/
#Source:         http://www.cpan.org/authors/id/N/NA/NANIS/Crypt-SSLeay-0.58.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
Source1001: 	perl-Crypt-SSLeay.manifest
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(MIME::Base64)
BuildRequires:  openssl-devel
Requires:       perl(MIME::Base64)
Requires:       openssl

%description
This Perl module provides support for the HTTPS protocol under LWP, to
allow an 'LWP::UserAgent' object to perform GET, HEAD and POST requests.
Please see LWP for more information on POST requests.

The 'Crypt::SSLeay' package provides 'Net::SSL', which is loaded by
'LWP::Protocol::https' for https requests and provides the necessary SSL
glue.

This distribution also makes following deprecated modules available:

    Crypt::SSLeay::CTX
    Crypt::SSLeay::Conn
    Crypt::SSLeay::X509

Work on Crypt::SSLeay has been continued only to provide https support for
the LWP (libwww-perl) libraries.

%prep
%setup -q -n %{cpan_name}-%{version}
cp %{SOURCE1001} .
### rpmlint
# wrong-file-end-of-line-encoding
%{__perl} -pi -e 's|\r\n|\n|' README

%build
export CRYPT_SSLEAY_DEFAULT=/usr
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist


%files -f %{name}.files
%manifest %{name}.manifest
%defattr(-,root,root,-)

%changelog
