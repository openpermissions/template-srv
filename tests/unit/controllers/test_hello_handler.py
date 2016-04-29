# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.


from mock import MagicMock, patch

from template.controllers.hello_handler import HelloHandler

from tornado.escape import json_encode
from template import __version__


@patch('tornado.process')
def test_get_service_status(process):
    hello = HelloHandler(MagicMock(), MagicMock(), version=__version__)
    hello.finish = MagicMock()

    process.task_id = MagicMock(return_value=0)

    # MUT
    hello.get()
    msg = {"service_name": 
           "Open Permissions Platform Template Service",
           "message": "Hello World",
           "version": "{}".format(__version__)}

    hello.finish.assert_called_once_with({'status': 200, 'data': msg})
