import common
import syncml

done = False

def manager_cb(eventType, session):
    print "CALLBACK ", common.EVENTS[eventType]
    #if eventType == syncml.SML_MANAGER_SESSION_ERROR:
    #    global done
    #    done = True

cm,sm,c,s = common.get_manager_and_transports(manager_cb, manager_cb)

c.SetConfigOption("URL", "http://127.0.0.1:12021")
s.SetConfigOption("PORT","12021")

c.Initialize()
s.Initialize()

cm.Start()
sm.Start()

datastr = "<SyncML><SyncHdr><VerProto>SyncML/1.1</VerProto><VerDTD>1.1</VerDTD><MsgID>1</MsgID><SessionID>1</SessionID><Target><LocURI>test</LocURI></Target><Source><LocURI>test</LocURI></Source></SyncHdr><SyncBody><Alert><CmdID>1</CmdID><Item><Target><LocURI>/test</LocURI></Target><Source><LocURI>/test</LocURI></Source><Meta><Anchor xmlns=\"syncml:metinf\"><Next>Next</Next><Last>last</Last></Anchor></Meta></Item><Data>200</Data></Alert><Final></Final></SyncBody></SyncML>"

data = syncml.TransportData(datastr, len(datastr), syncml.SML_MIMETYPE_XML, False)

c.Send(None, data)
while not done:
    sm.Dispatch()

cm ,sm,c,s = None,None,None,None

print "FINISHED"
