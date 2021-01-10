#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fda
Version  : 5.1.9
Release  : 33
URL      : https://cran.r-project.org/src/contrib/fda_5.1.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fda_5.1.9.tar.gz
Summary  : Functional Data Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-rainbow
BuildRequires : R-fds
BuildRequires : R-rainbow
BuildRequires : buildreq-R

%description
analysis as described in Ramsay, J. O. and Silverman, B. W.

%prep
%setup -q -c -n fda
cd %{_builddir}/fda

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610306335

%install
export SOURCE_DATE_EPOCH=1610306335
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fda
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fda
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fda
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fda || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fda/DESCRIPTION
/usr/lib64/R/library/fda/INDEX
/usr/lib64/R/library/fda/Meta/Rd.rds
/usr/lib64/R/library/fda/Meta/data.rds
/usr/lib64/R/library/fda/Meta/demo.rds
/usr/lib64/R/library/fda/Meta/features.rds
/usr/lib64/R/library/fda/Meta/hsearch.rds
/usr/lib64/R/library/fda/Meta/links.rds
/usr/lib64/R/library/fda/Meta/nsInfo.rds
/usr/lib64/R/library/fda/Meta/package.rds
/usr/lib64/R/library/fda/NAMESPACE
/usr/lib64/R/library/fda/NEWS
/usr/lib64/R/library/fda/R/fda
/usr/lib64/R/library/fda/R/fda.rdb
/usr/lib64/R/library/fda/R/fda.rdx
/usr/lib64/R/library/fda/data/Rdata.rdb
/usr/lib64/R/library/fda/data/Rdata.rds
/usr/lib64/R/library/fda/data/Rdata.rdx
/usr/lib64/R/library/fda/demo/ElectricDemand.R
/usr/lib64/R/library/fda/demo/canadian-weather.R
/usr/lib64/R/library/fda/demo/gait.R
/usr/lib64/R/library/fda/demo/goodsindex.R
/usr/lib64/R/library/fda/demo/growth.R
/usr/lib64/R/library/fda/demo/growthreg.R
/usr/lib64/R/library/fda/demo/growthsetup.R
/usr/lib64/R/library/fda/demo/growthsmooth.R
/usr/lib64/R/library/fda/demo/handwrit.R
/usr/lib64/R/library/fda/demo/handwrit.pda.R
/usr/lib64/R/library/fda/demo/lip.R
/usr/lib64/R/library/fda/demo/pinch.R
/usr/lib64/R/library/fda/demo/weatherANOVA.R
/usr/lib64/R/library/fda/help/AnIndex
/usr/lib64/R/library/fda/help/aliases.rds
/usr/lib64/R/library/fda/help/fda.rdb
/usr/lib64/R/library/fda/help/fda.rdx
/usr/lib64/R/library/fda/help/paths.rds
/usr/lib64/R/library/fda/html/00Index.html
/usr/lib64/R/library/fda/html/R.css
