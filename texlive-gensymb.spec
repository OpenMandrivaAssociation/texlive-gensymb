%global tl_name gensymb
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.2
Release:	%{tl_revision}.1
Summary:	Generic symbols for both text and math mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gensymb
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gensymb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gensymb.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gensymb.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides generic commands \degree, \celsius, \perthousand, \micro and
\ohm which work both in text and maths mode. Various means are provided
to fake the symbols or take them from particular symbol fonts, if they
are not available in the default fonts used in the document. This should
be perfectly transparent at user level, so that one can apply the same
notation for units of measurement in text and math mode and with
arbitrary typefaces. Note that the package has been designed to work in
conjunction with units.sty. This package used to be part of the was
bundle, but has now become a package in its own right.

