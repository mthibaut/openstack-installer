# Copyright 2015 James Beedy jamesbeedy@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging

from cloudinstall.charms import CharmBase
from cloudinstall.state import CharmState

log = logging.getLogger('cloudinstall.charms.ceilometer_agent')


class CharmCeilometerAgent(CharmBase):

    """ Ceilometer-agent directives """

    charm_name = 'ceilometer-agent'
    charm_rev = 3
    display_name = 'Ceilometer-Agent'
    subordinate = True
    contrib = True
    deploy_priority = 0
    charm_state = CharmState.OPTIONAL

__charm_class__ = CharmCeilometerAgent
