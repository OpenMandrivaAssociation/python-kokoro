%global commit b96fef95e6a746495f92443fac7c688f90fc57fc

Name:		python-kokoro
Version:	0.9.4
Release:	2
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
Recommends:	kokoro-voice

%description
Kokoro speech synthesis. This package is the engine and the kokoro
command. Checkpoints and voices are separate packages.

Official voices are packaged one per voice, as kokoro-voice-<name>,
and share the checkpoint in kokoro-model. The German Thorsten voice is
kokoro-voice-thorsten, with its own checkpoint.

Voices are read from /usr/share/kokoro, or from the directory named by
KOKORO_SHARE. A voice that is not installed is not downloaded.

One text can mix voices, languages, and raw phonemes. A voice tag
selects another style pack. Packs that share a checkpoint stay on
that model; Thorsten is a separate checkpoint, and a span in that
voice uses it. A language tag selects spelling rules and keeps the
voice, so an English title can sit inside a German sentence. Phonemes
outside the active checkpoint's alphabet are replaced with a close
match, or dropped. A pitch tag holds a note. note="A4" is the
equal-tempered name (A4 is 440; with no number the note is in octave
4). freq="..." is hertz and can sit between the notes. Words tagged
one after another stay one line, for example <pitch note="A4">I</pitch>
<pitch note="C5">like</pitch><pitch note="F4">dogs</pitch>.

%files
%doc README.md
%license LICENSE
%{_bindir}/kokoro
%{py_sitedir}/kokoro
%{py_sitedir}/kokoro-*.dist-info
