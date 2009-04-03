from pybindgen import Module, FileCodeSink, param, retval, cppclass


import pybindgen.settings
import warnings

class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, wrapper, exception, traceback_):
        warnings.warn("exception %r in wrapper %s" % (exception, wrapper))
        return True
pybindgen.settings.error_handler = ErrorHandler()


import sys

def module_init():
    root_module = Module('syncml', cpp_namespace='::')
    return root_module

def register_types(module):
    root_module = module.get_root()
    
    module.add_enum('SmlAlertType', ['SML_ALERT_UNKNOWN', 'SML_ALERT_DISPLAY', 'SML_ALERT_TWO_WAY', 'SML_ALERT_SLOW_SYNC', 'SML_ALERT_ONE_WAY_FROM_CLIENT', 'SML_ALERT_REFRESH_FROM_CLIENT', 'SML_ALERT_ONE_WAY_FROM_SERVER', 'SML_ALERT_REFRESH_FROM_SERVER', 'SML_ALERT_TWO_WAY_BY_SERVER', 'SML_ALERT_ONE_WAY_FROM_CLIENT_BY_SERVER', 'SML_ALERT_REFRESH_FROM_CLIENT_BY_SERVER', 'SML_ALERT_ONE_WAY_FROM_SERVER_BY_SERVER', 'SML_ALERT_REFRESH_FROM_SERVER_BY_SERVER', 'SML_ALERT_RESULT', 'SML_ALERT_NEXT_MESSAGE', 'SML_ALERT_NO_END_OF_DATA'])
    module.add_enum('SmlDevInfSyncCap', ['SML_DEVINF_SYNCTYPE_UNKNOWN', 'SML_DEVINF_SYNCTYPE_TWO_WAY', 'SML_DEVINF_SYNCTYPE_SLOW_SYNC', 'SML_DEVINF_SYNCTYPE_ONE_WAY_FROM_CLIENT', 'SML_DEVINF_SYNCTYPE_REFRESH_FROM_CLIENT', 'SML_DEVINF_SYNCTYPE_ONE_WAY_FROM_SERVER', 'SML_DEVINF_SYNCTYPE_REFRESH_FROM_SERVER', 'SML_DEVINF_SYNCTYPE_SERVER_ALERTED_SYNC'])
    module.add_enum('SmlTransportEventType', ['SML_TRANSPORT_EVENT_CONNECT_DONE', 'SML_TRANSPORT_EVENT_DISCONNECT_DONE', 'SML_TRANSPORT_EVENT_ERROR', 'SML_TRANSPORT_EVENT_DATA'])
    module.add_enum('SmlErrorClass', ['SML_ERRORCLASS_UNKNOWN', 'SML_ERRORCLASS_SUCCESS', 'SML_ERRORCLASS_RETRY', 'SML_ERRORCLASS_FATAL'])
    module.add_enum('SmlMimeType', ['SML_MIMETYPE_UNKNOWN', 'SML_MIMETYPE_XML', 'SML_MIMETYPE_WBXML', 'SML_MIMETYPE_SAN'])
    module.add_enum('SmlErrorType', ['SML_ERROR_UNKNOWN', 'SML_IN_PROGRESS', 'SML_NO_ERROR', 'SML_ITEM_ADDED', 'SML_PROCESSING_ACCEPTED', 'SML_NON_AUTHORITATIVE', 'SML_NO_CONTENT', 'SML_RESET_CONTENT', 'SML_PARTIAL_CONTENT', 'SML_CONFLICT_MERGE', 'SML_CONFLICT_CLIENT_WIN', 'SML_CONFLICT_DUPLICATE', 'SML_DELETE_NO_ARCHIVE', 'SML_DELETE_NOT_FOUND', 'SML_AUTH_ACCEPTED', 'SML_CHUNK_ACCEPTED', 'SML_OPERATION_CANCELLED', 'SML_NOT_EXECUTED', 'SML_ATOMIC_ROLLBACK_OK', 'SML_ERROR_RETRY', 'SML_ERROR_TIMEOUT_RETRY', 'SML_ERROR_FOUND_RETRY', 'SML_ERROR_SEE_OTHER_RETRY', 'SML_ERROR_NOT_MODIFIED', 'SML_ERROR_USE_PROXY', 'SML_ERROR_BAD_REQUEST', 'SML_ERROR_AUTH_REJECTED', 'SML_ERROR_PAYMENT_NEEDED', 'SML_ERROR_FORBIDDEN', 'SML_ERROR_NOT_FOUND', 'SML_ERROR_COMMAND_NOT_ALLOWED', 'SML_ERROR_UNSUPPORTED_FEATURE', 'SML_ERROR_AUTH_REQUIRED', 'SML_ERROR_ALREADY_EXISTS', 'SML_ERROR_SIZE_MISMATCH', 'SML_ERROR_GENERIC', 'SML_ERROR_IO_ERROR', 'SML_ERROR_NOT_SUPPORTED', 'SML_ERROR_TIMEOUT', 'SML_ERROR_DISCONNECTED', 'SML_ERROR_FILE_NOT_FOUND', 'SML_ERROR_MISCONFIGURATION', 'SML_ERROR_INITIALIZATION', 'SML_ERROR_REQUIRE_REFRESH', 'SML_ERROR_EXPECTED', 'SML_ERROR_NO_CONNECTION', 'SML_ERROR_TEMPORARY', 'SML_ERROR_NO_MEMORY'])
    module.add_enum('SmlTransportType', ['SML_TRANSPORT_HTTP_SERVER', 'SML_TRANSPORT_HTTP_CLIENT', 'SML_TRANSPORT_OBEX_CLIENT', 'SML_TRANSPORT_OBEX_SERVER'])
    module.add_enum('SmlTransportResult', ['SML_RESULT_OK', 'SML_RESULT_RETRY', 'SML_RESULT_FATAL'])
    module.add_enum('SmlSessionEventType', ['SML_SESSION_EVENT_ERROR', 'SML_SESSION_EVENT_COMMAND_START', 'SML_SESSION_EVENT_CHILD_COMMAND', 'SML_SESSION_EVENT_HEADER_REPLY', 'SML_SESSION_EVENT_FINAL', 'SML_SESSION_EVENT_END', 'SML_SESSION_EVENT_FLUSH', 'SML_SESSION_EVENT_COMMAND_END', 'SML_SESSION_EVENT_RESPONSE_URI'])
    module.add_enum('SmlManagerEventType', ['SML_MANAGER_CONNECT_DONE', 'SML_MANAGER_DISCONNECT_DONE', 'SML_MANAGER_TRANSPORT_ERROR', 'SML_MANAGER_SESSION_NEW', 'SML_MANAGER_SESSION_FINAL', 'SML_MANAGER_SESSION_END', 'SML_MANAGER_SESSION_FLUSH', 'SML_MANAGER_SESSION_WARNING', 'SML_MANAGER_SESSION_ERROR'])
    module.add_enum('SmlDevInfVersion', ['SML_DEVINF_VERSION_UNKNOWN', 'SML_DEVINF_VERSION_10', 'SML_DEVINF_VERSION_11', 'SML_DEVINF_VERSION_12'])
    module.add_enum('SmlChangeType', ['SML_CHANGE_UNKNOWN', 'SML_CHANGE_ADD', 'SML_CHANGE_REPLACE', 'SML_CHANGE_DELETE'])
    module.add_enum('SmlNotificationUIMode', ['SML_SAN_UIMODE_UNSPECIFIED', 'SML_SAN_UIMODE_BACKGROUND', 'SML_SAN_UIMODE_INFORMATIVE', 'SML_SAN_UIMODE_USER'])
    module.add_enum('SmlDevInfDevTyp', ['SML_DEVINF_DEVTYPE_UNKNOWN', 'SML_DEVINF_DEVTYPE_PAGER', 'SML_DEVINF_DEVTYPE_HANDHELD', 'SML_DEVINF_DEVTYPE_PDA', 'SML_DEVINF_DEVTYPE_PHONE', 'SML_DEVINF_DEVTYPE_SMARTPHONE', 'SML_DEVINF_DEVTYPE_SERVER', 'SML_DEVINF_DEVTYPE_WORKSTATION'])
    module.add_enum('SmlCommandType', ['SML_COMMAND_TYPE_UNKNOWN', 'SML_COMMAND_TYPE_ALERT', 'SML_COMMAND_TYPE_SYNC', 'SML_COMMAND_TYPE_PUT', 'SML_COMMAND_TYPE_HEADER', 'SML_COMMAND_TYPE_ADD', 'SML_COMMAND_TYPE_REPLACE', 'SML_COMMAND_TYPE_DELETE', 'SML_COMMAND_TYPE_MAP', 'SML_COMMAND_TYPE_GET', 'SML_COMMAND_TYPE_RESULTS'])
    module.add_enum('SmlFormatType', ['SML_FORMAT_TYPE_UNKNOWN', 'SML_FORMAT_TYPE_BASE64'])
    module.add_enum('SmlNotificationVersion', ['SML_SAN_VERSION_UNKNOWN', 'SML_SAN_VERSION_10', 'SML_SAN_VERSION_11', 'SML_SAN_VERSION_12'])
    module.add_enum('SmlDsServerType', ['SML_DS_UNKNOWN_TYPE', 'SML_DS_SERVER', 'SML_DS_CLIENT'])
    module.add_enum('SmlAuthType', ['SML_AUTH_TYPE_UNKNOWN', 'SML_AUTH_TYPE_BASIC', 'SML_AUTH_TYPE_MD5'])
    module.add_enum('SmlTransportConnectionType', ['SML_TRANSPORT_CONNECTION_TYPE_UNKNOWN', 'SML_TRANSPORT_CONNECTION_TYPE_SERIAL', 'SML_TRANSPORT_CONNECTION_TYPE_BLUETOOTH', 'SML_TRANSPORT_CONNECTION_TYPE_IRDA', 'SML_TRANSPORT_CONNECTION_TYPE_NET', 'SML_TRANSPORT_CONNECTION_TYPE_USB'])
    module.add_enum('SmlNotificationInitiator', ['SML_SAN_INITIATOR_USER', 'SML_SAN_INITIATOR_SERVER'])
    module.add_enum('SmlDevInfDataType', ['SML_DEVINF_DATATYPE_UNKNOWN', 'SML_DEVINF_DATATYPE_CHR', 'SML_DEVINF_DATATYPE_INT', 'SML_DEVINF_DATATYPE_BOOL', 'SML_DEVINF_DATATYPE_BIN', 'SML_DEVINF_DATATYPE_DATE', 'SML_DEVINF_DATATYPE_PHONE'])
    module.add_enum('SmlProtocolType', ['SML_PROTOCOL_UNKNOWN', 'SML_PROTOCOL_SYNCML', 'SML_PROTOCOL_DM'])
    module.add_enum('SmlProtocolVersion', ['SML_VERSION_UNKNOWN', 'SML_VERSION_10', 'SML_VERSION_11', 'SML_VERSION_12'])
    module.add_enum('SmlDevInfCTCapType', ['SML_DEVINF_CTCAP_UNKNOWN', 'SML_DEVINF_CTCAP_CTTYPE', 'SML_DEVINF_CTCAP_PROPNAME', 'SML_DEVINF_CTCAP_VALENUM', 'SML_DEVINF_CTCAP_DATATYPE', 'SML_DEVINF_CTCAP_SIZE', 'SML_DEVINF_CTCAP_DISPLAYNAME', 'SML_DEVINF_CTCAP_PARAMNAME', 'SML_DEVINF_CTCAP_VERCT', 'SML_DEVINF_CTCAP_PROPERTY', 'SML_DEVINF_CTCAP_PROPPARAM', 'SML_DEVINF_CTCAP_NOTRUNCATE', 'SML_DEVINF_CTCAP_MAXOCCUR', 'SML_DEVINF_CTCAP_MAXSIZE'])
    module.add_enum('SmlSessionType', ['SML_SESSION_TYPE_SERVER', 'SML_SESSION_TYPE_CLIENT'])
# ********************
#	SmlTransportData ::SmlTransportData
#	{'decref_function': 'smlTransportDataDeref', 'free_function': 'smlTransportDataDeref', 'incref_function': 'smlTransportDataRef', 'python_name': 'TransportData'}
    module.add_class('SmlTransportData', allow_subclassing=False, automatic_type_narrowing=False, python_name='TransportData', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlTransportDataDeref'))
# ********************
#	SmlDevInfAgent ::SmlDevInfAgent
#	{'free_function': 'smlDevInfAgentFree', 'python_name': 'DevInfAgent'}
    module.add_class('SmlDevInfAgent', allow_subclassing=False, automatic_type_narrowing=False, python_name='DevInfAgent', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlDevInfAgentFree'))
# ********************
#	SmlAnchor ::SmlAnchor
#	{'free_function': 'smlAnchorFree', 'python_name': 'Anchor'}
    module.add_class('SmlAnchor', allow_subclassing=False, automatic_type_narrowing=False, python_name='Anchor', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlAnchorFree'))
# ********************
#	SmlDevInfDataStore ::SmlDevInfDataStore
#	{'decref_function': 'smlDevInfDataStoreUnref', 'free_function': 'smlDevInfDataStoreUnref', 'incref_function': 'smlDevInfDataStoreRef', 'python_name': 'DevInfDataStore'}
    module.add_class('SmlDevInfDataStore', allow_subclassing=False, automatic_type_narrowing=False, python_name='DevInfDataStore', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlDevInfDataStoreUnref'))
# ********************
#	SmlDevInfPropParam ::SmlDevInfPropParam
#	{'free_function': 'HACKFree', 'python_name': 'DevInfPropParam'}
    module.add_class('SmlDevInfPropParam', allow_subclassing=False, automatic_type_narrowing=False, python_name='DevInfPropParam', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('HACKFree'))
# ********************
#	SmlDevInfContentType ::SmlDevInfContentType
#	{'free_function': 'HACKFree', 'python_name': 'DevInfContentType'}
    module.add_class('SmlDevInfContentType', allow_subclassing=False, automatic_type_narrowing=False, python_name='DevInfContentType', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('HACKFree'))
# ********************
#	SmlDevInfCTCap ::SmlDevInfCTCap
#	{'free_function': 'HACKFree', 'python_name': 'DevInfCTCap'}
    module.add_class('SmlDevInfCTCap', allow_subclassing=False, automatic_type_narrowing=False, python_name='DevInfCTCap', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('HACKFree'))
# ********************
#	SmlDevInf ::SmlDevInf
#	{'decref_function': 'smlDevInfUnref', 'free_function': 'smlDevInfUnref', 'incref_function': 'smlDevInfRef', 'python_name': 'DevInf'}
    module.add_class('SmlDevInf', allow_subclassing=False, automatic_type_narrowing=False, python_name='DevInf', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlDevInfUnref'))
# ********************
#	SmlChal ::SmlChal
#	{'decref_function': 'smlChalUnref', 'free_function': 'smlChalUnref', 'incref_function': 'smlChalRef', 'python_name': 'Chal'}
    module.add_class('SmlChal', allow_subclassing=False, automatic_type_narrowing=False, python_name='Chal', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlChalUnref'))
# ********************
#	SmlPendingStatus ::SmlPendingStatus
#	{'ignore': 'true', 'python_name': 'PendingStatus'}
# ********************
#	SmlAssembler ::SmlAssembler
#	{'ignore': 'true', 'python_name': 'Assembler'}
# ********************
#	SmlNotification ::SmlNotification
#	{'free_function': 'smlNotificationFree', 'python_name': 'Notification'}
    module.add_class('SmlNotification', allow_subclassing=False, automatic_type_narrowing=False, python_name='Notification', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlNotificationFree'))
# ********************
#	SmlMapItem ::SmlMapItem
#	{'decref_function': 'smlMapItemUnref', 'free_function': 'smlMapItemUnref', 'incref_function': 'smlMapItemRef', 'python_name': 'MapItem'}
    module.add_class('SmlMapItem', allow_subclassing=False, automatic_type_narrowing=False, python_name='MapItem', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlMapItemUnref'))
# ********************
#	SmlHeader ::SmlHeader
#	{'free_function': 'smlHeaderFree', 'python_name': 'Header'}
    module.add_class('SmlHeader', allow_subclassing=False, automatic_type_narrowing=False, python_name='Header', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlHeaderFree'))
# ********************
#	SmlManager ::SmlManager
#	{'free_function': 'smlManagerFree', 'python_name': 'Manager'}
    module.add_class('SmlManager', allow_subclassing=False, automatic_type_narrowing=False, python_name='Manager', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlManagerFree'))
# ********************
#	SmlLocation ::SmlLocation
#	{'decref_function': 'smlLocationUnref', 'free_function': 'smlLocationUnref', 'incref_function': 'smlLocationRef', 'python_name': 'Location'}
    module.add_class('SmlLocation', allow_subclassing=False, automatic_type_narrowing=False, python_name='Location', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlLocationUnref'))
# ********************
#	SmlDevInfProperty ::SmlDevInfProperty
#	{'free_function': 'HACKFree', 'python_name': 'DevInfProperty'}
    module.add_class('SmlDevInfProperty', allow_subclassing=False, automatic_type_narrowing=False, python_name='DevInfProperty', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('HACKFree'))
# ********************
#	SmlTransport ::SmlTransport
#	{'free_function': 'smlTransportFree', 'python_name': 'Transport'}
    module.add_class('SmlTransport', allow_subclassing=False, automatic_type_narrowing=False, python_name='Transport', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlTransportFree'))
# ********************
#	SmlItem ::SmlItem
#	{'decref_function': 'smlItemUnref', 'free_function': 'smlItemUnref', 'incref_function': 'smlItemRef', 'python_name': 'Item'}
    module.add_class('SmlItem', allow_subclassing=False, automatic_type_narrowing=False, python_name='Item', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlItemUnref'))
# ********************
#	SmlParser ::SmlParser
#	{'ignore': 'true', 'python_name': 'Parser'}
# ********************
#	SmlCommand ::SmlCommand
#	{'decref_function': 'smlCommandUnref', 'free_function': 'smlCommandUnref', 'incref_function': 'smlCommandRef', 'python_name': 'Command'}
    module.add_class('SmlCommand', allow_subclassing=False, automatic_type_narrowing=False, python_name='Command', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlCommandUnref'))
# ********************
#	SmlCred ::SmlCred
#	{'decref_function': 'smlCredUnref', 'free_function': 'smlCredUnref', 'incref_function': 'smlCredRef', 'python_name': 'Cred'}
    module.add_class('SmlCred', allow_subclassing=False, automatic_type_narrowing=False, python_name='Cred', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlCredUnref'))
# ********************
#	SmlLink ::SmlLink
#	{'decref_function': 'smlLinkDeref', 'free_function': 'smlLinkDeref', 'incref_function': 'smlLinkRef', 'python_name': 'Link'}
    module.add_class('SmlLink', allow_subclassing=False, automatic_type_narrowing=False, python_name='Link', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlLinkDeref'))
# ********************
#	SmlSession ::SmlSession
#	{'decref_function': 'smlSessionUnref', 'free_function': 'smlSessionUnref', 'incref_function': 'smlSessionRef', 'python_name': 'Session'}
    module.add_class('SmlSession', allow_subclassing=False, automatic_type_narrowing=False, python_name='Session', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlSessionUnref'))
# ********************
#	SmlError ::SmlError
#	{'ignore': 'true', 'python_name': 'Error'}
# ********************
#	SmlObject ::SmlObject
#	{'free_function': 'smlManagerObjectFree', 'python_name': 'Object'}
    module.add_class('SmlObject', allow_subclassing=False, automatic_type_narrowing=False, python_name='Object', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlManagerObjectFree'))
# ********************
#	SmlAuthenticator ::SmlAuthenticator
#	{'free_function': 'smlAuthFree', 'python_name': 'Authenticator'}
    module.add_class('SmlAuthenticator', allow_subclassing=False, automatic_type_narrowing=False, python_name='Authenticator', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlAuthFree'))
# ********************
#	SmlStatus ::SmlStatus
#	{'decref_function': 'smlStatusUnref', 'free_function': 'smlStatusUnref', 'incref_function': 'smlStatusRef', 'python_name': 'Status'}
    module.add_class('SmlStatus', allow_subclassing=False, automatic_type_narrowing=False, python_name='Status', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlStatusUnref'))
# ********************
#	SmlSanAlert ::SmlSanAlert
#	{'free_function': 'smlNotificationFreeAlert', 'python_name': 'SanAlert'}
    module.add_class('SmlSanAlert', allow_subclassing=False, automatic_type_narrowing=False, python_name='SanAlert', incomplete_type=True, memory_policy=cppclass.FreeFunctionPolicy('smlNotificationFreeAlert'))
    
    ## Register a nested module for the namespace std
    
    nested_module = module.add_cpp_namespace('std')
    register_types_std(nested_module)
    

def register_types_std(module):
    root_module = module.get_root()
    

def register_methods(root_module):
    return

def register_functions(root_module):
    module = root_module
#################### smlTransportGetType
# Return type: SmlTransportType (declarated_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportGetType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportGetType', 'SmlTransportType', [param('SmlTransport *', 'tsp', transfer_ownership=False)], custom_name='GetType')
#################### smlDevInfContentTypeGetCTType
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfContentType const
# First Param is Const:  SmlDevInfContentType
# First Param is declarated:  SmlDevInfContentType [typedef]
#	class name: SmlDevInfContentType 
#	prefix: smlDevInfContentType 
#	python class name: DevInfContentType 
#	pygccxmldefinition name:smlDevInfContentTypeGetCTType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfContentType'].add_function_as_method('smlDevInfContentTypeGetCTType', 'char *', [param('SmlDevInfContentType *', 'ct', transfer_ownership=False, is_const=True)], custom_name='GetCTType')
#################### smlDevInfCTCapAddProperty
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfCTCap
# First Param is declarated:  SmlDevInfCTCap [typedef]
#	class name: SmlDevInfCTCap 
#	prefix: smlDevInfCTCap 
#	python class name: DevInfCTCap 
#	pygccxmldefinition name:smlDevInfCTCapAddProperty
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfCTCap'].add_function_as_method('smlDevInfCTCapAddProperty', 'void', [param('SmlDevInfCTCap *', 'ctcap', transfer_ownership=False), param('SmlDevInfProperty *', 'property', transfer_ownership=False)], custom_name='AddProperty')
#################### smlTransportInitialize
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportInitialize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportInitialize', 'SmlBool', [param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='Initialize')
#	CONSTRUCTOR
    root_module['SmlDevInf'].add_function_as_constructor('smlDevInfNew', retval('SmlDevInf *', caller_owns_return=True), [param('char *', 'devid', transfer_ownership=False, is_const=True), param('SmlDevInfDevTyp', 'devtyp'), param('SmlError * *', 'error')])
#################### smlSessionReceiveHeader
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionReceiveHeader
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionReceiveHeader', 'SmlBool', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlHeader *', 'header', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='ReceiveHeader')
#################### smlDevInfGetMaxGUIDSize
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfGetMaxGUIDSize
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlDevInfGetMaxGUIDSize', 
                        'unsigned int', 
                        [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True)])
#################### smlDevInfPropParamNumValEnums
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInfPropParam const
# First Param is Const:  SmlDevInfPropParam
# First Param is declarated:  SmlDevInfPropParam [typedef]
#	class name: SmlDevInfPropParam 
#	prefix: smlDevInfPropParam 
#	python class name: DevInfPropParam 
#	pygccxmldefinition name:smlDevInfPropParamNumValEnums
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfPropParam'].add_function_as_method('smlDevInfPropParamNumValEnums', 'unsigned int', [param('SmlDevInfPropParam *', 'propParam', transfer_ownership=False, is_const=True)], custom_name='NumValEnums')
#################### smlSessionStartCommand
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionStartCommand
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionStartCommand', 'SmlBool', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlCommand *', 'cmd', transfer_ownership=False), param('SmlCommand *', 'parent', transfer_ownership=False), param('SmlStatusReplyCb *', 'callback'), param('void *', 'userdata'), param('SmlError * *', 'error')], custom_name='StartCommand')
#################### smlSessionEndCommand
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionEndCommand
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionEndCommand', 'SmlBool', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlCommand *', 'parent', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='EndCommand')
#################### smlBase64Encode
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlBase64Encode', 
                        'SmlBool', 
                        [param('char *', 'input', transfer_ownership=False, is_const=True), param('char * *', 'output'), param('SmlError * *', 'error')])
#################### smlCredNewFromString
# Return type: SmlCred * (pointer_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlCredNewFromString', 
                        'SmlCred *', 
                        [param('char *', 'type', transfer_ownership=False, is_const=True), param('char *', 'format', transfer_ownership=False, is_const=True), param('char *', 'data', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlChalNewFromBase64
# Return type: SmlChal * (pointer_t)
# First Param is declarated:  SmlAuthType [enumeration]
# First Param is Not Typedef:  SmlAuthType [enumeration]
# ADD_FUNCTION
    module.add_function('smlChalNewFromBase64', 
                        'SmlChal *', 
                        [param('SmlAuthType', 'type'), param('char *', 'nonce', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlSessionSendCommand
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionSendCommand
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionSendCommand', 'SmlBool', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlCommand *', 'cmd', transfer_ownership=False), param('SmlCommand *', 'parent', transfer_ownership=False), param('SmlStatusReplyCb *', 'callback'), param('void *', 'userdata'), param('SmlError * *', 'error')], custom_name='SendCommand')
#################### smlDevInfPropertyAddPropParam
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyAddPropParam
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyAddPropParam', 'void', [param('SmlDevInfProperty *', 'property', transfer_ownership=False), param('SmlDevInfPropParam *', 'propParam', transfer_ownership=False)], custom_name='AddPropParam')
#################### smlTransportDataRef
# Return type: SmlTransportData * (pointer_t)
# First Param is Pointer:  SmlTransportData
# First Param is declarated:  SmlTransportData [typedef]
#	class name: SmlTransportData 
#	prefix: smlTransportData 
#	python class name: TransportData 
#	pygccxmldefinition name:smlTransportDataRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransportData'].add_function_as_method('smlTransportDataRef', 'SmlTransportData *', [param('SmlTransportData *', 'data', transfer_ownership=False)], custom_name='Ref')
#################### smlDevInfPropertySetMaxOccur
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertySetMaxOccur
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertySetMaxOccur', 'void', [param('SmlDevInfProperty *', 'property', transfer_ownership=False), param('unsigned int', 'maxOccur')], custom_name='SetMaxOccur')
#	CONSTRUCTOR
    root_module['SmlSession'].add_function_as_constructor('smlSessionNew', retval('SmlSession *', caller_owns_return=True), [param('SmlSessionType', 'sessionType'), param('SmlMimeType', 'mimetype'), param('SmlProtocolVersion', 'version'), param('SmlProtocolType', 'protocol'), param('SmlLocation *', 'target', transfer_ownership=False), param('SmlLocation *', 'source', transfer_ownership=False), param('char *', 'sessionID', transfer_ownership=False, is_const=True), param('unsigned int', 'messageID'), param('SmlError * *', 'error')])
#################### smlDevInfDataStoreGetRxPref
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreGetRxPref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreGetRxPref', 'SmlBool', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True), param('char * *', 'contenttype'), param('char * *', 'version')], custom_name='GetRxPref')
#################### smlDevInfPropertyGetMaxOccur
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInfProperty const
# First Param is Const:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyGetMaxOccur
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyGetMaxOccur', 'unsigned int', [param('SmlDevInfProperty *', 'property', transfer_ownership=False, is_const=True)], custom_name='GetMaxOccur')
#	CONSTRUCTOR
    root_module['SmlNotification'].add_function_as_constructor('smlNotificationNew', retval('SmlNotification *', caller_owns_return=True), [param('SmlNotificationVersion', 'version'), param('SmlNotificationUIMode', 'mode'), param('SmlNotificationInitiator', 'init'), param('unsigned int', 'sessionID'), param('char *', 'identifier', transfer_ownership=False, is_const=True), param('char *', 'target', transfer_ownership=False, is_const=True), param('SmlMimeType', 'type'), param('SmlError * *', 'error')])
#################### smlDevInfCTCapNumProperties
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInfCTCap const
# First Param is Const:  SmlDevInfCTCap
# First Param is declarated:  SmlDevInfCTCap [typedef]
#	class name: SmlDevInfCTCap 
#	prefix: smlDevInfCTCap 
#	python class name: DevInfCTCap 
#	pygccxmldefinition name:smlDevInfCTCapNumProperties
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfCTCap'].add_function_as_method('smlDevInfCTCapNumProperties', 'unsigned int', [param('SmlDevInfCTCap *', 'ctcap', transfer_ownership=False, is_const=True)], custom_name='NumProperties')
#################### smlItemUnref
# Return type: void (void_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemUnref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemUnref', 'void', [param('SmlItem *', 'item', transfer_ownership=False)], custom_name='Unref')
#################### smlLocationClone
# Return type: SmlLocation * (pointer_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlLocationClone
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLocation'].add_function_as_method('smlLocationClone', 'SmlLocation *', [param('SmlLocation *', 'source', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='Clone')
#################### smlManagerRun
# Return type: void (void_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerRun
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerRun', 'void', [param('SmlManager *', 'manager', transfer_ownership=False)], custom_name='Run')
#################### smlDevInfCTCapGetNthProperty
# Return type: SmlDevInfProperty const * (pointer_t)
# First Param is Pointer:  SmlDevInfCTCap const
# First Param is Const:  SmlDevInfCTCap
# First Param is declarated:  SmlDevInfCTCap [typedef]
#	class name: SmlDevInfCTCap 
#	prefix: smlDevInfCTCap 
#	python class name: DevInfCTCap 
#	pygccxmldefinition name:smlDevInfCTCapGetNthProperty
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfCTCap'].add_function_as_method('smlDevInfCTCapGetNthProperty', retval('SmlDevInfProperty *', is_const=True, caller_owns_return=False), [param('SmlDevInfCTCap *', 'ctcap', transfer_ownership=False, is_const=True), param('unsigned int', 'n')], custom_name='GetNthProperty')
#################### smlManagerDispatchChildCommand
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerDispatchChildCommand
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerDispatchChildCommand', 'SmlBool', [param('SmlManager *', 'manager', transfer_ownership=False), param('SmlSession *', 'session', transfer_ownership=False), param('SmlCommand *', 'parent', transfer_ownership=False), param('SmlCommand *', 'cmd', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='DispatchChildCommand')
#################### smlChalRef
# Return type: void (void_t)
# First Param is Pointer:  SmlChal
# First Param is declarated:  SmlChal [typedef]
#	class name: SmlChal 
#	prefix: smlChal 
#	python class name: Chal 
#	pygccxmldefinition name:smlChalRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlChal'].add_function_as_method('smlChalRef', 'void', [param('SmlChal *', 'chal', transfer_ownership=False)], custom_name='Ref')
#################### smlChalNew
# Return type: SmlChal * (pointer_t)
# First Param is declarated:  SmlAuthType [enumeration]
# First Param is Not Typedef:  SmlAuthType [enumeration]
# ADD_FUNCTION
    module.add_function('smlChalNew', 
                        'SmlChal *', 
                        [param('SmlAuthType', 'type'), param('SmlError * *', 'error')])
#################### smlCredUnref
# Return type: void (void_t)
# First Param is Pointer:  SmlCred
# First Param is declarated:  SmlCred [typedef]
#	class name: SmlCred 
#	prefix: smlCred 
#	python class name: Cred 
#	pygccxmldefinition name:smlCredUnref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlCred'].add_function_as_method('smlCredUnref', 'void', [param('SmlCred *', 'cred', transfer_ownership=False)], custom_name='Unref')
#################### smlSessionSetSendingMaxMsgSize
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionSetSendingMaxMsgSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionSetSendingMaxMsgSize', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('unsigned int', 'size')], custom_name='SetSendingMaxMsgSize')
#################### smlManagerQuit
# Return type: void (void_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerQuit
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerQuit', 'void', [param('SmlManager *', 'manager', transfer_ownership=False)], custom_name='Quit')
#################### smlNotificationGetIdentifier
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationGetIdentifier
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationGetIdentifier', retval('char *', is_const=True, caller_owns_return=False), [param('SmlNotification *', 'san', transfer_ownership=False)], custom_name='GetIdentifier')
#################### smlDevInfSetModel
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetModel
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetModel', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('char *', 'model', transfer_ownership=False, is_const=True)], custom_name='SetModel')
#################### smlDevInfGetDeviceType
# Return type: SmlDevInfDevTyp (declarated_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetDeviceType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetDeviceType', 'SmlDevInfDevTyp', [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='GetDeviceType')
#################### smlDevInfDataStoreSetSourceRef
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreSetSourceRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreSetSourceRef', 'void', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False), param('char *', 'sourceref', transfer_ownership=False, is_const=True)], custom_name='SetSourceRef')
#################### smlSessionGetSessionID
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionGetSessionID
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionGetSessionID', retval('char *', is_const=True, caller_owns_return=False), [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='GetSessionID')
#################### smlDevInfDevTypeToString
# Return type: char const * (pointer_t)
# First Param is declarated:  SmlDevInfDevTyp [enumeration]
# First Param is Not Typedef:  SmlDevInfDevTyp [enumeration]
# ADD_FUNCTION
    module.add_function('smlDevInfDevTypeToString', 
                        retval('char *', is_const=True, caller_owns_return=False), 
                        [param('SmlDevInfDevTyp', 'type'), param('SmlError * *', 'error')])
#################### smlDevInfNumDataStores
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfNumDataStores
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfNumDataStores', 'unsigned int', [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='NumDataStores')
#################### smlManagerGetTransport
# Return type: SmlTransport * (pointer_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerGetTransport
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerGetTransport', 'SmlTransport *', [param('SmlManager *', 'manager', transfer_ownership=False)], custom_name='GetTransport')
#################### smlManagerRegisterHeaderHandler
# Return type: void (void_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerRegisterHeaderHandler
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerRegisterHeaderHandler', 'void', [param('SmlManager *', 'manager', transfer_ownership=False), param('SmlHeaderCb *', 'callback'), param('SmlStatusReplyCb *', 'statuscb'), param('void *', 'userdata')], custom_name='RegisterHeaderHandler')
#################### smlItemSetSource
# Return type: void (void_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemSetSource
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemSetSource', 'void', [param('SmlItem *', 'item', transfer_ownership=False), param('SmlLocation *', 'source', transfer_ownership=False)], custom_name='SetSource')
#################### smlSessionGetReceivingMaxObjSize
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionGetReceivingMaxObjSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionGetReceivingMaxObjSize', 'unsigned int', [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='GetReceivingMaxObjSize')
#################### smlNotificationFreeAlert
# Return type: void (void_t)
# First Param is Pointer:  SmlSanAlert
# First Param is declarated:  SmlSanAlert [typedef]
#	class name: SmlSanAlert 
#	prefix: smlSanAlert 
#	python class name: SanAlert 
#	pygccxmldefinition name:smlNotificationFreeAlert
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlNotificationFreeAlert', 
                        'void', 
                        [param('SmlSanAlert *', 'alert', transfer_ownership=False)])
#	CONSTRUCTOR
    root_module['SmlItem'].add_function_as_constructor('smlItemNew', retval('SmlItem *', caller_owns_return=True), [param('unsigned int', 'size'), param('SmlError * *', 'error')])
#################### smlNotificationGetMode
# Return type: SmlNotificationUIMode (declarated_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationGetMode
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationGetMode', 'SmlNotificationUIMode', [param('SmlNotification *', 'san', transfer_ownership=False)], custom_name='GetMode')
#################### smlSessionDispatchEvent
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionDispatchEvent
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionDispatchEvent', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlSessionEventType', 'type'), param('SmlCommand *', 'cmd', transfer_ownership=False), param('SmlCommand *', 'parent', transfer_ownership=False), param('SmlStatus *', 'headerreply', transfer_ownership=False), param('SmlError *', 'error')], custom_name='DispatchEvent')
#################### smlDevInfGetCTCap
# Return type: SmlDevInfCTCap const * (pointer_t)
# First Param is Pointer:  SmlDevInf const
# First Param is Const:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetCTCap
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetCTCap', retval('SmlDevInfCTCap *', is_const=True, caller_owns_return=False), [param('SmlDevInf *', 'devinf', transfer_ownership=False, is_const=True), param('SmlDevInfContentType *', 'ct', transfer_ownership=False)], custom_name='GetCTCap')
#################### smlSessionUseOnlyReplace
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionUseOnlyReplace
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionUseOnlyReplace', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlBool', 'onlyReplace')], custom_name='UseOnlyReplace')
#################### smlBase64EncodeBinary
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlBase64EncodeBinary', 
                        'SmlBool', 
                        [param('char *', 'input', transfer_ownership=False, is_const=True), param('unsigned int', 'size'), param('char * *', 'output'), param('SmlError * *', 'error')])
#################### smlDevInfPropertySetMaxSize
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertySetMaxSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertySetMaxSize', 'void', [param('SmlDevInfProperty *', 'property', transfer_ownership=False), param('unsigned int', 'maxSize')], custom_name='SetMaxSize')
#################### smlDevInfDataStoreSetTxPref
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreSetTxPref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreSetTxPref', 'void', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False), param('char *', 'contenttype', transfer_ownership=False, is_const=True), param('char *', 'version', transfer_ownership=False, is_const=True)], custom_name='SetTxPref')
#################### smlDevInfAssemble
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfAssemble
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfAssemble', 'SmlBool', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('char * *', 'data'), param('unsigned int *', 'size'), param('SmlError * *', 'error')], custom_name='Assemble')
#################### smlDevInfFreeContentType
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfContentType
# First Param is declarated:  SmlDevInfContentType [typedef]
#	class name: SmlDevInfContentType 
#	prefix: smlDevInfContentType 
#	python class name: DevInfContentType 
#	pygccxmldefinition name:smlDevInfFreeContentType
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlDevInfFreeContentType', 
                        'void', 
                        [param('SmlDevInfContentType *', 'ct', transfer_ownership=False)])
#################### smlDevInfSetSupportsLargeObjs
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetSupportsLargeObjs
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetSupportsLargeObjs', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('SmlBool', 'supports')], custom_name='SetSupportsLargeObjs')
#################### smlItemSetTarget
# Return type: void (void_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemSetTarget
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemSetTarget', 'void', [param('SmlItem *', 'item', transfer_ownership=False), param('SmlLocation *', 'target', transfer_ownership=False)], custom_name='SetTarget')
#################### smlDevInfConfigureSession
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfConfigureSession
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfConfigureSession', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('SmlSession *', 'session', transfer_ownership=False)], custom_name='ConfigureSession')
#	CONSTRUCTOR
    root_module['SmlLink'].add_function_as_constructor('smlLinkNew', retval('SmlLink *', caller_owns_return=True), [param('SmlTransport *', 'tsp', transfer_ownership=False), param('void *', 'link_data'), param('SmlError * *', 'error')])
#################### smlTransportConnect
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportConnect
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportConnect', 'SmlBool', [param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='Connect')
#################### smlDevInfPropertyGetDisplayName
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfProperty const
# First Param is Const:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyGetDisplayName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyGetDisplayName', 'char *', [param('SmlDevInfProperty *', 'property', transfer_ownership=False, is_const=True)], custom_name='GetDisplayName')
#################### smlCommandNewGet
# Return type: SmlCommand * (pointer_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlCommandNewGet
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlCommandNewGet', 
                        retval('SmlCommand *', caller_owns_return=True), 
                        [param('SmlLocation *', 'target', transfer_ownership=False), param('char *', 'contenttype', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlSessionSetSendingMaxObjSize
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionSetSendingMaxObjSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionSetSendingMaxObjSize', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('int', 'limit')], custom_name='SetSendingMaxObjSize')
#################### smlTransportDataDeref
# Return type: void (void_t)
# First Param is Pointer:  SmlTransportData
# First Param is declarated:  SmlTransportData [typedef]
#	class name: SmlTransportData 
#	prefix: smlTransportData 
#	python class name: TransportData 
#	pygccxmldefinition name:smlTransportDataDeref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransportData'].add_function_as_method('smlTransportDataDeref', 'void', [param('SmlTransportData *', 'data', transfer_ownership=False)], custom_name='Deref')
#################### smlSessionFlush
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionFlush
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionFlush', 'SmlBool', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlBool', 'final'), param('SmlError * *', 'error')], custom_name='Flush')
#################### smlDevInfDataStoreGetSourceRef
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreGetSourceRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreGetSourceRef', retval('char *', is_const=True, caller_owns_return=False), [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True)], custom_name='GetSourceRef')
#################### smlDevInfPropParamGetDataType
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfPropParam const
# First Param is Const:  SmlDevInfPropParam
# First Param is declarated:  SmlDevInfPropParam [typedef]
#	class name: SmlDevInfPropParam 
#	prefix: smlDevInfPropParam 
#	python class name: DevInfPropParam 
#	pygccxmldefinition name:smlDevInfPropParamGetDataType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfPropParam'].add_function_as_method('smlDevInfPropParamGetDataType', 'char *', [param('SmlDevInfPropParam *', 'propParam', transfer_ownership=False, is_const=True)], custom_name='GetDataType')
#################### smlTransportSetConnectionType
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportSetConnectionType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportSetConnectionType', 'SmlBool', [param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlTransportConnectionType', 'type'), param('SmlError * *', 'error')], custom_name='SetConnectionType')
#################### smlDevInfDataStoreGetTxPref
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreGetTxPref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreGetTxPref', 'SmlBool', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True), param('char * *', 'contenttype'), param('char * *', 'version')], custom_name='GetTxPref')
#################### smlDevInfGetDeviceID
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetDeviceID
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetDeviceID', retval('char *', is_const=True, caller_owns_return=False), [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='GetDeviceID')
#################### smlMapItemUnref
# Return type: void (void_t)
# First Param is Pointer:  SmlMapItem
# First Param is declarated:  SmlMapItem [typedef]
#	class name: SmlMapItem 
#	prefix: smlMapItem 
#	python class name: MapItem 
#	pygccxmldefinition name:smlMapItemUnref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlMapItem'].add_function_as_method('smlMapItemUnref', 'void', [param('SmlMapItem *', 'item', transfer_ownership=False)], custom_name='Unref')
#################### smlDevInfSetSoftwareVersion
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetSoftwareVersion
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetSoftwareVersion', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('char *', 'softwareVersion', transfer_ownership=False, is_const=True)], custom_name='SetSoftwareVersion')
#################### smlLocationUnref
# Return type: void (void_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlLocationUnref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLocation'].add_function_as_method('smlLocationUnref', 'void', [param('SmlLocation *', 'loc', transfer_ownership=False)], custom_name='Unref')
#################### smlItemGetTarget
# Return type: SmlLocation * (pointer_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemGetTarget
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemGetTarget', 'SmlLocation *', [param('SmlItem *', 'item', transfer_ownership=False)], custom_name='GetTarget')
#################### smlDevInfAppendCTCap
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfAppendCTCap
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfAppendCTCap', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('SmlDevInfCTCap *', 'ctcap', transfer_ownership=False)], custom_name='AppendCTCap')
#################### smlDevInfPropertyGetNthValEnum
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfProperty const
# First Param is Const:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyGetNthValEnum
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyGetNthValEnum', 'char *', [param('SmlDevInfProperty *', 'property', transfer_ownership=False, is_const=True), param('unsigned int', 'n')], custom_name='GetNthValEnum')
#	CONSTRUCTOR
    root_module['SmlMapItem'].add_function_as_constructor('smlMapItemNew', retval('SmlMapItem *', caller_owns_return=True), [param('char *', 'uid', transfer_ownership=False, is_const=True), param('char *', 'newuid', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlDevInfNewGet
# Return type: SmlCommand * (pointer_t)
# First Param is declarated:  SmlDevInfVersion [enumeration]
# First Param is Not Typedef:  SmlDevInfVersion [enumeration]
# ADD_FUNCTION
    module.add_function('smlDevInfNewGet', 
                        'SmlCommand *', 
                        [param('SmlDevInfVersion', 'version'), param('SmlError * *', 'error')])
#################### smlSessionReceiveBody
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionReceiveBody
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionReceiveBody', 'SmlBool', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlParser *', 'parser'), param('SmlError * *', 'error')], custom_name='ReceiveBody')
#################### smlDevInfNewResult
# Return type: SmlCommand * (pointer_t)
# First Param is Pointer:  SmlCommand
# First Param is declarated:  SmlCommand [typedef]
#	class name: SmlCommand 
#	prefix: smlCommand 
#	python class name: Command 
#	pygccxmldefinition name:smlDevInfNewResult
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlDevInfNewResult', 
                        'SmlCommand *', 
                        [param('SmlCommand *', 'cmd', transfer_ownership=False), param('SmlDevInf *', 'devinf', transfer_ownership=False), param('SmlDevInfVersion', 'version'), param('SmlError * *', 'error')])
#################### smlSessionSetReceivingMaxMsgSize
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionSetReceivingMaxMsgSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionSetReceivingMaxMsgSize', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('unsigned int', 'size')], custom_name='SetReceivingMaxMsgSize')
#	CONSTRUCTOR
    root_module['SmlDevInfAgent'].add_function_as_constructor('smlDevInfAgentNew', retval('SmlDevInfAgent *', caller_owns_return=True), [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('SmlError * *', 'error')])
#################### smlDevInfPropertySetNoTruncate
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertySetNoTruncate
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertySetNoTruncate', 'void', [param('SmlDevInfProperty *', 'property', transfer_ownership=False)], custom_name='SetNoTruncate')
#################### smlDevInfSetFirmwareVersion
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetFirmwareVersion
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetFirmwareVersion', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('char *', 'firmwareVersion', transfer_ownership=False, is_const=True)], custom_name='SetFirmwareVersion')
#################### HACKFree
# Return type: void (void_t)
# First Param is Pointer:  void
# First Param is Not Typedef:  void
# ADD_FUNCTION
    module.add_function('HACKFree', 
                        'void', 
                        [param('void *', 'foo')])
#################### smlLinkRef
# Return type: SmlLink * (pointer_t)
# First Param is Pointer:  SmlLink
# First Param is declarated:  SmlLink [typedef]
#	class name: SmlLink 
#	prefix: smlLink 
#	python class name: Link 
#	pygccxmldefinition name:smlLinkRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLink'].add_function_as_method('smlLinkRef', 'SmlLink *', [param('SmlLink *', 'link', transfer_ownership=False)], custom_name='Ref')
#################### smlNotificationSetCred
# Return type: void (void_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationSetCred
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationSetCred', 'void', [param('SmlNotification *', 'san', transfer_ownership=False), param('SmlCred *', 'cred', transfer_ownership=False)], custom_name='SetCred')
#################### smlSessionGetSource
# Return type: SmlLocation * (pointer_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionGetSource
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionGetSource', 'SmlLocation *', [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='GetSource')
#################### smlManagerSetEventCallback
# Return type: void (void_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerSetEventCallback
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerSetEventCallback', 'void', [param('SmlManager *', 'manager', transfer_ownership=False), param('SmlManagerEventCb *', 'callback'), param('void *', 'userdata')], custom_name='SetEventCallback')
#################### smlManagerDispatchCommand
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerDispatchCommand
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerDispatchCommand', 'SmlBool', [param('SmlManager *', 'manager', transfer_ownership=False), param('SmlSession *', 'session', transfer_ownership=False), param('SmlCommand *', 'cmd', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='DispatchCommand')
#################### smlDevInfDataStoreRef
# Return type: SmlDevInfDataStore * (pointer_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreRef', 'SmlDevInfDataStore *', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False)], custom_name='Ref')
#################### smlManagerObjectFind
# Return type: SmlObject * (pointer_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerObjectFind
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerObjectFind', 'SmlObject *', [param('SmlManager *', 'manager', transfer_ownership=False), param('SmlSession *', 'session', transfer_ownership=False), param('SmlCommand *', 'cmd', transfer_ownership=False)], custom_name='ObjectFind')
#################### smlLocationGetURI
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlLocationGetURI
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLocation'].add_function_as_method('smlLocationGetURI', retval('char *', is_const=True, caller_owns_return=False), [param('SmlLocation *', 'loc', transfer_ownership=False)], custom_name='GetURI')
#################### smlSessionUseLargeObjects
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionUseLargeObjects
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionUseLargeObjects', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlBool', 'support')], custom_name='UseLargeObjects')
#################### smlDevInfPropParamGetNthValEnum
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfPropParam const
# First Param is Const:  SmlDevInfPropParam
# First Param is declarated:  SmlDevInfPropParam [typedef]
#	class name: SmlDevInfPropParam 
#	prefix: smlDevInfPropParam 
#	python class name: DevInfPropParam 
#	pygccxmldefinition name:smlDevInfPropParamGetNthValEnum
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfPropParam'].add_function_as_method('smlDevInfPropParamGetNthValEnum', 'char *', [param('SmlDevInfPropParam *', 'propParam', transfer_ownership=False, is_const=True), param('unsigned int', 'n')], custom_name='GetNthValEnum')
#################### smlManagerFree
# Return type: void (void_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerFree
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerFree', 'void', [param('SmlManager *', 'manager', transfer_ownership=False)], custom_name='Free')
#################### smlManagerSessionRemove
# Return type: void (void_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerSessionRemove
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerSessionRemove', 'void', [param('SmlManager *', 'manager', transfer_ownership=False), param('SmlSession *', 'session', transfer_ownership=False)], custom_name='SessionRemove')
#################### smlSessionGetTarget
# Return type: SmlLocation * (pointer_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionGetTarget
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionGetTarget', 'SmlLocation *', [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='GetTarget')
#	CONSTRUCTOR
    root_module['SmlTransport'].add_function_as_constructor('smlTransportNew', retval('SmlTransport *', caller_owns_return=True), [param('SmlTransportType', 'type'), param('SmlError * *', 'error')])
#	CONSTRUCTOR
    root_module['SmlDevInfCTCap'].add_function_as_constructor('smlDevInfNewCTCap', retval('SmlDevInfCTCap *', caller_owns_return=True), [param('SmlError * *', 'error')])
#################### smlDevInfParse
# Return type: SmlDevInf * (pointer_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlDevInfParse', 
                        'SmlDevInf *', 
                        [param('char *', 'data', transfer_ownership=False, is_const=True), param('unsigned int', 'length'), param('SmlError * *', 'error')])
#################### smlDevInfSetSupportsNumberOfChanges
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetSupportsNumberOfChanges
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetSupportsNumberOfChanges', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('SmlBool', 'supports')], custom_name='SetSupportsNumberOfChanges')
#################### smlBase64DecodeBinary
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlBase64DecodeBinary', 
                        'SmlBool', 
                        [param('char *', 'input', transfer_ownership=False, is_const=True), param('unsigned int', 'size'), param('char * *', 'output'), param('unsigned int *', 'outsize'), param('SmlError * *', 'error')])
#################### smlSessionGetSendingMaxMsgSize
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionGetSendingMaxMsgSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionGetSendingMaxMsgSize', 'unsigned int', [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='GetSendingMaxMsgSize')
#################### smlCommandUnref
# Return type: void (void_t)
# First Param is Pointer:  SmlCommand
# First Param is declarated:  SmlCommand [typedef]
#	class name: SmlCommand 
#	prefix: smlCommand 
#	python class name: Command 
#	pygccxmldefinition name:smlCommandUnref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlCommand'].add_function_as_method('smlCommandUnref', 'void', [param('SmlCommand *', 'cmd', transfer_ownership=False)], custom_name='Unref')
#################### smlMapItemRef
# Return type: SmlMapItem * (pointer_t)
# First Param is Pointer:  SmlMapItem
# First Param is declarated:  SmlMapItem [typedef]
#	class name: SmlMapItem 
#	prefix: smlMapItem 
#	python class name: MapItem 
#	pygccxmldefinition name:smlMapItemRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlMapItem'].add_function_as_method('smlMapItemRef', 'SmlMapItem *', [param('SmlMapItem *', 'item', transfer_ownership=False)], custom_name='Ref')
#################### smlSanAlertGetServerURI
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlSanAlert
# First Param is declarated:  SmlSanAlert [typedef]
#	class name: SmlSanAlert 
#	prefix: smlSanAlert 
#	python class name: SanAlert 
#	pygccxmldefinition name:smlSanAlertGetServerURI
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSanAlert'].add_function_as_method('smlSanAlertGetServerURI', retval('char *', is_const=True, caller_owns_return=False), [param('SmlSanAlert *', 'alert', transfer_ownership=False)], custom_name='GetServerURI')
#################### smlAuthSetVerifyCallback
# Return type: void (void_t)
# First Param is Pointer:  SmlAuthenticator
# First Param is declarated:  SmlAuthenticator [typedef]
#	class name: SmlAuthenticator 
#	prefix: smlAuthenticator 
#	python class name: Authenticator 
#	pygccxmldefinition name:smlAuthSetVerifyCallback
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlAuthSetVerifyCallback', 
                        'void', 
                        [param('SmlAuthenticator *', 'auth', transfer_ownership=False), param('SmlAuthVerifyCb *', 'callback'), param('void *', 'userdata')])
#################### smlDevInfAgentSetDevInf
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfAgent
# First Param is declarated:  SmlDevInfAgent [typedef]
#	class name: SmlDevInfAgent 
#	prefix: smlDevInfAgent 
#	python class name: DevInfAgent 
#	pygccxmldefinition name:smlDevInfAgentSetDevInf
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfAgent'].add_function_as_method('smlDevInfAgentSetDevInf', 'void', [param('SmlDevInfAgent *', 'agent', transfer_ownership=False), param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='SetDevInf')
#################### smlDevInfDataStoreNumRx
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreNumRx
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreNumRx', 'unsigned int', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True)], custom_name='NumRx')
#################### smlManagerDispatch
# Return type: void (void_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerDispatch
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerDispatch', 'void', [param('SmlManager *', 'manager', transfer_ownership=False)], custom_name='Dispatch')
#################### smlDevInfGetSoftwareVersion
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetSoftwareVersion
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetSoftwareVersion', retval('char *', is_const=True, caller_owns_return=False), [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='GetSoftwareVersion')
#################### smlStatusGetClass
# Return type: SmlErrorClass (declarated_t)
# First Param is Pointer:  SmlStatus
# First Param is declarated:  SmlStatus [typedef]
#	class name: SmlStatus 
#	prefix: smlStatus 
#	python class name: Status 
#	pygccxmldefinition name:smlStatusGetClass
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlStatus'].add_function_as_method('smlStatusGetClass', 'SmlErrorClass', [param('SmlStatus *', 'status', transfer_ownership=False)], custom_name='GetClass')
#################### smlDevInfSetMaxGUIDSize
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfSetMaxGUIDSize
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlDevInfSetMaxGUIDSize', 
                        'void', 
                        [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False), param('unsigned int', 'max')])
#################### smlDevInfDataStoreNumTx
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreNumTx
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreNumTx', 'unsigned int', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True)], custom_name='NumTx')
#################### smlDevInfDataStoreGetDisplayName
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreGetDisplayName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreGetDisplayName', retval('char *', is_const=True, caller_owns_return=False), [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True)], custom_name='GetDisplayName')
#################### smlDevInfPropertySetPropName
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertySetPropName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertySetPropName', 'void', [param('SmlDevInfProperty *', 'property', transfer_ownership=False), param('char *', 'propName', transfer_ownership=False, is_const=True)], custom_name='SetPropName')
#################### smlDevInfGetFirmwareVersion
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetFirmwareVersion
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetFirmwareVersion', retval('char *', is_const=True, caller_owns_return=False), [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='GetFirmwareVersion')
#################### smlTransportFree
# Return type: void (void_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportFree
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportFree', 'void', [param('SmlTransport *', 'tsp', transfer_ownership=False)], custom_name='Free')
#################### smlSessionSetEventCallback
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionSetEventCallback
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionSetEventCallback', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlSessionEventCallback *', 'callback'), param('void *', 'userdata')], custom_name='SetEventCallback')
#	CONSTRUCTOR
    root_module['SmlAnchor'].add_function_as_constructor('smlAnchorNew', retval('SmlAnchor *', caller_owns_return=True), [param('char *', 'last', transfer_ownership=False, is_const=True), param('char *', 'next', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlDevInfSetHardwareVersion
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetHardwareVersion
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetHardwareVersion', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('char *', 'hardwareVersion', transfer_ownership=False, is_const=True)], custom_name='SetHardwareVersion')
#	CONSTRUCTOR
    root_module['SmlCommand'].add_function_as_constructor('smlCommandNew', retval('SmlCommand *', caller_owns_return=True), [param('SmlCommandType', 'type'), param('SmlError * *', 'error')])
#################### smlStatusRef
# Return type: SmlStatus * (pointer_t)
# First Param is Pointer:  SmlStatus
# First Param is declarated:  SmlStatus [typedef]
#	class name: SmlStatus 
#	prefix: smlStatus 
#	python class name: Status 
#	pygccxmldefinition name:smlStatusRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlStatus'].add_function_as_method('smlStatusRef', 'SmlStatus *', [param('SmlStatus *', 'status', transfer_ownership=False)], custom_name='Ref')
#################### smlDevInfPropertyGetNthPropParam
# Return type: SmlDevInfPropParam const * (pointer_t)
# First Param is Pointer:  SmlDevInfProperty const
# First Param is Const:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyGetNthPropParam
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyGetNthPropParam', retval('SmlDevInfPropParam *', is_const=True, caller_owns_return=False), [param('SmlDevInfProperty *', 'property', transfer_ownership=False, is_const=True), param('unsigned int', 'n')], custom_name='GetNthPropParam')
#################### smlSessionGetVersion
# Return type: SmlProtocolVersion (declarated_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionGetVersion
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionGetVersion', 'SmlProtocolVersion', [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='GetVersion')
#################### smlTransportFinalize
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportFinalize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportFinalize', 'SmlBool', [param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='Finalize')
#################### smlCommandNewChange
# Return type: SmlCommand * (pointer_t)
# First Param is declarated:  SmlChangeType [enumeration]
# First Param is Not Typedef:  SmlChangeType [enumeration]
# ADD_FUNCTION
    module.add_function('smlCommandNewChange', 
                        retval('SmlCommand *', caller_owns_return=True), 
                        [param('SmlChangeType', 'type'), param('char *', 'uid', transfer_ownership=False, is_const=True), param('char *', 'data', transfer_ownership=False, is_const=True), param('unsigned int', 'size'), param('char *', 'contenttype', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlHeaderFree
# Return type: void (void_t)
# First Param is Pointer:  SmlHeader
# First Param is declarated:  SmlHeader [typedef]
#	class name: SmlHeader 
#	prefix: smlHeader 
#	python class name: Header 
#	pygccxmldefinition name:smlHeaderFree
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlHeader'].add_function_as_method('smlHeaderFree', 'void', [param('SmlHeader *', 'header', transfer_ownership=False)], custom_name='Free')
#################### smlSessionUseNumberOfChanges
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionUseNumberOfChanges
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionUseNumberOfChanges', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlBool', 'support')], custom_name='UseNumberOfChanges')
#################### smlLocationCompare
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlLocationCompare
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLocation'].add_function_as_method('smlLocationCompare', 'SmlBool', [param('SmlLocation *', 'objectroot', transfer_ownership=False), param('SmlLocation *', 'object', transfer_ownership=False), param('SmlLocation *', 'urlroot', transfer_ownership=False), param('SmlLocation *', 'url', transfer_ownership=False)], custom_name='Compare')
#################### smlNotificationParse
# Return type: SmlNotification * (pointer_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlNotificationParse', 
                        'SmlNotification *', 
                        [param('char *', 'data', transfer_ownership=False, is_const=True), param('unsigned int', 'size'), param('SmlError * *', 'error')])
#################### smlManagerSessionFind
# Return type: SmlSession * (pointer_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerSessionFind
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerSessionFind', 'SmlSession *', [param('SmlManager *', 'manager', transfer_ownership=False), param('char *', 'sessionID', transfer_ownership=False, is_const=True)], custom_name='SessionFind')
#################### smlManagerSessionAdd
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerSessionAdd
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerSessionAdd', 'SmlBool', [param('SmlManager *', 'manager', transfer_ownership=False), param('SmlSession *', 'session', transfer_ownership=False), param('SmlLink *', 'link', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='SessionAdd')
#################### smlDevInfCTCapGetCTType
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfCTCap const
# First Param is Const:  SmlDevInfCTCap
# First Param is declarated:  SmlDevInfCTCap [typedef]
#	class name: SmlDevInfCTCap 
#	prefix: smlDevInfCTCap 
#	python class name: DevInfCTCap 
#	pygccxmldefinition name:smlDevInfCTCapGetCTType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfCTCap'].add_function_as_method('smlDevInfCTCapGetCTType', 'char *', [param('SmlDevInfCTCap *', 'ctcap', transfer_ownership=False, is_const=True)], custom_name='GetCTType')
#################### smlSanAlertGetContentType
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlSanAlert
# First Param is declarated:  SmlSanAlert [typedef]
#	class name: SmlSanAlert 
#	prefix: smlSanAlert 
#	python class name: SanAlert 
#	pygccxmldefinition name:smlSanAlertGetContentType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSanAlert'].add_function_as_method('smlSanAlertGetContentType', retval('char *', is_const=True, caller_owns_return=False), [param('SmlSanAlert *', 'alert', transfer_ownership=False)], custom_name='GetContentType')
#################### smlDevInfCTCapSetCTType
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfCTCap
# First Param is declarated:  SmlDevInfCTCap [typedef]
#	class name: SmlDevInfCTCap 
#	prefix: smlDevInfCTCap 
#	python class name: DevInfCTCap 
#	pygccxmldefinition name:smlDevInfCTCapSetCTType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfCTCap'].add_function_as_method('smlDevInfCTCapSetCTType', 'void', [param('SmlDevInfCTCap *', 'ctcap', transfer_ownership=False), param('char *', 'cttype', transfer_ownership=False, is_const=True)], custom_name='SetCTType')
#################### smlDevInfAgentRegister
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInfAgent
# First Param is declarated:  SmlDevInfAgent [typedef]
#	class name: SmlDevInfAgent 
#	prefix: smlDevInfAgent 
#	python class name: DevInfAgent 
#	pygccxmldefinition name:smlDevInfAgentRegister
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfAgent'].add_function_as_method('smlDevInfAgentRegister', 'SmlBool', [param('SmlDevInfAgent *', 'agent', transfer_ownership=False), param('SmlManager *', 'manager', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='Register')
#################### smlDevInfPropParamSetParamName
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfPropParam
# First Param is declarated:  SmlDevInfPropParam [typedef]
#	class name: SmlDevInfPropParam 
#	prefix: smlDevInfPropParam 
#	python class name: DevInfPropParam 
#	pygccxmldefinition name:smlDevInfPropParamSetParamName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfPropParam'].add_function_as_method('smlDevInfPropParamSetParamName', 'void', [param('SmlDevInfPropParam *', 'propParam', transfer_ownership=False), param('char *', 'paramName', transfer_ownership=False, is_const=True)], custom_name='SetParamName')
#	CONSTRUCTOR
    root_module['SmlAuthenticator'].add_function_as_constructor('smlAuthNew', retval('SmlAuthenticator *', caller_owns_return=True), [param('SmlError * *', 'error')])
#################### smlAuthRegister
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlAuthenticator
# First Param is declarated:  SmlAuthenticator [typedef]
#	class name: SmlAuthenticator 
#	prefix: smlAuthenticator 
#	python class name: Authenticator 
#	pygccxmldefinition name:smlAuthRegister
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlAuthRegister', 
                        'SmlBool', 
                        [param('SmlAuthenticator *', 'auth', transfer_ownership=False), param('SmlManager *', 'manager', transfer_ownership=False), param('SmlError * *', 'error')])
#################### smlCommandNewResult
# Return type: SmlCommand * (pointer_t)
# First Param is Pointer:  SmlCommand
# First Param is declarated:  SmlCommand [typedef]
#	class name: SmlCommand 
#	prefix: smlCommand 
#	python class name: Command 
#	pygccxmldefinition name:smlCommandNewResult
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlCommand'].add_function_as_method('smlCommandNewResult', 'SmlCommand *', [param('SmlCommand *', 'cmd', transfer_ownership=False), param('SmlLocation *', 'source', transfer_ownership=False), param('char *', 'data'), param('unsigned int', 'size'), param('char *', 'contenttype', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')], custom_name='NewResult')
#################### smlSessionGetSendingMaxObjSize
# Return type: int (int_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionGetSendingMaxObjSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionGetSendingMaxObjSize', 'int', [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='GetSendingMaxObjSize')
#################### smlDevInfRef
# Return type: SmlDevInf * (pointer_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfRef', 'SmlDevInf *', [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='Ref')
#################### smlStatusGetResult
# Return type: SmlCommand * (pointer_t)
# First Param is Pointer:  SmlStatus
# First Param is declarated:  SmlStatus [typedef]
#	class name: SmlStatus 
#	prefix: smlStatus 
#	python class name: Status 
#	pygccxmldefinition name:smlStatusGetResult
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlStatus'].add_function_as_method('smlStatusGetResult', 'SmlCommand *', [param('SmlStatus *', 'status', transfer_ownership=False)], custom_name='GetResult')
#################### smlCommandAddMapItem
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlCommand
# First Param is declarated:  SmlCommand [typedef]
#	class name: SmlCommand 
#	prefix: smlCommand 
#	python class name: Command 
#	pygccxmldefinition name:smlCommandAddMapItem
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlCommand'].add_function_as_method('smlCommandAddMapItem', 'SmlBool', [param('SmlCommand *', 'map', transfer_ownership=False), param('SmlMapItem *', 'item', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='AddMapItem')
#################### smlDevInfPropertyAddValEnum
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyAddValEnum
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyAddValEnum', 'void', [param('SmlDevInfProperty *', 'property', transfer_ownership=False), param('char *', 'valEnum', transfer_ownership=False, is_const=True)], custom_name='AddValEnum')
#	CONSTRUCTOR
    root_module['SmlDevInfProperty'].add_function_as_constructor('smlDevInfNewProperty', retval('SmlDevInfProperty *', caller_owns_return=True), [param('SmlError * *', 'error')])
#################### smlStatusUnref
# Return type: void (void_t)
# First Param is Pointer:  SmlStatus
# First Param is declarated:  SmlStatus [typedef]
#	class name: SmlStatus 
#	prefix: smlStatus 
#	python class name: Status 
#	pygccxmldefinition name:smlStatusUnref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlStatus'].add_function_as_method('smlStatusUnref', 'void', [param('SmlStatus *', 'status', transfer_ownership=False)], custom_name='Unref')
#################### smlTransportSend
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportSend
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportSend', 'SmlBool', [param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlLink *', 'link', transfer_ownership=False, null_ok=True), param('SmlTransportData *', 'data', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='Send')
#################### smlDevInfPropParamSetDisplayName
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfPropParam
# First Param is declarated:  SmlDevInfPropParam [typedef]
#	class name: SmlDevInfPropParam 
#	prefix: smlDevInfPropParam 
#	python class name: DevInfPropParam 
#	pygccxmldefinition name:smlDevInfPropParamSetDisplayName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfPropParam'].add_function_as_method('smlDevInfPropParamSetDisplayName', 'void', [param('SmlDevInfPropParam *', 'propParam', transfer_ownership=False), param('char *', 'displayName', transfer_ownership=False, is_const=True)], custom_name='SetDisplayName')
#################### smlItemStealData
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemStealData
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemStealData', 'SmlBool', [param('SmlItem *', 'item', transfer_ownership=False), param('char * *', 'data'), param('unsigned int *', 'size'), param('SmlError * *', 'error')], custom_name='StealData')
#################### smlDevInfSetDeviceType
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetDeviceType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetDeviceType', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('SmlDevInfDevTyp', 'devtyp')], custom_name='SetDeviceType')
#################### smlNotificationSetManager
# Return type: void (void_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationSetManager
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationSetManager', 'void', [param('SmlNotification *', 'san', transfer_ownership=False), param('SmlManager *', 'manager', transfer_ownership=False)], custom_name='SetManager')
#################### smlDevInfGetHardwareVersion
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetHardwareVersion
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetHardwareVersion', retval('char *', is_const=True, caller_owns_return=False), [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='GetHardwareVersion')
#################### smlAuthVerify
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlChal
# First Param is declarated:  SmlChal [typedef]
#	class name: SmlChal 
#	prefix: smlChal 
#	python class name: Chal 
#	pygccxmldefinition name:smlAuthVerify
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlAuthVerify', 
                        'SmlBool', 
                        [param('SmlChal *', 'chal', transfer_ownership=False), param('SmlCred *', 'cred', transfer_ownership=False), param('char *', 'username', transfer_ownership=False, is_const=True), param('char *', 'password', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlDevInfDataStoreGetMemory
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreGetMemory
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreGetMemory', 'void', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True), param('SmlBool *', 'shared'), param('unsigned int *', 'maxid'), param('unsigned int *', 'maxmem')], custom_name='GetMemory')
#################### smlAuthSetState
# Return type: void (void_t)
# First Param is Pointer:  SmlAuthenticator
# First Param is declarated:  SmlAuthenticator [typedef]
#	class name: SmlAuthenticator 
#	prefix: smlAuthenticator 
#	python class name: Authenticator 
#	pygccxmldefinition name:smlAuthSetState
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlAuthSetState', 
                        'void', 
                        [param('SmlAuthenticator *', 'auth', transfer_ownership=False), param('SmlErrorType', 'type')])
#################### smlSessionSetSessionID
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionSetSessionID
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionSetSessionID', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('char *', 'sessionID', transfer_ownership=False, is_const=True)], custom_name='SetSessionID')
#################### smlAuthIsEnabled
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlAuthenticator
# First Param is declarated:  SmlAuthenticator [typedef]
#	class name: SmlAuthenticator 
#	prefix: smlAuthenticator 
#	python class name: Authenticator 
#	pygccxmldefinition name:smlAuthIsEnabled
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlAuthIsEnabled', 
                        'SmlBool', 
                        [param('SmlAuthenticator *', 'auth', transfer_ownership=False)])
#################### smlDevInfDataStoreGetSyncCap
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreGetSyncCap
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreGetSyncCap', 'SmlBool', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True), param('SmlDevInfSyncCap', 'cap')], custom_name='GetSyncCap')
#################### smlLinkDeref
# Return type: void (void_t)
# First Param is Pointer:  SmlLink
# First Param is declarated:  SmlLink [typedef]
#	class name: SmlLink 
#	prefix: smlLink 
#	python class name: Link 
#	pygccxmldefinition name:smlLinkDeref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLink'].add_function_as_method('smlLinkDeref', 'void', [param('SmlLink *', 'link', transfer_ownership=False)], custom_name='Deref')
#################### smlSessionEnd
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionEnd
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionEnd', 'SmlBool', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='End')
#################### smlSessionCheck
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionCheck
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionCheck', 'SmlBool', [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='Check')
#################### smlDevInfAgentFree
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfAgent
# First Param is declarated:  SmlDevInfAgent [typedef]
#	class name: SmlDevInfAgent 
#	prefix: smlDevInfAgent 
#	python class name: DevInfAgent 
#	pygccxmldefinition name:smlDevInfAgentFree
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfAgent'].add_function_as_method('smlDevInfAgentFree', 'void', [param('SmlDevInfAgent *', 'agent', transfer_ownership=False)], custom_name='Free')
#################### smlDevInfPropParamGetParamName
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfPropParam const
# First Param is Const:  SmlDevInfPropParam
# First Param is declarated:  SmlDevInfPropParam [typedef]
#	class name: SmlDevInfPropParam 
#	prefix: smlDevInfPropParam 
#	python class name: DevInfPropParam 
#	pygccxmldefinition name:smlDevInfPropParamGetParamName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfPropParam'].add_function_as_method('smlDevInfPropParamGetParamName', 'char *', [param('SmlDevInfPropParam *', 'propParam', transfer_ownership=False, is_const=True)], custom_name='GetParamName')
#################### smlDevInfUnref
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfUnref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfUnref', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='Unref')
#################### smlManagerStop
# Return type: void (void_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerStop
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerStop', 'void', [param('SmlManager *', 'manager', transfer_ownership=False)], custom_name='Stop')
#################### smlDevInfGetOEM
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetOEM
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetOEM', retval('char *', is_const=True, caller_owns_return=False), [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='GetOEM')
#################### smlAuthSetEnable
# Return type: void (void_t)
# First Param is Pointer:  SmlAuthenticator
# First Param is declarated:  SmlAuthenticator [typedef]
#	class name: SmlAuthenticator 
#	prefix: smlAuthenticator 
#	python class name: Authenticator 
#	pygccxmldefinition name:smlAuthSetEnable
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlAuthSetEnable', 
                        'void', 
                        [param('SmlAuthenticator *', 'auth', transfer_ownership=False), param('SmlBool', 'enabled')])
#################### smlSessionSetDataCallback
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionSetDataCallback
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionSetDataCallback', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlSessionDataCallback *', 'callback'), param('void *', 'userdata')], custom_name='SetDataCallback')
#################### smlDevInfCTCapTypeToString
# Return type: char const * (pointer_t)
# First Param is declarated:  SmlDevInfCTCapType [enumeration]
# First Param is Not Typedef:  SmlDevInfCTCapType [enumeration]
# ADD_FUNCTION
    module.add_function('smlDevInfCTCapTypeToString', 
                        retval('char *', is_const=True, caller_owns_return=False), 
                        [param('SmlDevInfCTCapType', 'type'), param('SmlError * *', 'error')])
#################### smlSessionDispatch
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionDispatch
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionDispatch', 'void', [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='Dispatch')
#################### smlDevInfContentTypeGetVerCT
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfContentType const
# First Param is Const:  SmlDevInfContentType
# First Param is declarated:  SmlDevInfContentType [typedef]
#	class name: SmlDevInfContentType 
#	prefix: smlDevInfContentType 
#	python class name: DevInfContentType 
#	pygccxmldefinition name:smlDevInfContentTypeGetVerCT
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfContentType'].add_function_as_method('smlDevInfContentTypeGetVerCT', 'char *', [param('SmlDevInfContentType *', 'ct', transfer_ownership=False, is_const=True)], custom_name='GetVerCT')
#################### smlDevInfAgentSendDevInf
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInfAgent
# First Param is declarated:  SmlDevInfAgent [typedef]
#	class name: SmlDevInfAgent 
#	prefix: smlDevInfAgent 
#	python class name: DevInfAgent 
#	pygccxmldefinition name:smlDevInfAgentSendDevInf
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfAgent'].add_function_as_method('smlDevInfAgentSendDevInf', 'SmlBool', [param('SmlDevInfAgent *', 'agent', transfer_ownership=False), param('SmlSession *', 'session', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='SendDevInf')
#################### smlDevInfGetNthCTCap
# Return type: SmlDevInfCTCap const * (pointer_t)
# First Param is Pointer:  SmlDevInf const
# First Param is Const:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetNthCTCap
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetNthCTCap', retval('SmlDevInfCTCap *', is_const=True, caller_owns_return=False), [param('SmlDevInf *', 'devinf', transfer_ownership=False, is_const=True), param('unsigned int', 'n')], custom_name='GetNthCTCap')
#################### smlSanAlertGetType
# Return type: SmlAlertType (declarated_t)
# First Param is Pointer:  SmlSanAlert
# First Param is declarated:  SmlSanAlert [typedef]
#	class name: SmlSanAlert 
#	prefix: smlSanAlert 
#	python class name: SanAlert 
#	pygccxmldefinition name:smlSanAlertGetType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSanAlert'].add_function_as_method('smlSanAlertGetType', 'SmlAlertType', [param('SmlSanAlert *', 'alert', transfer_ownership=False)], custom_name='GetType')
#################### smlNotificationAssemble
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationAssemble
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationAssemble', 'SmlBool', [param('SmlNotification *', 'san', transfer_ownership=False), param('char * *', 'data'), param('unsigned int *', 'size'), param('SmlError * *', 'error')], custom_name='Assemble')
#################### smlMD5ToString
# Return type: char * (pointer_t)
# First Param is Pointer:  unsigned char
# First Param is Not Typedef:  unsigned char
# ADD_FUNCTION
    module.add_function('smlMD5ToString', 
                        'char *', 
                        [param('unsigned char *', 'digest'), param('SmlError * *', 'error')])
#################### smlLocationSetName
# Return type: void (void_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlLocationSetName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLocation'].add_function_as_method('smlLocationSetName', 'void', [param('SmlLocation *', 'loc', transfer_ownership=False), param('char *', 'name', transfer_ownership=False, is_const=True)], custom_name='SetName')
#################### smlDevInfPropertyNumPropParams
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInfProperty const
# First Param is Const:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyNumPropParams
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyNumPropParams', 'unsigned int', [param('SmlDevInfProperty *', 'property', transfer_ownership=False, is_const=True)], custom_name='NumPropParams')
#################### smlCommandRef
# Return type: SmlCommand * (pointer_t)
# First Param is Pointer:  SmlCommand
# First Param is declarated:  SmlCommand [typedef]
#	class name: SmlCommand 
#	prefix: smlCommand 
#	python class name: Command 
#	pygccxmldefinition name:smlCommandRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlCommand'].add_function_as_method('smlCommandRef', 'SmlCommand *', [param('SmlCommand *', 'cmd', transfer_ownership=False)], custom_name='Ref')
#################### smlDevInfDevTypeFromString
# Return type: SmlDevInfDevTyp (declarated_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlDevInfDevTypeFromString', 
                        'SmlDevInfDevTyp', 
                        [param('char *', 'name', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlDevInfPropertySetDataType
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertySetDataType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertySetDataType', 'void', [param('SmlDevInfProperty *', 'property', transfer_ownership=False), param('char *', 'dataType', transfer_ownership=False, is_const=True)], custom_name='SetDataType')
#################### smlManagerObjectRegister
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerObjectRegister
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerObjectRegister', 'SmlBool', [param('SmlManager *', 'manager', transfer_ownership=False), param('SmlCommandType', 'type'), param('SmlSession *', 'session', transfer_ownership=False), param('SmlLocation *', 'location', transfer_ownership=False), param('SmlLocation *', 'source', transfer_ownership=False), param('char *', 'contentType', transfer_ownership=False, is_const=True), param('SmlCommandCb *', 'callback'), param('SmlCommandCb *', 'childCallback'), param('void *', 'userdata'), param('SmlError * *', 'error')], custom_name='ObjectRegister')
#################### smlTransportStop
# Return type: void (void_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportStop
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportStop', 'void', [param('SmlTransport *', 'tsp', transfer_ownership=False)], custom_name='Stop')
#	CONSTRUCTOR
    root_module['SmlDevInfContentType'].add_function_as_constructor('smlDevInfNewContentType', retval('SmlDevInfContentType *', caller_owns_return=True), [param('char *', 'cttype', transfer_ownership=False, is_const=True), param('char *', 'verct', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlDevInfPropParamAddValEnum
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfPropParam
# First Param is declarated:  SmlDevInfPropParam [typedef]
#	class name: SmlDevInfPropParam 
#	prefix: smlDevInfPropParam 
#	python class name: DevInfPropParam 
#	pygccxmldefinition name:smlDevInfPropParamAddValEnum
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfPropParam'].add_function_as_method('smlDevInfPropParamAddValEnum', 'void', [param('SmlDevInfPropParam *', 'propParam', transfer_ownership=False), param('char *', 'valEnum', transfer_ownership=False, is_const=True)], custom_name='AddValEnum')
#################### smlDevInfSetSupportsUTC
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetSupportsUTC
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetSupportsUTC', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('SmlBool', 'supports')], custom_name='SetSupportsUTC')
#################### smlAnchorFree
# Return type: void (void_t)
# First Param is Pointer:  SmlAnchor
# First Param is declarated:  SmlAnchor [typedef]
#	class name: SmlAnchor 
#	prefix: smlAnchor 
#	python class name: Anchor 
#	pygccxmldefinition name:smlAnchorFree
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlAnchor'].add_function_as_method('smlAnchorFree', 'void', [param('SmlAnchor *', 'anchor', transfer_ownership=False)], custom_name='Free')
#################### smlItemCheck
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemCheck
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemCheck', 'SmlBool', [param('SmlItem *', 'item', transfer_ownership=False)], custom_name='Check')
#################### smlDevInfSetManufacturer
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetManufacturer
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetManufacturer', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('char *', 'man', transfer_ownership=False, is_const=True)], custom_name='SetManufacturer')
#################### smlDevInfGetModel
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetModel
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetModel', retval('char *', is_const=True, caller_owns_return=False), [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='GetModel')
#################### smlNotificationNthAlert
# Return type: SmlSanAlert * (pointer_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationNthAlert
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationNthAlert', 'SmlSanAlert *', [param('SmlNotification *', 'san', transfer_ownership=False), param('unsigned int', 'nth')], custom_name='NthAlert')
#################### smlMD5GetDigest
# Return type: void (void_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlMD5GetDigest', 
                        'void', 
                        [param('char *', 'buffer', transfer_ownership=False, is_const=True), param('int', 'buffer_size'), param('unsigned char *', 'digest')])
#################### smlBase64Decode
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlBase64Decode', 
                        'SmlBool', 
                        [param('char *', 'input', transfer_ownership=False, is_const=True), param('char * *', 'output'), param('unsigned int *', 'outsize'), param('SmlError * *', 'error')])
#################### smlNotificationGetVersion
# Return type: SmlNotificationVersion (declarated_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationGetVersion
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationGetVersion', 'SmlNotificationVersion', [param('SmlNotification *', 'san', transfer_ownership=False)], custom_name='GetVersion')
#################### smlLinkFind
# Return type: SmlLink * (pointer_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlLinkFind
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlLinkFind', 
                        'SmlLink *', 
                        [param('SmlTransport *', 'tsp', transfer_ownership=False), param('void *', 'link_data')])
#################### smlLocationIsRelative
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlLocationIsRelative
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLocation'].add_function_as_method('smlLocationIsRelative', 'SmlBool', [param('SmlLocation *', 'location', transfer_ownership=False)], custom_name='IsRelative')
#################### smlStatusGetCode
# Return type: SmlErrorType (declarated_t)
# First Param is Pointer:  SmlStatus
# First Param is declarated:  SmlStatus [typedef]
#	class name: SmlStatus 
#	prefix: smlStatus 
#	python class name: Status 
#	pygccxmldefinition name:smlStatusGetCode
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlStatus'].add_function_as_method('smlStatusGetCode', 'SmlErrorType', [param('SmlStatus *', 'status', transfer_ownership=False)], custom_name='GetCode')
#################### smlDevInfDataStoreSetMemory
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreSetMemory
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreSetMemory', 'void', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False), param('SmlBool', 'shared'), param('unsigned int', 'maxid'), param('unsigned int', 'maxmem')], custom_name='SetMemory')
#################### smlDevInfCTCapGetVerCT
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfCTCap const
# First Param is Const:  SmlDevInfCTCap
# First Param is declarated:  SmlDevInfCTCap [typedef]
#	class name: SmlDevInfCTCap 
#	prefix: smlDevInfCTCap 
#	python class name: DevInfCTCap 
#	pygccxmldefinition name:smlDevInfCTCapGetVerCT
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfCTCap'].add_function_as_method('smlDevInfCTCapGetVerCT', 'char *', [param('SmlDevInfCTCap *', 'ctcap', transfer_ownership=False, is_const=True)], custom_name='GetVerCT')
#################### smlDevInfFromResult
# Return type: SmlDevInf * (pointer_t)
# First Param is Pointer:  SmlCommand
# First Param is declarated:  SmlCommand [typedef]
#	class name: SmlCommand 
#	prefix: smlCommand 
#	python class name: Command 
#	pygccxmldefinition name:smlDevInfFromResult
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlDevInfFromResult', 
                        'SmlDevInf *', 
                        [param('SmlCommand *', 'result', transfer_ownership=False), param('SmlError * *', 'error')])
#################### smlCommandNewPut
# Return type: SmlCommand * (pointer_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlCommandNewPut
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlCommandNewPut', 
                        retval('SmlCommand *', caller_owns_return=True), 
                        [param('SmlLocation *', 'target', transfer_ownership=False), param('SmlLocation *', 'source', transfer_ownership=False), param('char *', 'data', transfer_ownership=False, is_const=True), param('unsigned int', 'size'), param('char *', 'contenttype', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlCredNewAuth
# Return type: SmlCred * (pointer_t)
# First Param is declarated:  SmlAuthType [enumeration]
# First Param is Not Typedef:  SmlAuthType [enumeration]
# ADD_FUNCTION
    module.add_function('smlCredNewAuth', 
                        'SmlCred *', 
                        [param('SmlAuthType', 'type'), param('char *', 'username', transfer_ownership=False, is_const=True), param('char *', 'password', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlDevInfSupportsUTC
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSupportsUTC
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSupportsUTC', 'SmlBool', [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='SupportsUTC')
#################### smlDevInfSetOEM
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetOEM
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetOEM', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('char *', 'oem', transfer_ownership=False, is_const=True)], custom_name='SetOEM')
#################### smlChalUnref
# Return type: void (void_t)
# First Param is Pointer:  SmlChal
# First Param is declarated:  SmlChal [typedef]
#	class name: SmlChal 
#	prefix: smlChal 
#	python class name: Chal 
#	pygccxmldefinition name:smlChalUnref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlChal'].add_function_as_method('smlChalUnref', 'void', [param('SmlChal *', 'chal', transfer_ownership=False)], custom_name='Unref')
#################### smlDevInfSupportsLargeObjs
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSupportsLargeObjs
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSupportsLargeObjs', 'SmlBool', [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='SupportsLargeObjs')
#################### smlDevInfPropertyGetDataType
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfProperty const
# First Param is Const:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyGetDataType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyGetDataType', 'char *', [param('SmlDevInfProperty *', 'property', transfer_ownership=False, is_const=True)], custom_name='GetDataType')
#################### smlManagerObjectFree
# Return type: void (void_t)
# First Param is Pointer:  SmlObject
# First Param is declarated:  SmlObject [typedef]
#	class name: SmlObject 
#	prefix: smlObject 
#	python class name: Object 
#	pygccxmldefinition name:smlManagerObjectFree
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlManagerObjectFree', 
                        'void', 
                        [param('SmlObject *', 'object', transfer_ownership=False)])
#################### smlNotificationGetInitiator
# Return type: SmlNotificationInitiator (declarated_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationGetInitiator
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationGetInitiator', 'SmlNotificationInitiator', [param('SmlNotification *', 'san', transfer_ownership=False)], custom_name='GetInitiator')
#################### smlLocationGetName
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlLocationGetName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLocation'].add_function_as_method('smlLocationGetName', retval('char *', is_const=True, caller_owns_return=False), [param('SmlLocation *', 'loc', transfer_ownership=False)], custom_name='GetName')
#################### smlSessionRef
# Return type: SmlSession * (pointer_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionRef', 'SmlSession *', [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='Ref')
#################### smlDevInfSupportsNumberOfChanges
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSupportsNumberOfChanges
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSupportsNumberOfChanges', 'SmlBool', [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='SupportsNumberOfChanges')
#################### smlDevInfGetNthDataStore
# Return type: SmlDevInfDataStore const * (pointer_t)
# First Param is Pointer:  SmlDevInf const
# First Param is Const:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetNthDataStore
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetNthDataStore', retval('SmlDevInfDataStore *', is_const=True, caller_owns_return=False), [param('SmlDevInf *', 'devinf', transfer_ownership=False, is_const=True), param('unsigned int', 'nth')], custom_name='GetNthDataStore')
#################### smlDevInfPropertyNumValEnums
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInfProperty const
# First Param is Const:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyNumValEnums
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyNumValEnums', 'unsigned int', [param('SmlDevInfProperty *', 'property', transfer_ownership=False, is_const=True)], custom_name='NumValEnums')
#################### smlSessionSetRequestedMaxObjSize
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionSetRequestedMaxObjSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionSetRequestedMaxObjSize', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('int', 'limit')], custom_name='SetRequestedMaxObjSize')
#################### smlDevInfNumCTCaps
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInf const
# First Param is Const:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfNumCTCaps
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfNumCTCaps', 'unsigned int', [param('SmlDevInf *', 'devinf', transfer_ownership=False, is_const=True)], custom_name='NumCTCaps')
#################### smlStatusIsResult
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlStatus
# First Param is declarated:  SmlStatus [typedef]
#	class name: SmlStatus 
#	prefix: smlStatus 
#	python class name: Status 
#	pygccxmldefinition name:smlStatusIsResult
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlStatus'].add_function_as_method('smlStatusIsResult', 'SmlBool', [param('SmlStatus *', 'status', transfer_ownership=False)], custom_name='IsResult')
#################### smlDevInfPropertySetDisplayName
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertySetDisplayName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertySetDisplayName', 'void', [param('SmlDevInfProperty *', 'property', transfer_ownership=False), param('char *', 'displayName', transfer_ownership=False, is_const=True)], custom_name='SetDisplayName')
#################### smlCommandNewSync
# Return type: SmlCommand * (pointer_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlCommandNewSync
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlCommandNewSync', 
                        retval('SmlCommand *', caller_owns_return=True), 
                        [param('SmlLocation *', 'target', transfer_ownership=False), param('SmlLocation *', 'source', transfer_ownership=False), param('unsigned int', 'num_changes'), param('SmlError * *', 'error')])
#################### smlItemRef
# Return type: SmlItem * (pointer_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemRef', 'SmlItem *', [param('SmlItem *', 'item', transfer_ownership=False)], custom_name='Ref')
#################### smlDevInfCTCapSetVerCT
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfCTCap
# First Param is declarated:  SmlDevInfCTCap [typedef]
#	class name: SmlDevInfCTCap 
#	prefix: smlDevInfCTCap 
#	python class name: DevInfCTCap 
#	pygccxmldefinition name:smlDevInfCTCapSetVerCT
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfCTCap'].add_function_as_method('smlDevInfCTCapSetVerCT', 'void', [param('SmlDevInfCTCap *', 'ctcap', transfer_ownership=False), param('char *', 'verct', transfer_ownership=False, is_const=True)], custom_name='SetVerCT')
#################### smlDevInfDataStoreAddRx
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreAddRx
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreAddRx', 'void', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False), param('SmlDevInfContentType *', 'ct', transfer_ownership=False)], custom_name='AddRx')
#################### smlDevInfDataStoreAddTx
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreAddTx
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreAddTx', 'void', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False), param('SmlDevInfContentType *', 'ct', transfer_ownership=False)], custom_name='AddTx')
#################### smlDevInfDataStoreGetNthRx
# Return type: SmlDevInfContentType const * (pointer_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreGetNthRx
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreGetNthRx', retval('SmlDevInfContentType *', is_const=True, caller_owns_return=False), [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True), param('unsigned int', 'n')], custom_name='GetNthRx')
#################### smlItemGetData
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemGetData
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemGetData', 'SmlBool', [param('SmlItem *', 'item', transfer_ownership=False), param('char * *', 'data'), param('unsigned int *', 'size'), param('SmlError * *', 'error')], custom_name='GetData')
#################### smlDevInfNewPut
# Return type: SmlCommand * (pointer_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfNewPut
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfNewPut', 'SmlCommand *', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('SmlDevInfVersion', 'version'), param('SmlError * *', 'error')], custom_name='NewPut')
#################### smlDevInfPropertyGetPropName
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfProperty const
# First Param is Const:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyGetPropName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyGetPropName', 'char *', [param('SmlDevInfProperty *', 'property', transfer_ownership=False, is_const=True)], custom_name='GetPropName')
#################### smlDevInfDataStoreUnref
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreUnref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreUnref', 'void', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False)], custom_name='Unref')
#################### smlDevInfDataStoreGetNthTx
# Return type: SmlDevInfContentType const * (pointer_t)
# First Param is Pointer:  SmlDevInfDataStore const
# First Param is Const:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreGetNthTx
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreGetNthTx', retval('SmlDevInfContentType *', is_const=True, caller_owns_return=False), [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False, is_const=True), param('unsigned int', 'n')], custom_name='GetNthTx')
#################### smlDevInfDataStoreSetRxPref
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreSetRxPref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreSetRxPref', 'void', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False), param('char *', 'contenttype', transfer_ownership=False, is_const=True), param('char *', 'version', transfer_ownership=False, is_const=True)], custom_name='SetRxPref')
#	CONSTRUCTOR
    root_module['SmlStatus'].add_function_as_constructor('smlStatusNew', retval('SmlStatus *', caller_owns_return=True), [param('SmlErrorType', 'data'), param('unsigned int', 'cmdref'), param('unsigned int', 'msgref'), param('SmlLocation *', 'sourceref', transfer_ownership=False), param('SmlLocation *', 'targeref', transfer_ownership=False), param('SmlCommandType', 'type'), param('SmlError * *', 'error')])
#################### smlCommandNewPartialChange
# Return type: SmlCommand * (pointer_t)
# First Param is declarated:  SmlChangeType [enumeration]
# First Param is Not Typedef:  SmlChangeType [enumeration]
# ADD_FUNCTION
    module.add_function('smlCommandNewPartialChange', 
                        retval('SmlCommand *', caller_owns_return=True), 
                        [param('SmlChangeType', 'type'), param('char *', 'uid', transfer_ownership=False, is_const=True), param('char *', 'data', transfer_ownership=False, is_const=True), param('unsigned int', 'complete_size'), param('unsigned int', 'partial_size'), param('char *', 'contenttype', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlSessionRegisterCred
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionRegisterCred
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionRegisterCred', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlCred *', 'cred', transfer_ownership=False)], custom_name='RegisterCred')
#################### smlCredNew
# Return type: SmlCred * (pointer_t)
# First Param is declarated:  SmlAuthType [enumeration]
# First Param is Not Typedef:  SmlAuthType [enumeration]
# ADD_FUNCTION
    module.add_function('smlCredNew', 
                        retval('SmlCred *', caller_owns_return=True), 
                        [param('SmlAuthType', 'type'), param('SmlFormatType', 'format'), param('char *', 'data', transfer_ownership=False, is_const=True), param('char *', 'username', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlSessionSetReceivingMaxObjSize
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionSetReceivingMaxObjSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionSetReceivingMaxObjSize', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('unsigned int', 'limit')], custom_name='SetReceivingMaxObjSize')
#################### smlNotificationFree
# Return type: void (void_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationFree
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationFree', 'void', [param('SmlNotification *', 'san', transfer_ownership=False)], custom_name='Free')
#################### smlAuthFree
# Return type: void (void_t)
# First Param is Pointer:  SmlAuthenticator
# First Param is declarated:  SmlAuthenticator [typedef]
#	class name: SmlAuthenticator 
#	prefix: smlAuthenticator 
#	python class name: Authenticator 
#	pygccxmldefinition name:smlAuthFree
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlAuthFree', 
                        'void', 
                        [param('SmlAuthenticator *', 'auth', transfer_ownership=False)])
#################### smlCredFree
# Return type: void (void_t)
# First Param is Pointer:  SmlCred
# First Param is declarated:  SmlCred [typedef]
#	class name: SmlCred 
#	prefix: smlCred 
#	python class name: Cred 
#	pygccxmldefinition name:smlCredFree
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlCred'].add_function_as_method('smlCredFree', 'void', [param('SmlCred *', 'cred', transfer_ownership=False)], custom_name='Free')
#################### smlCommandNewMap
# Return type: SmlCommand * (pointer_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlCommandNewMap
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlCommandNewMap', 
                        retval('SmlCommand *', caller_owns_return=True), 
                        [param('SmlLocation *', 'target', transfer_ownership=False), param('SmlLocation *', 'source', transfer_ownership=False), param('SmlError * *', 'error')])
#################### smlDevInfPropertyGetMaxSize
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlDevInfProperty const
# First Param is Const:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyGetMaxSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyGetMaxSize', 'unsigned int', [param('SmlDevInfProperty *', 'property', transfer_ownership=False, is_const=True)], custom_name='GetMaxSize')
#################### smlAuthHeaderReply
# Return type: SmlStatus * (pointer_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlAuthHeaderReply
#	ADD_FUNCTION_AS_METHOD
    module.add_function('smlAuthHeaderReply', 
                        'SmlStatus *', 
                        [param('SmlSession *', 'session', transfer_ownership=False), param('SmlAuthType', 'code'), param('SmlError * *', 'error')])
#################### smlSessionSendReply
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionSendReply
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionSendReply', 'SmlBool', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlStatus *', 'status', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='SendReply')
#################### smlNotificationGetSessionID
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationGetSessionID
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationGetSessionID', 'unsigned int', [param('SmlNotification *', 'san', transfer_ownership=False)], custom_name='GetSessionID')
#################### smlDevInfPropertyGetNoTruncate
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInfProperty const
# First Param is Const:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertyGetNoTruncate
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertyGetNoTruncate', 'SmlBool', [param('SmlDevInfProperty *', 'property', transfer_ownership=False, is_const=True)], custom_name='GetNoTruncate')
#################### smlCommandNewReply
# Return type: SmlStatus * (pointer_t)
# First Param is Pointer:  SmlCommand
# First Param is declarated:  SmlCommand [typedef]
#	class name: SmlCommand 
#	prefix: smlCommand 
#	python class name: Command 
#	pygccxmldefinition name:smlCommandNewReply
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlCommand'].add_function_as_method('smlCommandNewReply', 'SmlStatus *', [param('SmlCommand *', 'cmd', transfer_ownership=False), param('SmlErrorType', 'code'), param('SmlError * *', 'error')], custom_name='NewReply')
#################### smlDevInfGetManufacturer
# Return type: char const * (pointer_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfGetManufacturer
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfGetManufacturer', retval('char *', is_const=True, caller_owns_return=False), [param('SmlDevInf *', 'devinf', transfer_ownership=False)], custom_name='GetManufacturer')
#################### smlDevInfCTCapTypeFromString
# Return type: SmlDevInfCTCapType (declarated_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlDevInfCTCapTypeFromString', 
                        'SmlDevInfCTCapType', 
                        [param('char *', 'name', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlDevInfPropParamSetDataType
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfPropParam
# First Param is declarated:  SmlDevInfPropParam [typedef]
#	class name: SmlDevInfPropParam 
#	prefix: smlDevInfPropParam 
#	python class name: DevInfPropParam 
#	pygccxmldefinition name:smlDevInfPropParamSetDataType
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfPropParam'].add_function_as_method('smlDevInfPropParamSetDataType', 'void', [param('SmlDevInfPropParam *', 'propParam', transfer_ownership=False), param('char *', 'dataType', transfer_ownership=False, is_const=True)], custom_name='SetDataType')
#################### smlTransportSetConfigOption
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportSetConfigOption
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportSetConfigOption', 'SmlBool', [param('SmlTransport *', 'tsp', transfer_ownership=False), param('char *', 'name', transfer_ownership=False, is_const=True), param('char *', 'value', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')], custom_name='SetConfigOption')
#################### smlManagerCheck
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerCheck
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerCheck', 'SmlBool', [param('SmlManager *', 'manager', transfer_ownership=False)], custom_name='Check')
#	CONSTRUCTOR
    root_module['SmlLocation'].add_function_as_constructor('smlLocationNew', retval('SmlLocation *', caller_owns_return=True), [param('char *', 'locURI', transfer_ownership=False, is_const=True), param('char *', 'locName', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlDevInfDataStoreSetSyncCap
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreSetSyncCap
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreSetSyncCap', 'void', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False), param('SmlDevInfSyncCap', 'cap'), param('SmlBool', 'supported')], custom_name='SetSyncCap')
#################### smlDevInfSetDeviceID
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfSetDeviceID
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfSetDeviceID', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('char *', 'devid', transfer_ownership=False, is_const=True)], custom_name='SetDeviceID')
#################### smlDevInfAddDataStore
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInf
# First Param is declarated:  SmlDevInf [typedef]
#	class name: SmlDevInf 
#	prefix: smlDevInf 
#	python class name: DevInf 
#	pygccxmldefinition name:smlDevInfAddDataStore
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInf'].add_function_as_method('smlDevInfAddDataStore', 'void', [param('SmlDevInf *', 'devinf', transfer_ownership=False), param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False)], custom_name='AddDataStore')
#################### smlLocationCopy
# Return type: void (void_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlLocationCopy
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLocation'].add_function_as_method('smlLocationCopy', 'void', [param('SmlLocation *', 'source', transfer_ownership=False), param('SmlLocation *', 'target', transfer_ownership=False)], custom_name='Copy')
#	CONSTRUCTOR
    root_module['SmlDevInfPropParam'].add_function_as_constructor('smlDevInfNewPropParam', retval('SmlDevInfPropParam *', caller_owns_return=True), [param('SmlError * *', 'error')])
#################### smlCredRef
# Return type: void (void_t)
# First Param is Pointer:  SmlCred
# First Param is declarated:  SmlCred [typedef]
#	class name: SmlCred 
#	prefix: smlCred 
#	python class name: Cred 
#	pygccxmldefinition name:smlCredRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlCred'].add_function_as_method('smlCredRef', 'void', [param('SmlCred *', 'cred', transfer_ownership=False)], custom_name='Ref')
#	CONSTRUCTOR
    root_module['SmlManager'].add_function_as_constructor('smlManagerNew', retval('SmlManager *', caller_owns_return=True), [param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlError * *', 'error')])
#################### smlNotificationNewAlert
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationNewAlert
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationNewAlert', 'SmlBool', [param('SmlNotification *', 'san', transfer_ownership=False), param('SmlAlertType', 'type'), param('char *', 'contenttype', transfer_ownership=False, is_const=True), param('char *', 'serverURI', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')], custom_name='NewAlert')
#################### smlItemGetSource
# Return type: SmlLocation * (pointer_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemGetSource
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemGetSource', 'SmlLocation *', [param('SmlItem *', 'item', transfer_ownership=False)], custom_name='GetSource')
#################### smlNotificationNumAlerts
# Return type: unsigned int (unsigned_int_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationNumAlerts
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationNumAlerts', 'unsigned int', [param('SmlNotification *', 'san', transfer_ownership=False)], custom_name='NumAlerts')
#################### smlDevInfAgentRegisterSession
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInfAgent
# First Param is declarated:  SmlDevInfAgent [typedef]
#	class name: SmlDevInfAgent 
#	prefix: smlDevInfAgent 
#	python class name: DevInfAgent 
#	pygccxmldefinition name:smlDevInfAgentRegisterSession
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfAgent'].add_function_as_method('smlDevInfAgentRegisterSession', 'SmlBool', [param('SmlDevInfAgent *', 'agent', transfer_ownership=False), param('SmlManager *', 'manager', transfer_ownership=False), param('SmlSession *', 'session', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='RegisterSession')
#################### smlItemAddData
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemAddData
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemAddData', 'SmlBool', [param('SmlItem *', 'item', transfer_ownership=False), param('char *', 'data', transfer_ownership=False, is_const=True), param('unsigned int', 'size'), param('SmlError * *', 'error')], custom_name='AddData')
#################### smlNotificationSend
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlNotification
# First Param is declarated:  SmlNotification [typedef]
#	class name: SmlNotification 
#	prefix: smlNotification 
#	python class name: Notification 
#	pygccxmldefinition name:smlNotificationSend
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlNotification'].add_function_as_method('smlNotificationSend', 'SmlBool', [param('SmlNotification *', 'san', transfer_ownership=False), param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='Send')
#################### smlDevInfAgentGetDevInf
# Return type: SmlDevInf * (pointer_t)
# First Param is Pointer:  SmlDevInfAgent
# First Param is declarated:  SmlDevInfAgent [typedef]
#	class name: SmlDevInfAgent 
#	prefix: smlDevInfAgent 
#	python class name: DevInfAgent 
#	pygccxmldefinition name:smlDevInfAgentGetDevInf
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfAgent'].add_function_as_method('smlDevInfAgentGetDevInf', 'SmlDevInf *', [param('SmlDevInfAgent *', 'agent', transfer_ownership=False)], custom_name='GetDevInf')
#################### smlDevInfPropertySetPropSize
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfProperty
# First Param is declarated:  SmlDevInfProperty [typedef]
#	class name: SmlDevInfProperty 
#	prefix: smlDevInfProperty 
#	python class name: DevInfProperty 
#	pygccxmldefinition name:smlDevInfPropertySetPropSize
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfProperty'].add_function_as_method('smlDevInfPropertySetPropSize', 'void', [param('SmlDevInfProperty *', 'property', transfer_ownership=False), param('unsigned int', 'propSize')], custom_name='SetPropSize')
#################### smlTransportSetEventCallback
# Return type: void (void_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportSetEventCallback
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportSetEventCallback', 'void', [param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlTransportEventCb *', 'callback'), param('void *', 'userdata')], custom_name='SetEventCallback')
#	CONSTRUCTOR
    root_module['SmlTransportData'].add_function_as_constructor('smlTransportDataNew', retval('SmlTransportData *', caller_owns_return=True), [param('char *', 'data'), param('long unsigned int', 'size'), param('SmlMimeType', 'mimetype'), param('SmlBool', 'ownsData'), param('SmlError * *', 'error')])
#################### smlItemNewForData
# Return type: SmlItem * (pointer_t)
# First Param is Pointer:  char const
# First Param is Const:  char
# First Param is Not Typedef:  char
# ADD_FUNCTION
    module.add_function('smlItemNewForData', 
                        'SmlItem *', 
                        [param('char *', 'data', transfer_ownership=False, is_const=True), param('unsigned int', 'size'), param('SmlError * *', 'error')])
#################### smlDevInfPropParamGetDisplayName
# Return type: char * (pointer_t)
# First Param is Pointer:  SmlDevInfPropParam const
# First Param is Const:  SmlDevInfPropParam
# First Param is declarated:  SmlDevInfPropParam [typedef]
#	class name: SmlDevInfPropParam 
#	prefix: smlDevInfPropParam 
#	python class name: DevInfPropParam 
#	pygccxmldefinition name:smlDevInfPropParamGetDisplayName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfPropParam'].add_function_as_method('smlDevInfPropParamGetDisplayName', 'char *', [param('SmlDevInfPropParam *', 'propParam', transfer_ownership=False, is_const=True)], custom_name='GetDisplayName')
#################### smlSessionUseStringTable
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionUseStringTable
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionUseStringTable', 'void', [param('SmlSession *', 'session', transfer_ownership=False), param('SmlBool', 'useStringtable')], custom_name='UseStringTable')
#################### smlDevInfDataStoreSetDisplayName
# Return type: void (void_t)
# First Param is Pointer:  SmlDevInfDataStore
# First Param is declarated:  SmlDevInfDataStore [typedef]
#	class name: SmlDevInfDataStore 
#	prefix: smlDevInfDataStore 
#	python class name: DevInfDataStore 
#	pygccxmldefinition name:smlDevInfDataStoreSetDisplayName
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfDataStore'].add_function_as_method('smlDevInfDataStoreSetDisplayName', 'void', [param('SmlDevInfDataStore *', 'datastore', transfer_ownership=False), param('char *', 'displayName', transfer_ownership=False, is_const=True)], custom_name='SetDisplayName')
#################### smlChalFree
# Return type: void (void_t)
# First Param is Pointer:  SmlChal
# First Param is declarated:  SmlChal [typedef]
#	class name: SmlChal 
#	prefix: smlChal 
#	python class name: Chal 
#	pygccxmldefinition name:smlChalFree
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlChal'].add_function_as_method('smlChalFree', 'void', [param('SmlChal *', 'chal', transfer_ownership=False)], custom_name='Free')
#################### smlDevInfAgentRequestDevInf
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlDevInfAgent
# First Param is declarated:  SmlDevInfAgent [typedef]
#	class name: SmlDevInfAgent 
#	prefix: smlDevInfAgent 
#	python class name: DevInfAgent 
#	pygccxmldefinition name:smlDevInfAgentRequestDevInf
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlDevInfAgent'].add_function_as_method('smlDevInfAgentRequestDevInf', 'SmlBool', [param('SmlDevInfAgent *', 'agent', transfer_ownership=False), param('SmlSession *', 'session', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='RequestDevInf')
#################### smlSessionUnref
# Return type: void (void_t)
# First Param is Pointer:  SmlSession
# First Param is declarated:  SmlSession [typedef]
#	class name: SmlSession 
#	prefix: smlSession 
#	python class name: Session 
#	pygccxmldefinition name:smlSessionUnref
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlSession'].add_function_as_method('smlSessionUnref', 'void', [param('SmlSession *', 'session', transfer_ownership=False)], custom_name='Unref')
#################### smlTransportDisconnect
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportDisconnect
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportDisconnect', 'SmlBool', [param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlLink *', 'link', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='Disconnect')
#################### smlManagerStart
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerStart
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerStart', 'SmlBool', [param('SmlManager *', 'manager', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='Start')
#################### smlChalNewFromBinary
# Return type: SmlChal * (pointer_t)
# First Param is declarated:  SmlAuthType [enumeration]
# First Param is Not Typedef:  SmlAuthType [enumeration]
# ADD_FUNCTION
    module.add_function('smlChalNewFromBinary', 
                        'SmlChal *', 
                        [param('SmlAuthType', 'type'), param('char *', 'nonce', transfer_ownership=False, is_const=True), param('size_t', 'length'), param('SmlError * *', 'error')])
#	CONSTRUCTOR
    root_module['SmlDevInfDataStore'].add_function_as_constructor('smlDevInfDataStoreNew', retval('SmlDevInfDataStore *', caller_owns_return=True), [param('char *', 'sourceRef', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlCommandNewAlert
# Return type: SmlCommand * (pointer_t)
# First Param is declarated:  SmlAlertType [enumeration]
# First Param is Not Typedef:  SmlAlertType [enumeration]
# ADD_FUNCTION
    module.add_function('smlCommandNewAlert', 
                        retval('SmlCommand *', caller_owns_return=True), 
                        [param('SmlAlertType', 'type'), param('SmlLocation *', 'target', transfer_ownership=False), param('SmlLocation *', 'source', transfer_ownership=False), param('char *', 'next', transfer_ownership=False, is_const=True), param('char *', 'last', transfer_ownership=False, is_const=True), param('char *', 'contenttype', transfer_ownership=False, is_const=True), param('SmlError * *', 'error')])
#################### smlItemHasData
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemHasData
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemHasData', 'SmlBool', [param('SmlItem *', 'item', transfer_ownership=False)], custom_name='HasData')
#################### smlTransportSetError
# Return type: void (void_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportSetError
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportSetError', 'void', [param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlLink *', 'link', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='SetError')
#################### smlLocationRef
# Return type: SmlLocation * (pointer_t)
# First Param is Pointer:  SmlLocation
# First Param is declarated:  SmlLocation [typedef]
#	class name: SmlLocation 
#	prefix: smlLocation 
#	python class name: Location 
#	pygccxmldefinition name:smlLocationRef
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlLocation'].add_function_as_method('smlLocationRef', 'SmlLocation *', [param('SmlLocation *', 'loc', transfer_ownership=False)], custom_name='Ref')
#################### smlTransportRunAsync
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlTransport
# First Param is declarated:  SmlTransport [typedef]
#	class name: SmlTransport 
#	prefix: smlTransport 
#	python class name: Transport 
#	pygccxmldefinition name:smlTransportRunAsync
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlTransport'].add_function_as_method('smlTransportRunAsync', 'SmlBool', [param('SmlTransport *', 'tsp', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='RunAsync')
#################### smlItemSetRaw
# Return type: void (void_t)
# First Param is Pointer:  SmlItem
# First Param is declarated:  SmlItem [typedef]
#	class name: SmlItem 
#	prefix: smlItem 
#	python class name: Item 
#	pygccxmldefinition name:smlItemSetRaw
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlItem'].add_function_as_method('smlItemSetRaw', 'void', [param('SmlItem *', 'item', transfer_ownership=False), param('SmlBool', 'raw')], custom_name='SetRaw')
#################### smlManagerDispatchHeader
# Return type: SmlBool (declarated_t)
# First Param is Pointer:  SmlManager
# First Param is declarated:  SmlManager [typedef]
#	class name: SmlManager 
#	prefix: smlManager 
#	python class name: Manager 
#	pygccxmldefinition name:smlManagerDispatchHeader
#	ADD_FUNCTION_AS_METHOD
    root_module['SmlManager'].add_function_as_method('smlManagerDispatchHeader', 'SmlBool', [param('SmlManager *', 'manager', transfer_ownership=False), param('SmlSession *', 'session', transfer_ownership=False), param('SmlHeader *', 'header', transfer_ownership=False), param('SmlCred *', 'cred', transfer_ownership=False), param('SmlError * *', 'error')], custom_name='DispatchHeader')
    register_functions_std(module.get_submodule('std'), root_module)
    return

def register_functions_std(module, root_module):
    return

def main():
    out = FileCodeSink(sys.stdout)
    root_module = module_init()
    register_types(root_module)
    register_methods(root_module)
    register_functions(root_module)
    root_module.generate(out)

if __name__ == '__main__':
    main()

