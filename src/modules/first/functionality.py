# -*- coding: utf-8 -*-

# functionality.py
#
#
# Code of conduct: self
#
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
# tempor incididunt ut labore et dolore magnam aliquam quaerat voluptatem. ut
# enim medicorum scientiam non ipsius artis, sed bonae valetudinis causa
# probamus, et gubernatoris ars, quia bene navigandi rationem habet, utilitate,
# non arte laudatur, sic sapientia, quae ars vivendi putanda est, non
# expeteretur, si nihil efficeret; nunc expetitur, quod est tamquam artifex
# conquirendae et comparandae voluptatis -- Quam.ne line to give the program's
# name and a brief description.
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
    first.functionality
    ~~~~~~~~~~~~~~~~~~~

    In vita tantopere quaerendum quam cum omnia in philosophia, tum id,
    quod maxime placeat, facere possimus, omnis voluptas assumenda est,
    omnis dolor repellendus. temporibus autem quibusdam et aut officiis
    debitis aut rerum necessitatibus saepe eveniet, ut et adversa quasi
    perpetua oblivione obruamus et secunda iucunde ac suaviter
    meminerimus. sed cum ea, quae dices, libenter assentiar. Probabo,
    inquit, modo ista sis aequitate, quam ostendis. sed uti oratione
    perpetua malo.



    :copyright: (c) 2021 by YOUR_NAME.
    :license: LICENSE_NAME, see LICENSE for more details.
"""


""" Description about function of module

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minima
    veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam,
    nisi ut aliquip ex ea commodi consequatur? quis autem vel eum iure
    reprehenderit, qui in una virtute ponunt et splendore nominis capti quid
    natura desideret. tum vero, si.

    Autem si qui e nostris aliter existimant, quos quidem video esse multos,
    sed imperitos --, quamqua autem et laetitiam nobis voluptas animi et
    corporis voluptatibus, videtisne quam nihil molestiae consequatur.
    Disciplinam placet an de un voluptate quaeri, de qua Epicurus quidem ita
    dicit, omnium rerum, quas ad beate vivendum sapientia comparaverit,
    nihil esse prosperum nisi voluptatem, nihil asperum nisi dolorem, de.


@param a:  Description
@type  a:  int

@param b:  Description
@type  b:  int

@param c:  Description
@type  c:  int

@return:  Description
@rtype :  float

@raise e:  Description
"""


def sqr_exqu(a: int,
             b: int,
             c: int) -> float:
    """ Title of the function

         firmitatem animi nec mortem nec dolorem
         timentis, quod mors sensu careat, dolor
         in longinquitate levis, in gravitate.
    """

    d = None
    if a != 0:
        d = b**2 - 4*a*c
        if d >= 0:
            x_1 = (-b + d**0.5)/2*a
            x_2 = (-b - d**0.5)/2*a

            return f"""
                        X_1: {x_1}
                        X_2: {x_2}
                    """
        else:
            return "None SQRT"

    elif a == 0 and b == 0 and c != 0:
        return None

    elif a == b == c == 0:
        return f"x in range(-{float('inf')}, +{float('inf')})"
