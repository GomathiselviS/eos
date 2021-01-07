#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for eos_bgp_af
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
module: eos_bgp_af
short_description: Manages BGP address family resource module
description: This module configures and manages the attributes of BGP AF on Arista
  EOS platforms.
version_added: 1.4.0
author: Gomathi Selvi Srinivasan (@GomathiselviS)
notes:
- Tested against Arista EOS 4.23.0F
- This module works with connection C(network_cli). See the L(EOS Platform Options,eos_platform_options).
options:
    config:
      description: Configurations for BGP address family.
      type: dict
      suboptions:
        aS_number:
          description: Autonomous system number.
          type: str
        address_family: &address_family
          description: Enable address family and enter its config mode
          type: list
          elements: dict
          suboptions:
            afi:
              description: address family.
              type: str
              choices: ['ipv4', 'ipv6', 'evpn']
            af_type:
              description: Address family type for ipv4.
              type: str
              choices: ['labeled_unicast', 'multicast']
            bgp_params:
              description: BGP parameters.
              type: dict
              suboptions:
                additional_paths:
                  description: BGP additional-paths commands
                  type: str
                  choices: ['install', 'send', 'receive'] 
                next_hop_address_family:
                  description: Next-hop address-family configuration
                  type: str
                  choices: ['ipv6']
                next_hop_unchanged:
                  description: Preserve original nexthop while advertising routes to
                         eBGP peers.
                  type: bool
                redistribute_internal:
                  description: Redistribute internal BGP routes.
                  type: bool
                route:
                  description: Configure route-map for route installation.
                  type: str
            graceful_restart:
              description: Enable graceful restart mode.
              type: bool
            neighbor:
              description: Configure routing for a network.
              type: list
              elements: dict
              suboptions:
                address:
                  type: str
                  description: Neighbor address
                peer_group:
                  description: Name of the peer-group.
                  type: str
                activate:
                  description: Activate neighbor in the address family.
                  type: bool
                additional_paths:
                  description: BGP additional-paths commands.
                  type: str
                  choices: ['send', 'receive']
                default_orignate:
                  description: Originate default route to this neighbor.
                  type: dict
                  suboptions:
                    route_map:
                      description: Route map reference.
                      type: str
                    always:
                      descrition: Always originate default route to this neighbor.
                      type: bool
                graceful_restart:
                  description: Enable graceful restart mode.
                  type: bool
                next_hop_address_family:
                  description: Next-hop address-family configuration
                  type: str
                  choices: ['ipv6']
                next_hop_unchanged:
                  description: Preserve original nexthop while advertising routes to
                         eBGP peers.
                  type: bool
                prefix_list:
                  description: Prefix list reference.
                  type: dict
                  suboptions:
                    direction:
                      description: Configure an inbound/outbound prefix-list.
                      type: str
                      choices: ['in', 'out']
                    name:
                      description: prefix list name.
                      type: str
                route_map:
                  description: Route map reference.
                  type: dict
                  suboptions:
                    direction:
                      description: Configure an inbound/outbound route-map.
                      type: str
                      choices: ['in', 'out']
                    name:
                      description: Route map name.
                      type: str
                weight:
                  description: Weight to assign.
                  type: int 
                encapsulation:
                  description: Default transport encapsulation for neighbor. Applicable for evpn address-family.
                  type: dict
                  suboptions:
                    transport:
                      description: MPLS/VXLAN transport.
                      type: str
                      choices: ['mpls', 'vxlan']
                    source_interface:
                      description: Source interface to update BGP next hop address. Applicable for mpls transport.
                      type: str.
            redistribute:
              description: Redistribute routes in to BGP.
              type: list
              elements: dict
              suboptions:         
                protocol:
                  description: Routes to be redistributed.
                  type: str
                  choices: ['isis', 'ospf3', 'dhcp']
                route_map:
                  description: Route map reference.
                  type: str
                isis_level:
                  description: Applicable for isis routes. Specify isis route level.
                  type: str
                  choices: ['level-1', 'level-2', 'level-1-2']
                ospf_route:
                  description: ospf route options.
                  type: str
                  choices: ['internal', 'external', 'nssa_external_1', 'nssa_external_2']  
        vrf:
          description: Configure BGP in a VRF.
          type: list
          elements: dict
          suboptions:
            name:
             description: VRF name.
             type: str
            address_family: *address_family
    running_config:
      description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the EOS device by
        executing the command B(show running-config | section bgp).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
      type: str
    state:
      description:
      - The state the configuration should be left in.
      type: str
      choices: [deleted, merged, overridden, replaced, gathered, rendered, parsed]
      default: merged
EXAMPLES:
- deleted_example_01.txt
- merged_example_01.txt
- overridden_example_01.txt
- replaced_example_01.txt
- gathered_example_01.txt
- rendered_example_01.txt
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.bgp_af.bgp_af import (
    Bgp_afArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.bgp_af.bgp_af import (
    Bgp_af,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Bgp_afArgs.argument_spec,
        mutually_exclusive=[],
        required_if=[],
        supports_check_mode=False
    )

    result = Bgp_af(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
