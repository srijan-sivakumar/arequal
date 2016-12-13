Name:           arequal
Version:        1.0
Release:        1%{?dist}
Summary:        Tool to test data integrity of GlusterFS

License:        AGPL
URL:            https://github.com/nigelbabu/arequal
Source0:        https://github.com/nigelbabu/arequal/archive/%{version}.tar.gz

%description


%prep
%autosetup


%build
./autogen
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%doc README



%changelog
* Tue Dec 13 2016 Nigel Babu <nigelb@redhat.com>
- Initial RPM release.
