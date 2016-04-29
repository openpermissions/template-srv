# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

import os

import pytest
from mock import MagicMock, patch

from template.commands.load_data import cli, do_load_data

FIXTURE_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_do_load_data():
    # Will need to be properly implemented in a real service.
    # DELETE THIS COMMENT IN A REAL SERVICE
    do_load_data(os.path.abspath(os.path.join(FIXTURE_DIR, 'file1')))


@patch('template.commands.load_data.do_load_data')
def test_cli(do_load_data):
    with pytest.raises(SystemExit) as exc:
        cli([os.path.abspath(os.path.join(FIXTURE_DIR, 'file1')),
             os.path.abspath(os.path.join(FIXTURE_DIR, 'file2'))])

    assert do_load_data.call_count == 2
    assert exc.value.code == 0
