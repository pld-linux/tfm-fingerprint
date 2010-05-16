Summary:	TouchChip TFM/ESS FingerPrint BSP
Summary(pl.UTF-8):	Moduł BSP do dla czytnika odcisków palców TouchChip TFM/ESS
Name:		tfm-fingerprint
Version:	1.0
Release:	0.1
License:	Custom EULA
Group:		Applications/Networking
Source0:	http://www.upek.com/support/download/TFMESS_BSP_LIN_%{version}.zip
# NoSource0-md5:	5da4e96ddb8ee446ef3fd7eff05fadc6
URL:		http://www.upek.com/support/dl_linux_bsp.asp
BuildRequires:	unzip
Requires(post,postun):	bioapi
Requires:	bioapi
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TouchChip TFM/ESS FingerPrint BSP.

%description -l pl.UTF-8
Moduł BSP do dla czytnika odcisków palców TouchChip TFM/ESS.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc,%{_libdir}}

echo 'security-level="5"' > $RPM_BUILD_ROOT%{_sysconfdir}/tfmessbsp.cfg
install libtfmessbsp.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{_bindir}/BioAPI-mod_install -fi %{_libdir}/libtfmessbsp.so

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.pdf REDISTRIBUTABLES.TXT relnotes.txt
%attr(755,root,root) %{_libdir}/lib*.so*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.cfg
