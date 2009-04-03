import gtk.gdk
gtk.gdk.threads_init()

import syncml

EVENTS = {
	syncml.SML_MANAGER_SESSION_FLUSH:"SML_MANAGER_SESSION_FLUSH",
	syncml.SML_MANAGER_CONNECT_DONE:"SML_MANAGER_CONNECT_DONE",
	syncml.SML_MANAGER_DISCONNECT_DONE:"SML_MANAGER_DISCONNECT_DONE",
	syncml.SML_MANAGER_TRANSPORT_ERROR:"SML_MANAGER_TRANSPORT_ERROR",
	syncml.SML_MANAGER_SESSION_NEW:"SML_MANAGER_SESSION_NEW",
	syncml.SML_MANAGER_SESSION_FINAL:"SML_MANAGER_SESSION_FINAL",
	syncml.SML_MANAGER_SESSION_END:"SML_MANAGER_SESSION_END",
	syncml.SML_MANAGER_SESSION_ERROR:"SML_MANAGER_SESSION_ERROR",
	syncml.SML_MANAGER_SESSION_WARNING:"SML_MANAGER_SESSION_WARNING"
}

def get_manager_and_transports(client_manager_cb, server_manager_cb):
    c = syncml.Transport(syncml.SML_TRANSPORT_HTTP_CLIENT)
    s = syncml.Transport(syncml.SML_TRANSPORT_HTTP_SERVER)

    cm = syncml.Manager(c)
    cm.SetEventCallback(client_manager_cb)

    sm = syncml.Manager(s)
    sm.SetEventCallback(server_manager_cb)

    return cm,sm,c,s

