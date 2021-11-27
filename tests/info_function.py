# -*- coding: utf-8 -*-

# info.function.py
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

# -*- coding: utf-8 -*-
"""
    tests.info_function
    ~~~~~~~~~~~~~~~~~~~

    DESCRIPTION

    :copyright: (c) 2021 by YOUR_NAME.
    :license: LICENSE_NAME, see LICENSE for more details.
"""

from ..src.core.settings import base


print(base.PATH.as_posix())

def check_call():
    return 'Import working!'
