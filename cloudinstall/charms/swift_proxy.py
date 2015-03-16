# Copyright 2014 Canonical, Ltd.
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

from cloudinstall.charms import CharmBase, DisplayPriorities
from cloudinstall.state import CharmState


class CharmSwiftProxy(CharmBase):

    """ swift directives """

    charm_name = 'swift-proxy'
    charm_rev = 11
    display_name = 'Swift Proxy'
    display_priority = DisplayPriorities.Storage
    related = [
        ('keystone:identity-service', 'swift-proxy:identity-service'),
        ('glance:image-service', 'swift-proxy:image-service')
    ]
    deploy_priority = 5
    constraints = {'mem': 1024,
                   'root-disk': 8192}
    allow_multi_units = False
    menuable = True
    charm_state = CharmState.OPTIONAL
    depends = ['swift-storage']
    conflicts = ['ceph', 'cinder', 'cinder-ceph', 'ceph-osd', 'ceph-radosgw']

__charm_class__ = CharmSwiftProxy
