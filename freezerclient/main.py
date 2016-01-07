"""
Copyright 2016 Ericsson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Freezer Command Line Interface
"""

from freezerclient import client
from oslo_config import cfg

CONF = cfg.CONF

FREEZER_SERVICE_TYPE = 'backup'


def freezer_main(client):
    if CONF.action is None:
        CONF.print_help()
        return 65  # os.EX_DATAERR

    apiclient = None
    verify = True
    if CONF.insecure:
        verify = False

    if CONF.no_api is False:
        try:
            apiclient = client.Client(opts=CONF, verify=verify)
            if CONF.client_id:
                apiclient.client_id = CONF.client_id
        except Exception as e:
            LOG.error(e)
            print e
            sys.exit(1)
    else:
        if winutils.is_windows():
            print("--no-api mode is not available on windows")
            return 69  # os.EX_UNAVAILABLE


def main():
    freezer_main(client)

