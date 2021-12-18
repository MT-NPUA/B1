# -*- coding: utf-8 -*-

# __init__.py
#
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
    settings.__init__
    ~~~~~~~~~~~~~~~~~


        Applications need some kind of configuration. There are different
        settings you might want to change depending on the application
        environment like toggling the debug mode, setting the secret key, and
        other such environment-specific things.

        The way Application is designed usually requires the configuration to
        be available when the application starts up. You can hard code the
        configuration in the code, which for many small applications is not
        actually that bad, but there are better ways.

        Independent of how you load your config, there is a config object
        available which holds the loaded configuration values: The config
        attribute of the Application object. This is the place where
        Application itself puts certain configuration values and also where
        extensions can put their configuration values. But this is also where
        you can have your own configuration.




    :copyright: (c) 2021 by Janik Tarverdyan <Janik.Tarverdyan@gmail.com>.
    :license: FDLv1-3, see LICENSE for more details.
"""


import pathlib
from dotenv import load_dotenv


# APPLICATION_ROOT:
#    Inform the application what path it is mounted under by the application /
#    web server. This is used for generating URLs outside the context of a
#    request (inside a request, the dispatcher is responsible for setting
#    SCRIPT_NAME instead; see Application Dispatching for examples of dispatch
#    configuration).
#
#    Will be used for the session cookie path if SESSION_COOKIE_PATH is
#    not set.
#
#    Default: '/'
__BASE__ = pathlib.Path('src')

PATH = dict(
    APPLILCATION_ROOT=__BASE__,
    ENV=__BASE__.parent / '.env',
    SETTINGS=__BASE__.parent / 'core/settings'
)
load_dotenv(dotenv_path=PATH['ENV'].as_posix())
