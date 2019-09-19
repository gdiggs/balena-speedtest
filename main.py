import datadog
import json
import os
import socket

datadog.initialize(api_key=os.environ['DATADOG_API_KEY'])

raw = os.popen('speedtest --json').read()
result = json.loads(raw)

ping = result['ping']
download = result['download']
upload = result['upload']

hostname = os.environ.get('BALENA_DEVICE_NAME_AT_INIT', socket.gethostname())

print("Speedtest complete. Ping: {} Download: {} Upload: {}".format(ping, download, upload))

datadog.api.Metric.send([
    {
        'metric': 'speedtest.ping',
        'points': ping,
        'host': hostname,
    },
    {
        'metric': 'speedtest.download',
        'points': download,
        'host': hostname,
    },
    {
        'metric': 'speedtest.upload',
        'points': upload,
        'host': hostname,
    },
])
