Name:		texlive-binarytree
Version:	41777
Release:	2
Summary:	Drawing binary trees using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/binarytree
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/binarytree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/binarytree.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/binarytree.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an easy but flexible way to draw binary
trees using TikZ. A path specification and the setting of
various options determine the style for each edge of the tree.
There is support for the external library of TikZ which does
not affect externalization of the rest of the TikZ figures in
the document. There is an option to use automatic file naming:
useful if the trees are often moved around.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/binarytree
%{_texmfdistdir}/tex/latex/binarytree
%doc %{_texmfdistdir}/doc/latex/binarytree

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
