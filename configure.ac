AC_PREREQ(2.50)

AC_INIT(python-syncml, 0.0.1, john.stowers@gmail.com)
AM_INIT_AUTOMAKE([1.9])
AC_CONFIG_SRCDIR(pysyncml.h)
AM_MAINTAINER_MODE
AC_SUBST(ACLOCAL_AMFLAGS, "$ACLOCAL_FLAGS -I m4")

AC_DEFINE(PYSYNCML_MAJOR_VERSION, 0, [PySyncml major version])
AC_DEFINE(PYSYNCML_MINOR_VERSION, 0, [PySyncml minor version])
AC_DEFINE(PYSYNCML_PATCH_VERSION, 1, [PySyncml patch version])

AC_PROG_CC
AC_DISABLE_STATIC
AC_PROG_LIBTOOL

AM_PATH_PYTHON(2.5)
AM_CHECK_PYTHON_HEADERS(,[AC_MSG_ERROR(could not find Python headers)])
PKG_CHECK_MODULES([SYNCML], [libsyncml-1.0])
AM_CHECK_PYMOD([pybindgen], , , AC_MSG_ERROR([Python module pybindgen required to run Conduit]))

AC_SUBST(SYNCML_CFLAGS)
AC_SUBST(SYNCML_LIBS)

AC_CONFIG_FILES([
Makefile
])

AC_OUTPUT

echo
echo $PACKAGE v$VERSION

echo
echo "Now type make to compile"
echo "Then su to root and type: make install"
echo
