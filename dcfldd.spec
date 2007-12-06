Summary:	Enhanced version of GNU dd with features useful for forensics
Name:		dcfldd
Version:	1.3.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/dcfldd/%{name}-%{version}-1.tar.gz
# Source0-md5:	952026c872f11b53ce0ec6681a3eef0a
URL:		http://dcfldd.sourceforge.net
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dcfldd is an enhanced version of GNU dd with features useful for
forensics and security. Based on the dd program found in the GNU
Coreutils package, dcfldd has the following additional features:

    - Hashing on-the-fly - dcfldd can hash the input data as it is being
      transferred, helping to ensure data integrity.
    - Status output - dcfldd can update the user of its progress in terms
      of the amount of data transferred and how much longer operation will
      take.
    - Flexible disk wipes - dcfldd can be used to wipe disks quickly and
      with a known pattern if desired.
    - Image/wipe Verify - dcfldd can verify that a target drive is a
      bit-for-bit match of the specified input file or pattern.
    - Multiple outputs - dcfldd can output to multiple files or disks at
      the same time.
    - Split output - dcfldd can split output to multiple files with more
      configurability than the split command.
    - Piped output and logs - dcfldd can send all its log data and output
      to commands as well as files natively.

%prep
%setup -q -n %{name}-%{version}-1

%build
./configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir}

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dcfldd
%{_mandir}/man1/*
