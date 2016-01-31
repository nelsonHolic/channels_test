# In routing.py
channel_routing = {
    "websocket.connect": "backend.applications.web_apps.channels_app.consumers.ws_add",
    "websocket.keepalive": "backend.applications.web_apps.channels_app.consumers.ws_add",
    "websocket.receive": "backend.applications.web_apps.channels_app.consumers.ws_message",
    "websocket.disconnect": "backend.applications.web_apps.channels_app.consumers.ws_disconnect",
}
