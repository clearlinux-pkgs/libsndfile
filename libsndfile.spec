#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDCF91FB242ACED (erikd@mega-nerd.com)
#
Name     : libsndfile
Version  : 1.0.28
Release  : 51
URL      : http://www.mega-nerd.com/libsndfile/files/libsndfile-1.0.28.tar.gz
Source0  : http://www.mega-nerd.com/libsndfile/files/libsndfile-1.0.28.tar.gz
Source1  : http://www.mega-nerd.com/libsndfile/files/libsndfile-1.0.28.tar.gz.asc
Summary  : A library for reading and writing audio files
Group    : Development/Tools
License  : LGPL-2.1
Requires: libsndfile-bin = %{version}-%{release}
Requires: libsndfile-filemap = %{version}-%{release}
Requires: libsndfile-lib = %{version}-%{release}
Requires: libsndfile-license = %{version}-%{release}
Requires: libsndfile-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-dev32
BuildRequires : flac-dev
BuildRequires : flac-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libogg-dev
BuildRequires : libogg-dev32
BuildRequires : libvorbis-dev
BuildRequires : libvorbis-dev32
BuildRequires : pkg-config
BuildRequires : sed
BuildRequires : sqlite-autoconf-dev
BuildRequires : sqlite-autoconf-dev32
Patch1: cve-2017-8365.patch
Patch2: cve-2017-8362.patch
Patch3: cve-2017-6892.patch
Patch4: CVE-2017-12562.patch
Patch5: cve-2017-14245.patch
Patch6: cve-2017-14634.patch
Patch7: cve-2018-13139.patch
Patch8: CVE-2018-19662.patch
Patch9: CVE-2018-19758.patch
Patch10: CVE-2019-3832.patch

%description
This is libsndfile, 1.0.28
libsndfile is a library of C routines for reading and writing
files containing sampled audio data.

%package bin
Summary: bin components for the libsndfile package.
Group: Binaries
Requires: libsndfile-license = %{version}-%{release}
Requires: libsndfile-filemap = %{version}-%{release}

%description bin
bin components for the libsndfile package.


%package dev
Summary: dev components for the libsndfile package.
Group: Development
Requires: libsndfile-lib = %{version}-%{release}
Requires: libsndfile-bin = %{version}-%{release}
Provides: libsndfile-devel = %{version}-%{release}
Requires: libsndfile = %{version}-%{release}

%description dev
dev components for the libsndfile package.


%package dev32
Summary: dev32 components for the libsndfile package.
Group: Default
Requires: libsndfile-lib32 = %{version}-%{release}
Requires: libsndfile-bin = %{version}-%{release}
Requires: libsndfile-dev = %{version}-%{release}

%description dev32
dev32 components for the libsndfile package.


%package doc
Summary: doc components for the libsndfile package.
Group: Documentation
Requires: libsndfile-man = %{version}-%{release}

%description doc
doc components for the libsndfile package.


%package filemap
Summary: filemap components for the libsndfile package.
Group: Default

%description filemap
filemap components for the libsndfile package.


%package lib
Summary: lib components for the libsndfile package.
Group: Libraries
Requires: libsndfile-license = %{version}-%{release}
Requires: libsndfile-filemap = %{version}-%{release}

%description lib
lib components for the libsndfile package.


%package lib32
Summary: lib32 components for the libsndfile package.
Group: Default
Requires: libsndfile-license = %{version}-%{release}

%description lib32
lib32 components for the libsndfile package.


%package license
Summary: license components for the libsndfile package.
Group: Default

%description license
license components for the libsndfile package.


%package man
Summary: man components for the libsndfile package.
Group: Default

%description man
man components for the libsndfile package.


%prep
%setup -q -n libsndfile-1.0.28
cd %{_builddir}/libsndfile-1.0.28
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
pushd ..
cp -a libsndfile-1.0.28 build32
popd
pushd ..
cp -a libsndfile-1.0.28 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664932441
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static --disable-octave
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --disable-octave --disable-octave  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --disable-octave
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1664932441
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libsndfile
cp %{_builddir}/libsndfile-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libsndfile/21c7a7d66a9430401a40a6f57bf212a6570b1819 || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## install_append content
cp src/sndfile.hh %{buildroot}/usr/include/sndfile.hh
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sndfile-cmp
/usr/bin/sndfile-concat
/usr/bin/sndfile-convert
/usr/bin/sndfile-deinterleave
/usr/bin/sndfile-info
/usr/bin/sndfile-interleave
/usr/bin/sndfile-metadata-get
/usr/bin/sndfile-metadata-set
/usr/bin/sndfile-play
/usr/bin/sndfile-regtest
/usr/bin/sndfile-salvage
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/sndfile.h
/usr/include/sndfile.hh
/usr/lib64/glibc-hwcaps/x86-64-v3/libsndfile.so
/usr/lib64/libsndfile.so
/usr/lib64/pkgconfig/sndfile.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libsndfile.so
/usr/lib32/pkgconfig/32sndfile.pc
/usr/lib32/pkgconfig/sndfile.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libsndfile/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-libsndfile

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libsndfile.so.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libsndfile.so.1.0.28
/usr/lib64/libsndfile.so.1
/usr/lib64/libsndfile.so.1.0.28

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libsndfile.so.1
/usr/lib32/libsndfile.so.1.0.28

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libsndfile/21c7a7d66a9430401a40a6f57bf212a6570b1819

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sndfile-cmp.1
/usr/share/man/man1/sndfile-concat.1
/usr/share/man/man1/sndfile-convert.1
/usr/share/man/man1/sndfile-deinterleave.1
/usr/share/man/man1/sndfile-info.1
/usr/share/man/man1/sndfile-interleave.1
/usr/share/man/man1/sndfile-metadata-get.1
/usr/share/man/man1/sndfile-metadata-set.1
/usr/share/man/man1/sndfile-play.1
/usr/share/man/man1/sndfile-salvage.1
