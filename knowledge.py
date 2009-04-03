# This could probbably be automatic, if it wasnt for
# "smlAuthNew"                :   "SmlAuthenticator"
# (difference in name)
CONSTRUCTORS = {
    #include <libsyncml/sml_manager.h>
    "smlManagerNew"             :   "SmlManager",
    #include <libsyncml/sml_session.h>
    "smlSessionNew"             :   "SmlSession",
    #include <libsyncml/sml_transport.h>
    "smlLinkNew"                :   "SmlLink",
    "smlTransportNew"           :   "SmlTransport",
    "smlTransportDataNew"       :   "SmlTransportData",
    #include <libsyncml/sml_elements.h>
    "smlLocationNew"            :   "SmlLocation",
    "smlAnchorNew"              :   "SmlAnchor",
    "smlItemNew"                :   "SmlItem",
    "smlMapItemNew"             :   "SmlMapItem",
    #include <libsyncml/sml_auth.h>
    "smlAuthNew"                :   "SmlAuthenticator",
    #include <libsyncml/sml_command.h>
    "smlStatusNew"              :   "SmlStatus",
    "smlCommandNew"             :   "SmlCommand",
    #include <libsyncml/sml_devinf.h>
    "smlDevInfNew"              :   "SmlDevInf",
    "smlDevInfDataStoreNew"     :   "SmlDevInfDataStore",

    "smlDevInfNewContentType"   :   "SmlDevInfContentType",
    "smlDevInfNewCTCap"         :   "SmlDevInfCTCap",
    "smlDevInfNewProperty"      :   "SmlDevInfProperty",
    "smlDevInfNewPropParam"     :   "SmlDevInfPropParam",
    #include <libsyncml/sml_devinf.h>
    "smlDevInfAgentNew"         :   "SmlDevInfAgent",
    #include <libsyncml/sml_notification.h>
    "smlNotificationNew"        :   "SmlNotification"
    #include <libsyncml/sml_defines.h>
    #include <libsyncml/sml_error.h>
    #include <libsyncml/sml_base64.h>
    #include <libsyncml/sml_md5.h>
}

CUSTOM_ANNOTATIONS = {
    #poorly named functions
    "SmlAuthenticator"      :   {'free_function':'smlAuthFree'},
    "SmlObject"             :   {'free_function':'smlManagerObjectFree'},
    "SmlSanAlert"           :   {'free_function':'smlNotificationFreeAlert'},
    #unimplemented free functions
    "SmlDevInfContentType"  :   {'free_function':'HACKFree'},
    "SmlDevInfCTCap"        :   {'free_function':'HACKFree'},
    "SmlDevInfProperty"     :   {'free_function':'HACKFree'},
    "SmlDevInfPropParam"    :   {'free_function':'HACKFree'},
    #objects with reference counting: Ref/Deref
    "SmlTransportData"      :   {'free_function':   'smlTransportDataDeref',
                                 'incref_function': 'smlTransportDataRef',
                                 'decref_function': 'smlTransportDataDeref'
                                },
    "SmlLink"               :   {'free_function':   'smlLinkDeref',
                                 'incref_function': 'smlLinkRef',
                                 'decref_function': 'smlLinkDeref'
                                }
}

# objects with a free function but no reference counting
TYPES_WITH_NO_REF_COUNTING = ('Anchor', 'Notification', 'Header', 'Manager', 'Transport', "DevInfAgent")

# objects with reference counting: Ref/Unref
TYPES_WITH_REF_COUNTING = ('DevInfDataStore', 'DevInf', 'MapItem', 'Location', 'Item', 'Command', 'Session', 'Status', 'Cred', 'Chal')

TYPES_TO_IGNORE = ('PendingStatus', 'Error', 'Parser', 'Assembler')

LIES = (
    #in the headers but not in the library
    "smlManagerReceive",
    #depreciated (sml_devinf.h)
    "smlDevInfAddCTCap",
    "smlDevInfGetNthCTCapType",
    "smlDevInfGetNthCTCapValue",
    "smlDevInfDataStoreSetRx",
    "smlDevInfDataStoreGetRx",
    "smlDevInfDataStoreSetTx",
    "smlDevInfDataStoreGetTx",
    #depreciated (sml_session.h)
    "smlSessionSetSendingLimit",
    "smlSessionSetReceivingLimit",
    "smlSessionGetSendingLimit"
)

PARAMETER_ANNOTATIONS = {
    #function name                      #param/s        #annotations
    "smlManagerNew":                    {'tsp'      :   {'transfer_ownership':'False'}},
    "smlManagerDispatchChildCommand":   {'session'  :   {'transfer_ownership':'False'},
                                         'parent'   :   {'transfer_ownership':'False'},
                                         'cmd'      :   {'transfer_ownership':'False'}},
    "smlManagerDispatchHeader":         {'session'  :   {'transfer_ownership':'False'},
                                         'header'   :   {'transfer_ownership':'False'},
                                         'cred'     :   {'transfer_ownership':'False'}},
    "smlManagerDispatchCommand":        {'session'  :   {'transfer_ownership':'False'},
                                         'cmd'      :   {'transfer_ownership':'False'}},
    "smlManagerObjectFind":             {'session'  :   {'transfer_ownership':'False'},
                                         'cmd'      :   {'transfer_ownership':'False'}},
    "smlManagerSessionAdd":             {'session'  :   {'transfer_ownership':'False'},
                                         'link'     :   {'transfer_ownership':'False'}},
    "smlManagerObjectRegister":         {'session'  :   {'transfer_ownership':'False'},
                                         'location' :   {'transfer_ownership':'False'},
                                         'source'   :   {'transfer_ownership':'False'}},
    "smlManagerSessionRemove":          {'session'  :   {'transfer_ownership':'False'}},
    "smlManagerObjectFree":             {'object'   :   {'transfer_ownership':'False'}},
    "smlDevInfAgentRegisterSession":    {'manager'  :   {'transfer_ownership':'False'},
                                         'session'  :   {'transfer_ownership':'False'}},
    "smlDevInfAgentRequestDevInf":      {'session'  :   {'transfer_ownership':'False'}},
    "smlDevInfCTCapAddProperty":        {'property' :   {'transfer_ownership':'False'}},
    "smlDevInfGetCTCap":                {'ct'       :   {'transfer_ownership':'False'}},
    "smlDevInfAddDataStore":            {'datastore':   {'transfer_ownership':'False'}},
    "smlDevInfDataStoreAddTx":          {'ct'       :   {'transfer_ownership':'False'}},
    "smlDevInfDataStoreAddRx":          {'ct'       :   {'transfer_ownership':'False'}},
    "smlDevInfFreeContentType":         {'ct'       :   {'transfer_ownership':'False'}},
    "smlDevInfPropertyAddPropParam":    {'propParam':   {'transfer_ownership':'False'}},
    "smlDevInfConfigureSession":        {'session'  :   {'transfer_ownership':'False'}},
    "smlDevInfAppendCTCap":             {'ctcap'    :   {'transfer_ownership':'False'}},
    "smlDevInfNewResult":               {'devinf'   :   {'transfer_ownership':'False'},
                                         'cmd'      :   {'transfer_ownership':'False'}},
    "smlDevInfAgentSetDevInf":          {'devinf'   :   {'transfer_ownership':'False'}},
    "smlDevInfAgentNew":                {'devinf'   :   {'transfer_ownership':'False'}},
    "smlDevInfAgentRegister":           {'manager'  :   {'transfer_ownership':'False'}},
    "smlDevInfSetMaxGUIDSize":          {'datastore':   {'transfer_ownership':'False'}},
    "smlDevInfAgentSendDevInf":         {'session'  :   {'transfer_ownership':'False'}},
    "smlDevInfFromResult":              {'result'   :   {'transfer_ownership':'False'}},
    "smlSessionReceiveHeader" :         {'header'   :   {'transfer_ownership':'False'}},
    "smlSessionStartCommand" :          {'cmd'      :   {'transfer_ownership':'False'},
                                         'parent'   :   {'transfer_ownership':'False'}},
    "smlSessionEndCommand":             {'parent'   :   {'transfer_ownership':'False'}},
    "smlSessionSendCommand":            {'cmd'      :   {'transfer_ownership':'False'},
                                         'parent'   :   {'transfer_ownership':'False'}},
    "smlSessionDispatchEvent":          {'cmd'      :   {'transfer_ownership':'False'},
                                         'parent'   :   {'transfer_ownership':'False'},
                                         'headerreply': {'transfer_ownership':'False'}},
    "smlSessionNew":                    {'target'   :   {'transfer_ownership':'False'},
                                         'source'   :   {'transfer_ownership':'False'}},
    "smlSessionSendReply":              {'status'   :   {'transfer_ownership':'False'}},
    "smlSessionRegisterCred":           {'cred'     :   {'transfer_ownership':'False'}},
    "smlItemSetSource":                 {'source'   :   {'transfer_ownership':'False'}},
    "smlItemSetTarget":                 {'target'   :   {'transfer_ownership':'False'}},
    "smlNotificationFreeAlert":         {'alert'    :   {'transfer_ownership':'False'}},
    "smlNotificationSetManager":        {'manager'  :   {'transfer_ownership':'False'}},
    "smlLinkNew":                       {'tsp'      :   {'transfer_ownership':'False'}},
    "smlLinkFind":                      {'tsp'      :   {'transfer_ownership':'False'}},
    "smlCommandNewGet":                 {'target'   :   {'transfer_ownership':'False'},
                                         'return'   :   {'caller_owns_return':'True' }},
    "smlCommandNewPut":                 {'target'   :   {'transfer_ownership':'False'},
                                         'source'   :   {'transfer_ownership':'False'},
                                         'return'   :   {'caller_owns_return':'True' }},
    "smlCommandNewSync":                {'target'   :   {'transfer_ownership':'False'},
                                         'source'   :   {'transfer_ownership':'False'},
                                         'return'   :   {'caller_owns_return':'True' }},
    "smlCommandNewMap":                 {'target'   :   {'transfer_ownership':'False'},
                                         'source'   :   {'transfer_ownership':'False'},
                                         'return'   :   {'caller_owns_return':'True' }},
    "smlCommandNewAlert":               {'target'   :   {'transfer_ownership':'False'},
                                         'source'   :   {'transfer_ownership':'False'},
                                         'return'   :   {'caller_owns_return':'True' }},
    "smlCommandNewPartialChange":       {'return'   :   {'caller_owns_return':'True' }},
    "smlCommandNewChange":              {'return'   :   {'caller_owns_return':'True' }},
    "smlNotificationSetCred":           {'cred'     :   {'transfer_ownership':'False'}},
    "smlNotificationSend":              {'tsp'      :   {'transfer_ownership':'False'}},
    "smlAuthSetVerifyCallback":         {'auth'     :   {'transfer_ownership':'False'}},
    "smlAuthRegister":                  {'auth'     :   {'transfer_ownership':'False'},
                                         'manager'  :   {'transfer_ownership':'False'}},
    "smlAuthVerify":                    {'chal'     :   {'transfer_ownership':'False'},
                                         'cred'     :   {'transfer_ownership':'False'}},
    "smlAuthSetState":                  {'auth'     :   {'transfer_ownership':'False'}},
    "smlAuthSetEnable":                 {'auth'     :   {'transfer_ownership':'False'}},
    "smlAuthFree":                      {'auth'     :   {'transfer_ownership':'False'}},
    "smlAuthIsEnabled":                 {'auth'     :   {'transfer_ownership':'False'}},
    "smlAuthHeaderReply":               {'session'  :   {'transfer_ownership':'False'}},
    "smlStatusNew":                     {'sourceref':   {'transfer_ownership':'False'},
                                         'targeref' :   {'transfer_ownership':'False'}},
    "smlLocationCompare":               {'object'   :   {'transfer_ownership':'False'},
                                         'urlroot'  :   {'transfer_ownership':'False'},
                                         'url'      :   {'transfer_ownership':'False'}},
    "smlCommandNewResult":              {'source'   :   {'transfer_ownership':'False'}},
    "smlCommandAddMapItem":             {'item'     :   {'transfer_ownership':'False'}},
    "smlTransportSend":                 {'link'     :   {'transfer_ownership':'False',
                                                         'null_ok':'True'            },
                                         'data'     :   {'transfer_ownership':'False'}},
    "smlTransportSetError":             {'link'     :   {'transfer_ownership':'False'}},
    "smlTransportDisconnect":           {'link'     :   {'transfer_ownership':'False'}},
    "smlLocationCopy":                  {'target'   :   {'transfer_ownership':'False'}},
    "smlCredNew":                       {'return'   :   {'caller_owns_return':'True' }},
}	
