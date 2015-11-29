# TODO
# - do something (what?) with bs and nn locales
# - what about la locale?
# - does not work with awesome (with tiling wms?)
#
Summary:	Allarm panel applet for GNOME
Summary(pl.UTF-8):	Budzik dla GNOME
Name:		alarm-clock
Version:	0.9.18
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://89.76.224.23/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	b6160b767cb5634db0b9afbda3b6a5ac
URL:		http://alarm-clock.54.pl/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	dbus(org.freedesktop.Notifications)
Requires:	gstreamer-audio-formats
Requires:	python-gstreamer
Requires:	python-pynotify
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alarm Clock is a small alarm panel applet developed in Python for
GNOME/GTK desktop environments. It supports sound fading, scheduled
alarms, snooze option, passive window reminders, exception lists for
scheduled alarms, exporting alarms and much more!

%description -l pl.UTF-8
Alarm Clock to budzik napisany jako applet dla środowiska GNOME.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f {} \;
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/alarm-clock
%{_datadir}/%{name}
%{_desktopdir}/alarm-clock.desktop
%{_pixmapsdir}/alarm-clock.svg
%{py_sitescriptdir}/alarmclock
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/alarm_clock-*.egg-info
%endif
