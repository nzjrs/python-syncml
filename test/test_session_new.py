import common
import syncml

l = syncml.Location("/test", "")
s = syncml.Session(syncml.SML_SESSION_TYPE_CLIENT, syncml.SML_MIMETYPE_XML, syncml.SML_VERSION_12, syncml.SML_PROTOCOL_SYNCML, l, l, "1", 0)

print "FINISHED"
