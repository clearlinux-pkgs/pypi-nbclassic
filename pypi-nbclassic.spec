#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nbclassic
Version  : 0.4.3
Release  : 24
URL      : https://files.pythonhosted.org/packages/39/0c/87ce838b0436e7c4f52a53d08f3e7ed17482043475594e6c38f6acaa096c/nbclassic-0.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/39/0c/87ce838b0436e7c4f52a53d08f3e7ed17482043475594e6c38f6acaa096c/nbclassic-0.4.3.tar.gz
Summary  : A web-based notebook environment for interactive computing
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: pypi-nbclassic-bin = %{version}-%{release}
Requires: pypi-nbclassic-data = %{version}-%{release}
Requires: pypi-nbclassic-license = %{version}-%{release}
Requires: pypi-nbclassic-python = %{version}-%{release}
Requires: pypi-nbclassic-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(babel)
BuildRequires : pypi(jupyter_packaging)
BuildRequires : pypi(jupyter_server)
BuildRequires : pypi(notebook_shim)
BuildRequires : pypi-jupyter_server
BuildRequires : pypi-jupyterlab_server

%description
# Jupyter Notebook as a Jupyter Server Extension
![Testing nbclassic](https://github.com/jupyterlab/nbclassic/workflows/Testing%20nbclassic/badge.svg)

%package bin
Summary: bin components for the pypi-nbclassic package.
Group: Binaries
Requires: pypi-nbclassic-data = %{version}-%{release}
Requires: pypi-nbclassic-license = %{version}-%{release}

%description bin
bin components for the pypi-nbclassic package.


%package data
Summary: data components for the pypi-nbclassic package.
Group: Data

%description data
data components for the pypi-nbclassic package.


%package license
Summary: license components for the pypi-nbclassic package.
Group: Default

%description license
license components for the pypi-nbclassic package.


%package python
Summary: python components for the pypi-nbclassic package.
Group: Default
Requires: pypi-nbclassic-python3 = %{version}-%{release}

%description python
python components for the pypi-nbclassic package.


%package python3
Summary: python3 components for the pypi-nbclassic package.
Group: Default
Requires: python3-core
Provides: pypi(nbclassic)
Requires: pypi(argon2_cffi)
Requires: pypi(ipykernel)
Requires: pypi(ipython_genutils)
Requires: pypi(jinja2)
Requires: pypi(jupyter_client)
Requires: pypi(jupyter_core)
Requires: pypi(jupyter_server)
Requires: pypi(nbconvert)
Requires: pypi(nbformat)
Requires: pypi(nest_asyncio)
Requires: pypi(notebook_shim)
Requires: pypi(prometheus_client)
Requires: pypi(pyzmq)
Requires: pypi(send2trash)
Requires: pypi(terminado)
Requires: pypi(tornado)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-nbclassic package.


%prep
%setup -q -n nbclassic-0.4.3
cd %{_builddir}/nbclassic-0.4.3
pushd ..
cp -a nbclassic-0.4.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657637900
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nbclassic
cp %{_builddir}/nbclassic-0.4.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-nbclassic/02f19bd915e1c4665a4bbadfceeb74baa4d45bd2
cp %{_builddir}/nbclassic-0.4.3/nbclassic/static/components/marked/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-nbclassic/c58a5ba3adc04dbb22ae3eaa904dc0da16bae9ec
cp %{_builddir}/nbclassic-0.4.3/nbclassic/static/components/text-encoding/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-nbclassic/7a2096cc227b93b3d41f3e8c5f6951fc965998f9
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
## install_append content
mkdir -p  %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/jupyter_server_config.d/nbclassic.json  %{buildroot}/usr/share/jupyter/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-bundlerextension
/usr/bin/jupyter-nbclassic
/usr/bin/jupyter-nbextension
/usr/bin/jupyter-serverextension

%files data
%defattr(-,root,root,-)
/usr/share/applications/jupyter-nbclassic.desktop
/usr/share/icons/hicolor/scalable/apps/nbclassic.svg
/usr/share/jupyter/nbclassic.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-nbclassic/02f19bd915e1c4665a4bbadfceeb74baa4d45bd2
/usr/share/package-licenses/pypi-nbclassic/7a2096cc227b93b3d41f3e8c5f6951fc965998f9
/usr/share/package-licenses/pypi-nbclassic/c58a5ba3adc04dbb22ae3eaa904dc0da16bae9ec

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
