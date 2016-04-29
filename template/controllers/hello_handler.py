# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

"""API hello handler. Returns hello world when endpoint hit.
"""
import logging

from tornado.escape import json_encode

from koi import base


class HelloHandler(base.BaseHandler):
    """Responsible for providing basic inf. on the service, like:
    + its name
    + current minor version
    """

    def initialize(self, **kwargs):
        try:
            self.version = kwargs['version']
        except KeyError:
            raise KeyError('version is required')

    def get(self):
        """Respond with JSON containing service name and current minor version
        of the service.
        """
        msg = {"service_name":
               "Open Permissions Platform Template Service",
               "message": "Hello World",
               "version": "{}".format(self.version)}
        logging.info("send back msg %s", msg)
        self.finish({'status': 200, 'data': msg})
