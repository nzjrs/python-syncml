import common
import syncml

s = syncml.Transport(syncml.SML_TRANSPORT_HTTP_SERVER)
sm = syncml.Manager(s)

if s and sm:
    print "FINISHED"

s = None
sm = None

