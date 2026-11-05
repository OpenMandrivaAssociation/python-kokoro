%global commit b96fef95e6a746495f92443fac7c688f90fc57fc

Name:		python-kokoro
Version:	0.9.4
Release:	1
Summary:	Kokoro text-to-speech engine
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/semidark/kokoro
# semidark fork: same engine for English and for German.
Source0:	https://github.com/semidark/kokoro/archive/%{commit}.tar.gz#/kokoro-%{commit}.tar.gz
Patch0:		python-kokoro-distro.patch
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Kokoro speech synthesis. This package is the engine and the kokoro
command. Checkpoints and voices are separate packages.

The official voices share the checkpoint in kokoro-model and are split
by language in kokoro-voices. The German Thorsten voice is the separate
fine-tune kokoro-voice-thorsten, with its own checkpoint.

Voices are read from /usr/share/kokoro, or from the directory named by
KOKORO_SHARE. A voice that is not installed is not downloaded.

%files
%doc README.md
%license LICENSE
%{_bindir}/kokoro
%{py_sitedir}/kokoro
%{py_sitedir}/kokoro-*.dist-info
