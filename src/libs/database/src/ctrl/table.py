# -*- coding: utf-8 -*-

# table.py
#
# TODO: code of couduct
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
    ctrl.table
    ~~~~~~~~~~

    DESCRIPTION

    :copyright: (c) 2021 by Janik Tarverdyan <Janik.Tarverdyan@gmail.om>.
    :license: FDLv1-3, see LICENSE for more details.
"""


class Table:
    # Permissions of the class
    public_EXP = 'Public expressoin for the class'
    _private_EXP = 'Private expression for the class'
    __protected_EXP = 'Protected expression for the class'

    def Any_Function():
        # code of any function
        pass

    @classmethod
    def get():
        # code of class method
        pass

    @staticmethod
    def static_method():
        # code of static method
        pass

    @property
    def Property():
        # code of property
        pass
