# -*- coding: utf-8 -*-

# scheme.py
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
    core.scheme
    ~~~~~~~~~~~

    TODO: DESCRIPTION

    :copyright: (c) 2021 by Janik Tarverdyan <Janik.Tarverdyan@gmail.com>.
    :license: FDLv1-3, see LICENSE.fdl_1-3 for more details.
"""

from .log import Log


class Schema(object):
    """
        Description
    """

    def __init__(self):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass

    def __repr__(self):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass

    def __str__(self):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass

    def __unicode__(self):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass

    def create(self):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass

    def remove(self):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass

    def encrypt(self):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass

    def show(self):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass

    @Log
    def file(self):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass

    @Log.info(**action)
    def info(self):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass


"""
db_users = Schema( Name='Users' )
db_users.create(format='json', table=table_schema)
db_users.encrypt(rsa=4096, autogenerate = True)


@db_users.get(name='admin')
def name():
    pass

db_users.init()
"""
