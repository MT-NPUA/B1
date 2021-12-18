# -*- coding: utf-8 -*-

# base.py
#
# TODO: write code of conduct for the settings
#
# Copyright © 2021 Janik Tarverdyan <Janik.Tarverdyan@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
    settings.base
    ~~~~~~~~~~~~~

    DESCRIPTION

    :copyright: (c) 2021 by Janik Tarverdyan <Janik.Tarverdyan@gmail.com>.
    :license: FDLv1-3, see LICENSE for more details.
"""


import os
from . import PATH


# SECRET_KEY: A secret key that will be used for securely signing the session
#             cookie and can be used for any other security related needs by
#             extensions or your application. It should be a long random bytes
#             or str. For example, copy the output of this to your config:
#
def SECRET_KEY(): return ''.join(item for item in os.urandom(4096).hex())


# ENV:  What environment the app is running in. Flask and extensions may enable
#       behaviors based on the environment, such as enabling debug mode.
#       The env attribute maps to this config key. This is set by the APP_ENV
#       environment variable and may not behave as expected if set in code. Do
#       not enable development when deploying in production.
#
if not os.getenv('ENV'):
    APP_ENV = 'production'
else:
    APP_ENV = os.getenv('ENV').lower()


# DEBUG: Whether debug mode is enabled. When using flask run to start the
#        development server, an interactive debugger will be shown for
#        unhandled exceptions, and the server will be reloaded when code
#        changes. The debug attribute maps to this config key. This is enabled
#        when ENV is 'development' and is overridden by the APP_DEBUG
#        environment variable. It may not behave as expected if set in code.
#        Do not enable debug mode when deploying in production. Default: True
#        if ENV is 'development', or False otherwise.
#
if os.getenv('APP_DEBUG') and \
        os.getenv('APP_DEBUG').lower() == 'production':
    DEBUG = False
else:
    DEBUG = True


# TESTING:  Enable testing mode. Exceptions are propagated rather than handled
#           by the the app’s error handlers. Extensions may also change their
#           behavior to facilitate easier testing. You should enable this in
#           your own tests. Default: False
#
if not os.getenv('TESTING'):
    TESTING = False
