INCLUDES = $(PYTHON_INCLUDES) $(SYNCML_CFLAGS)

pkgpythondir = $(pyexecdir)/
pkgpyexecdir = $(pyexecdir)/

pkgpyexec_LTLIBRARIES = syncml.la
syncml_la_LDFLAGS = -module -avoid-version -export-symbols-regex initsyncml
syncml_la_LIBADD = $(SYNCML_LIBS)
syncml_la_SOURCES = \
	syncmlmodule.c \
	pysyncml.h

syncmlmodule.c: syncmlmodule_customizations.py syncmlmodule_generated.py
	$(PYTHON) syncmlmodule_customizations.py > syncmlmodule.c

syncmlmodule_generated.py: knowledge.py syncmlgen.py pysyncml.h
	$(PYTHON) syncmlgen.py pysyncml.h > syncmlmodule_generated.py

doc:
	cd .libs && epydoc syncml --html --introspect-only --name python-syncml --graph all -o ../docs ; cd ..

EXTRA_DIST = \
	test \
	AUTHORS NEWS INSTALL COPYING README \
	ChangeLog \
	autogen.sh \
	configure.ac \
	syncmlmodule.c  \
	knowledge.py \
	syncmlgen.py    \
	syncmlmodule_customizations.py  \
	syncmlmodule_generated.py

dist-hook:
	rm -rf `find $(distdir)/test -name '*.log'`
	rm -rf `find $(distdir)/test -name '*.pyc'`

.PHONY: doc
