#! /usr/bin/env python

import sys
import subprocess
import os.path

import pybindgen
from pybindgen import FileCodeSink
from pybindgen.typehandlers.base import param_type_matcher, Parameter
from pybindgen.gccxmlparser import ModuleParser
from pygccxml.declarations.class_declaration import class_declaration_t
from pygccxml.declarations.calldef import free_function_t
from pygccxml.declarations.cpptypes import pointer_t, const_t, declarated_t
from pygccxml.declarations.typedef import typedef_t

import knowledge

class PreScanHook(object):

    def __init__(self):
        self.classes = {} # class name -> None

    def __call__(self, dummy_module_parser,
                 pygccxml_definition,
                 global_annotations,
                 parameter_annotations):

        if isinstance(pygccxml_definition, class_declaration_t):

            # strip Sml from type name
            name = pygccxml_definition.name[3:]
            global_annotations['python_name'] = name

            # apply api customizations
            try:
                annotations = knowledge.CUSTOM_ANNOTATIONS[pygccxml_definition.name]
                global_annotations.update(annotations)
            except KeyError:
                #objects with a free function but no reference counting
                if name in knowledge.TYPES_WITH_NO_REF_COUNTING:
                    global_annotations['free_function'] = 'sml%sFree' % name

                ## objects with reference counting: Ref/Unref
                elif name in knowledge.TYPES_WITH_REF_COUNTING:
                    global_annotations['free_function'] = 'sml%sUnref' % name
                    global_annotations['incref_function'] = 'sml%sRef' % name
                    global_annotations['decref_function'] = 'sml%sUnref' % name

            # types to ignore
            if name in knowledge.TYPES_TO_IGNORE:
                global_annotations['ignore'] = 'true'

            if 'ignore' not in global_annotations:
                self.classes['Sml%s' % name] = None

            print "#","*"*20
            print "#\t",pygccxml_definition.name, pygccxml_definition.decl_string
            print "#\t",global_annotations

            return

        elif isinstance(pygccxml_definition, free_function_t):

            ## ignore SmlError methods, and those methods defined in headers
            ## that are not present in the library
            if pygccxml_definition.name.startswith("smlError") or pygccxml_definition.name in knowledge.LIES:
                global_annotations['ignore'] = 'true'
                return

            first_param = pygccxml_definition.arguments[0].type
            return_type = pygccxml_definition.return_type
            
            ## detect constructors
            if pygccxml_definition.name in knowledge.CONSTRUCTORS and isinstance(return_type, pointer_t):
                print "#\tCONSTRUCTOR"
                global_annotations['is_constructor_of'] = knowledge.CONSTRUCTORS[pygccxml_definition.name]
            else:
                cls = first_param

                print "#"*20,pygccxml_definition.name
                print "# Return type: %s (%s)" % (return_type, return_type.__class__.__name__)

                if isinstance(first_param, pointer_t):
                    cls = cls.base
                    print "# First Param is Pointer: ",cls
                if isinstance(cls, const_t):
                    cls = cls.base
                    print "# First Param is Const: ",cls
                if isinstance(cls, declarated_t):
                    cls = cls.declaration
                    print "# First Param is declarated: ",cls
                if not isinstance(cls, typedef_t):
                    print "# First Param is Not Typedef: ",cls
                    print "# ADD_FUNCTION"
                    cls = None

                #skip over plain functions, only add methods to classes
                #if a class was the first parameter
                if cls:
                    if cls.name in self.classes:
                        prefix = cls.name[0].lower() + cls.name[1:]
                        class_name = cls.name[3:]

                        print "#\tclass name: %s \n#\tprefix: %s \n#\tpython class name: %s \n#\tpygccxmldefinition name:%s" % (
                                            cls.name,prefix,class_name,pygccxml_definition.name)

                        print "#\tADD_FUNCTION_AS_METHOD"
                        if pygccxml_definition.name.startswith(prefix):
                            global_annotations['as_method'] = pygccxml_definition.name[len(prefix):]
                            global_annotations['of_class'] = 'Sml%s' % class_name
                            
                            #craft a minimally useful docstring that at least includes
                            #the types of the required params
                            docs = []
                            for i in pygccxml_definition.arguments[1:]:
                                docs.append(str(i))
                                
                            global_annotations['docstring'] = "Args: %s" % ", ".join(docs)
                            
                    else:
                        print "#\tDONT KNOW ANYTHING ABOUT", cls

        else:
            pass #raise Exception("Unknown pygccxml_definition: %s" % pygccxml_definition)

        #apply function argument customizations
        try:
            annotations = knowledge.PARAMETER_ANNOTATIONS[pygccxml_definition.name]
            parameter_annotations.update(annotations)
        except KeyError: pass
        
if __name__ == '__main__':
    #yuck, no waf or autotool here! Use pkg-config to get the libsyncml path
    pkgconfig = subprocess.Popen("pkg-config --cflags libsyncml-1.0",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = pkgconfig.communicate()
    if pkgconfig.wait() != 0:
        raise Exception(stderr)

    #strip -I
    includes = stdout.replace("-I",'').strip()

    out_file=sys.stdout
    header=sys.argv[1]
    cpp_path=[includes]

    module_parser = ModuleParser('syncml')
    module_parser.add_pre_scan_hook(PreScanHook())
    module = module_parser.parse(
                        header_files=[os.path.abspath(header)],
                        include_paths=cpp_path,
                        whitelist_paths=cpp_path,
                        pygen_sink=FileCodeSink(out_file))




