import os
import settings

def annotate(title, text, tags=None):
    influxdb_url = settings.cluster.get('influxdb_url')
    if influxdb_url:
        os.system('curl -s -X POST %s/write?db=collectd --data-binary \'events title="%s",text="%s"\'' % (influxdb_url, title, text or ""))
