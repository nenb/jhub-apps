# TODO: Fix this hardcoding
DEFAULT_CMD = ["python", "-m", "jhsingle_native_proxy.main", "--authtype=none"]

# TODO: Fix this hardcoding
BASE_EXAMPLES_PATH = "/Users/aktech/quansight/jhub-apps/jhub_apps/examples"
EXAMPLES_PATH = {
    "panel": f"{BASE_EXAMPLES_PATH}/panel_basic.py",
    "bokeh": f"{BASE_EXAMPLES_PATH}/bokeh_basic.py",
    "streamlit": f"{BASE_EXAMPLES_PATH}/streamlit_app.py",
    "plotlydash": f"{BASE_EXAMPLES_PATH}/plotlydash_app.py",
    "voila": f"{BASE_EXAMPLES_PATH}/voila_basic.ipynb",
    "gradio": f"{BASE_EXAMPLES_PATH}/gradio_basic.py",
}

base_url = "http://127.0.0.1:8000"
origin_host = "127.0.0.1:8000"


COMMANDS = {
    "gradio": {
        "args": [
            "--destport=0",
            "python",
            f'{EXAMPLES_PATH.get("gradio")}',
        ],
    },
    "voila": {
        "args": [
            "--destport=0",
            "python",
            "{-}m",
            "voila",
            f'{EXAMPLES_PATH.get("voila")}',
            "{--}port={port}",
            "{--}no-browser",
            "{--}Voila.server_url=/",
            "{--}Voila.ip=0.0.0.0",
            "{--}Voila.tornado_settings",
            "--debug",
            "allow_origin=" + f"{origin_host}",
            "--progressive",
            "--ready-check-path=/voila/static/",
        ],
    },
    "streamlit": {
        "args": [
            "--destport=0",
            "streamlit",
            "run",
            f'{EXAMPLES_PATH.get("streamlit")}',
            "{--}server.port={port}",
            "{--}server.headless=True",
            "{--}browser.serverAddress=" + f"{origin_host}",
            "{--}browser.gatherUsageStats=false",
        ],
        "debug_args": [],
    },
    "plotlydash": {
        "args": [
            "--destport=0",
            "python",
            "{-}m",
            "plotlydash_tornado_cmd.main",
            f'{EXAMPLES_PATH.get("plotlydash")}',
            "{--}port={port}",
        ],
        "env": {"DASH_REQUESTS_PATHNAME_PREFIX": f"{base_url}/"},
    },
    "bokeh": {
        "args": [
            "--destport=0",
            "python",
            "{-}m",
            "bokeh_root_cmd.main",
            f'{EXAMPLES_PATH.get("bokeh")}',
            "{--}port={port}",
            "{--}allow-websocket-origin=" + f"{origin_host}",
            "{--}prefix=" + f"{base_url}",
            "--ready-check-path=/ready-check",
        ]
    },
    "panel": {
        "args": [
            "--destport=0",
            "python",
            "{-}m",
            "bokeh_root_cmd.main",
            f'{EXAMPLES_PATH.get("panel")}',
            "{--}port={port}",
            "{--}debug",
            "{--}allow-websocket-origin=" + f"{origin_host}",
            "{--}server=panel",
            "{--}prefix=" + f"{base_url}",
            "--ready-check-path=/ready-check",
        ]
    },
    "rshiny": {
        "args": [
            "--destport=0",
            "python",
            "{-}m",
            "rshiny_server_cmd.main",
            f'{EXAMPLES_PATH.get("rshiny")}',
            "{--}port={port}",
        ]
    },
}
