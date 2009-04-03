import common
import syncml

class ErrorTest:
    def __init__(self):
        self.cm,sm,self.c,s = common.get_manager_and_transports(self.manager_cb, self.manager_cb)

        self.c.SetConfigOption("URL", "http://127.0.0.1:12020")
        s.SetConfigOption("PORT","12020")

        self.c.Initialize()
        s.Initialize()

        self.cm.Start()
        sm.Start()

        self.done = False

    def manager_cb(self, eventType, session):
    	print "CALLBACK ", common.EVENTS[eventType]
        if eventType == syncml.SML_MANAGER_SESSION_ERROR:
            self.done = True

    def run(self):
        datastr = "<SyncML></SyncML>"
        #datastr = "<SyncML><SyncHdr><VerProto>SyncML/1.1</VerProto><VerDTD>1.1</VerDTD><MsgID>1</MsgID><SessionID>1</SessionID><Target><LocURI>test</LocURI></Target><Source><LocURI>test</LocURI></Source></SyncHdr><SyncBody><Alert><CmdID>1</CmdID><Item><Target><LocURI>/test</LocURI></Target><Source><LocURI>/test</LocURI></Source><Meta><Anchor xmlns=\"syncml:metinf\"><Next>Next</Next><Last>last</Last></Anchor></Meta></Item><Data>200</Data></Alert><Final></Final></SyncBody></SyncML>"
        data = syncml.TransportData(datastr, len(datastr), syncml.SML_MIMETYPE_XML, False)

        self.c.Send(None, data)
        while 1:
        	self.sm.Dispatch()

if __name__ == "__main__":
    t = ErrorTest()
    t.run()
