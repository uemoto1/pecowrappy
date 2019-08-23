#!/usr/bin/env python
#
#  Copyright 2017-2019 M.Uemoto
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from subprocess import Popen, PIPE

# Check 'peco' command is already installed.
peco_error = OSError("peco command is not installed")
try:
    from shutil import which
    if which('peco') is None:
        raise peco_error
except(ImportError):
    from distutils.spawn import find_executable
    if find_executable('peco') is None:
        raise peco_error

# peco function
def peco(options, query=None, rcfile=None, buffer_size=None, 
            initial_index=None,initial_matcher=None, 
            initial_filter=None, prompt=None, layout=None,  
            select_1=False):
    """Call peco command.

    Parameters
    ----------
    options : string, list, tuple, set, ... and any iterable object
    query : string, optional
        Specifies the default query to be used upon startup.
    rcfile : string, optional
        Specifies a configuration file of peco.
    buffer_size : int, optional
        Specifies a limits of the buffer size.
    initial_index : int, optional
        Specifies the initial line position upon start up.
    initial_matcher : string, optional
        Specifies the initial filter to use upon start up,
        should be one of
            - 'IgnoreCase'
            - 'CaseSensitive'
            - 'SmartCase'
            - 'Regexp'
            - 'Fuzzy'
        If not given, IgnoreCase is used by default. 
    initial_filter : string, optional
        Specifies the query line's prompt string.
    prompt : string, optional
    layout : string, optional
        Specifies the display layout, which should be one of
            - 'top-down'
            - 'bottom-up'
        If not given, IgnoreCase is used by default. 
    select_1: boolean
    """

    if type(options) is str:
        inp = options
    else:
        inp = '\n'.join(map(str, list(options)))
    
    command = ['peco']

    if query:
        command += ['--query={}'.format(query)]
    if rcfile:
        command += ['--rcfile={}'.format(rcfile)]
    if buffer_size:
        command += ['--buffer-size={}'.format(buffer_size)]
    if initial_index:
        command += ['--initial-index={}'.format(initial_index)]
    if initial_matcher:
        command += ['--initial-matcher={}'.format(initial_matcher)]
    if initial_filter:
        command += ['--initial-filter={}'.format(initial_filter)]
    if initial_filter:
        command += ['--initial-filter={}'.format(initial_filter)]
    if prompt:
        command += ['--prompt={}'.format(prompt)]
    if layout:
        command += ['--layout={}'.format(layout)]
    if select_1:
        command += ['--select-1']
    
    proc = Popen(command, stdin=PIPE, stdout=PIPE)
    out, err = proc.communicate(inp)
    
    return out.strip()

