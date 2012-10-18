Summary: Creation of sky charts in Postscript or PDF format
Name: pp3
Version: 1.3.3
Release: %mkrel 7
License: MIT
Group: Sciences/Astronomy
Source0: http://prdownloads.sourceforge.net/pp3/pp3-%{version}.tar.bz2
Url: http://pp3.sourceforge.net
Patch0:	gcc47.patch

%description
PP3 creates celestial charts. It generates resolution independent
maps of very high graphical quality in Postscript or PDF format.
They can be used for example as illustrations in books or on web
pages. You may use the databases of the distribution or your own
databases converted to PP3's simple text format.

PP3 uses LaTeX+pstricks as the backend for generating the vector
graphics. You can add arbitrary labels to the map. The output is
configurable in many ways.

%prep
%setup -q
%patch0 -p1

%build
%make LOCAL="" CHANGEFILE=fmax.ch CXXFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p  %buildroot%_bindir
install -m755 pp3 %buildroot%_bindir/pp3
mkdir -p %buildroot%_datadir/%name
for i in *.dat; do
    install -m644 $i %buildroot%_datadir/%name/$i
done

%files
%doc COPYING README WHATSNEW
%doc examples
%{_bindir}/%name
%{_datadir}/%name
