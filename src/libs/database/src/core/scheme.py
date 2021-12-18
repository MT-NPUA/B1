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

    A schema is the structure behind data organization. It is a visual
    representation of how different table relationships enable the schema’s
    underlying mission business rules for which the database is created.s

    In a schema diagram, all database tables are designated with unique columns
    and special features, e.g., primary/foreign keys or not null, etc. Formats
    and symbols for expression are universally understood, eliminating the
    possibility of confusion. The table relationships also are expressed via a
    parent table’s primary key lines when joined with the child table’s
    corresponding foreign
    keys.

    Schema diagrams have an important function because they force database
    developers to transpose ideas to paper. This provides an overview of the
    entire database, while facilitating future database administrator work.

    Database (DB) refers to schema as a user collection of database
    objects. The schema and user names are the same but function quite
    distinctly; i.e., a user may be deleted or reassigned to another user while
    its collection of objects (schema) within the database remains intact.
"""


from .log import Log


class Schema(object):
    """Description
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
    def file(self, name: str, datetime: 'date type'):
        """Description

        @param param:  Description
        @type  param:  Type

        @return:  Description
        @rtype :  Type

        @raise e:  Description
        """
        pass

    @Log.info(**action)
    def dump(self):
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
