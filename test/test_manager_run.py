import common
import syncml

s = syncml.Transport(syncml.SML_TRANSPORT_HTTP_SERVER)
sm = syncml.Manager(s)

if s and sm:
    if sm.Start():
        print "STARTED OK"
        sm.Stop()
        print "FINISHED"

s = None
sm = None

