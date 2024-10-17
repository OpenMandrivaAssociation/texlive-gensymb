Name:		texlive-gensymb
Version:	64740
Release:	2
Summary:	Generic symbols for both text and math mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gensymb
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gensymb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gensymb.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gensymb.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides generic commands \degree, \celsius, \perthousand,
\micro and \ohm which work both in text and maths mode. Various
means are provided to fake the symbols or take them from
particular symbol fonts, if they are not available in the
default fonts used in the document. This should be perfectly
transparent at user level, so that one can apply the same
notation for units of measurement in text and math mode and
with arbitrary typefaces. Note that the package has been
designed to work in conjunction with units.sty. This package
used to be part of the was bundle, but has now become a package
in its own right.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gensymb
%{_texmfdistdir}/tex/latex/gensymb
%doc %{_texmfdistdir}/doc/latex/gensymb

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
