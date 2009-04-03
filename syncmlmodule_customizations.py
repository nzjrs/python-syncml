#! /usr/bin/env python
import sys

from pybindgen.cppmethod import CustomCppMethodWrapper
from pybindgen.typehandlers.base import param_type_matcher, return_type_matcher, Parameter
from pybindgen.typehandlers.inttype import IntParam, IntReturn
from pybindgen.typehandlers.stringtype import CStringParam, CStringReturn
from pybindgen import Module, FileCodeSink, write_preamble, param, retval

import syncmlmodule_generated

class SmlErrorParam(Parameter):
    DIRECTIONS = [Parameter.DIRECTION_OUT]
    CTYPES = ['SmlError * *']
    def __init__(self, ctype, name):
        super(SmlErrorParam, self).__init__(
            ctype, name, direction=Parameter.DIRECTION_OUT)

    def convert_python_to_c(self, wrapper):
        name = wrapper.declarations.declare_variable("SmlError*", "error", initializer="NULL")
        wrapper.call_params.append('&'+name)
        wrapper.after_call.write_error_check("smlErrorIsSet(&%s)" % name,
                                             'PyErr_SetString(PyExc_RuntimeError, smlErrorPrint(&%s));\n'
                                             'smlErrorDeref(&%s);' % (name, name))
                
    def convert_c_to_python(self, wrapper):
        raise NotImplementedError
param_type_matcher.register("SmlError", SmlErrorParam)

#because syncml.h does
#    typedef int SmlBool;
param_type_matcher.register("SmlBool", IntParam)
return_type_matcher.register("SmlBool", IntReturn)

#smlMD5ToString
param_type_matcher.register("unsigned char *", CStringParam)

#smlTransportDataNew
param_type_matcher.register("long unsigned int", IntParam)

def callback_customizations(module):
    #write the callbacks with c compatible apis
    #typedef void (* SmlManagerEventCb) (SmlManager *manager, SmlManagerEventType type, SmlSession *session, SmlError *error, void *userdata);
    #typedef void (* SmlCommandCb) (SmlSession *session, SmlCommand *cmd, void *userdata);
    #typedef void (* SmlHeaderCb) (SmlSession *session, SmlHeader *header, SmlCred *cred, void *userdata);
    #typedef void (* SmlStatusReplyCb) (SmlSession *session, SmlStatus *status, void *userdata);
    module.header.writeln(
'''
void _SmlManagerEventCb(SmlManager *manager, SmlManagerEventType type, SmlSession *session, SmlError *error, void *userdata)
{
    PyObject *py_callback, *py_eventType, *arglist;
    PySmlSession *py_session;
    PyGILState_STATE gstate;

    py_callback = (PyObject *)userdata;
    py_eventType = PyInt_FromLong(type);
    py_session = PyObject_New(PySmlSession, &PySmlSession_Type);
    py_session->obj = session;
    
    // Build up the argument list... 
    arglist = Py_BuildValue("(OO)", py_eventType, py_session);

    // for calling the Python compare callback function.
    gstate = PyGILState_Ensure();
    PyEval_CallObject(py_callback,arglist);

    Py_DECREF(arglist);
    Py_DECREF(py_session);
    PyGILState_Release(gstate);    
}

void _SmlCommandCb(SmlSession *session, SmlCommand *cmd, void *userdata)
{
    PyObject *py_callback, *arglist;
    PySmlCommand *py_command;
    PySmlSession *py_session;
    PyGILState_STATE gstate;

    py_callback = (PyObject *)userdata;
    py_session = PyObject_New(PySmlSession, &PySmlSession_Type);
    py_session->obj = session;
    
    py_command = PyObject_New(PySmlCommand, &PySmlCommand_Type);
    py_command->obj = cmd;

    // Build up the argument list... 
    arglist = Py_BuildValue("(OO)", py_session, py_command);

    // for calling the Python compare callback function.
    gstate = PyGILState_Ensure();
    PyEval_CallObject(py_callback,arglist);

    Py_DECREF(arglist);
    Py_DECREF(py_session);
    Py_DECREF(py_command);
    PyGILState_Release(gstate);    
}
''')

    wrapper_body = '''
PyObject *
_wrap_smlManagerSetEventCallback(PySmlManager *self, PyObject *args, PyObject **return_exception)    
{
    PyObject *exc_type, *traceback;
    PyObject *py_callback;
    SmlManager *manager;

    if (PyTuple_GET_SIZE(args) < 1) {
        PyErr_SetString(PyExc_TypeError, "Callback required");
        goto error;
    }
    py_callback = PyTuple_GET_ITEM(args, 0);

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "Callback should be callable");
        goto error;
    }
    smlManagerSetEventCallback(self->obj, _SmlManagerEventCb, (void *)py_callback);

    Py_INCREF(Py_None);
    return Py_None;

error:
    PyErr_Fetch(&exc_type, return_exception, &traceback);
    Py_XDECREF(exc_type);

    Py_XDECREF(traceback);
    return NULL;
}
'''
    module['SmlManager'].add_method(CustomCppMethodWrapper(
                                                "SetEventCallback",
                                                "_wrap_smlManagerSetEventCallback",
                                                wrapper_body,
                                                flags=["METH_VARARGS"]))

    wrapper_body = '''
PyObject *
_wrap_smlManagerObjectRegister(PySmlManager *self, PyObject *args, PyObject *kwargs, PyObject **return_exception) 
{
    PyObject *exc_type, *traceback;
    PyObject *py_retval;
    SmlBool retval;
    SmlCommandType type;
    PySmlSession *session;
    PySmlLocation *location;
    PySmlLocation *source;
    char const *contentType;
    PyObject *callback;
    PyObject *childCallback;
    SmlError *error2 = NULL;

    const char *keywords[] = {"type", "session", "location", "source", "contentType", "callback", "childCallback", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "iO!O!O!sO!O!", (char **) keywords, &type, &PySmlSession_Type, &session, &PySmlLocation_Type, &location, &PySmlLocation_Type, &source, &contentType, &PyFunction_Type, &callback, &PyFunction_Type, &childCallback)) {
        PyErr_SetString(PyExc_TypeError, "Incorrect Arguments");
        goto error;
    }
    retval = smlManagerObjectRegister(self->obj, type, session->obj, location->obj, source->obj, contentType, _SmlCommandCb, /*_SmlCommandCb*/NULL, (void *)callback, &error2);
    if (smlErrorIsSet(&error2)) {
        PyErr_SetString(PyExc_RuntimeError, smlErrorPrint(&error2));
        smlErrorDeref(&error2);
        goto error;
    }
    py_retval = Py_BuildValue("i", retval);
    return py_retval;
error:
    PyErr_Fetch(&exc_type, return_exception, &traceback);
    Py_XDECREF(exc_type);

    Py_XDECREF(traceback);
    return NULL;
}
'''
    module['SmlManager'].add_method(CustomCppMethodWrapper(
                                                "ObjectRegister",
                                                "_wrap_smlManagerObjectRegister",
                                                wrapper_body))




    #void smlManagerRegisterHeaderHandler(SmlManager *manager, SmlHeaderCb callback, SmlStatusReplyCb statuscb, void *userdata);

def main():
    out = FileCodeSink(sys.stdout)

    root_module = syncmlmodule_generated.module_init()
    root_module.add_include('"pysyncml.h"')

    syncmlmodule_generated.register_types(root_module)
    syncmlmodule_generated.register_methods(root_module)
    syncmlmodule_generated.register_functions(root_module)

    callback_customizations(root_module)

    write_preamble(out)
    root_module.generate(out)

if __name__ == '__main__':
    main()


