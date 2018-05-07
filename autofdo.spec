Name:           autofdo
Version:        0.18
Release:        1%{?dist}
Summary:        Tools for converting perf.data profiles into a form usable by GCC and LLVM

License:        ASL 2.0
URL:            https://github.com/google/autofdo
Source0:        https://github.com/google/autofdo/archive/0.18.tar.gz

BuildRequires:  automake
BuildRequires:  openssl-devel


%description
Tools for converting perf.data profiles into a form usable by GCC and LLVM


%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%doc README
%{_bindir}/profile_merger
%{_bindir}/dump_gcov
%{_bindir}/sample_merger
%{_bindir}/profile_diff
%{_bindir}/profile_update
%{_bindir}/create_gcov
%{_bindir}/create_llvm_prof


%changelog
* Mon May  7 2018 David Malcolm <dmalcolm@redhat.com> - 0.18-1
- Initial packaging
