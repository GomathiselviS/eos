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
        as_number:
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
            safi:
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
                peer:
                  type: str
                  description: Neighbor address/ peer-group name.
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
            network:
              description: configure routing for network.
              type: list
              elements: dict
              suboptions:
                route_map:
                  description: Route map reference.
                  type: str
                address:
                  description: network address.
                  type: str
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
            route_target:
              description: Route target
              type: dict
              suboptions:
                mode:
                  description: route import or route export.
                  type: str
                  choices: ['both', 'import', 'export']
                target:
                  description: route target
                  type: str
            vrf:
              description: name of the VRF in which BGP will be configured.
              type: str
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

"""

EXAMPLES = """

# Using merged

# Before state

# veos(config)#show running-config | section bgp
# veos(config)#

  - name: Merge provided configuration with device configuration
    arista.eos.eos_bgp_af:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv4"
            redistribute:
              - protocol: "ospf3"
                ospf_route: "external"
            network:
              - address: "1.1.1.0/24"
              - address: "1.5.1.0/24"
                route_map: "MAP01"
          - afi: "ipv6"
            bgp_params:
              additional_paths: "receive"
            neighbor:
              - peer: "peer2"
                default_originate:
                  always: True
          - afi: "ipv6"
            redistribute:
              - protocol: "isis"
                isis_level: "level-2"
            route_target: 
              mode: "export"
              target: "33:11"
            vrf: "vrft"
            
      state: merged

# After state:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000 
#    neighbor 1.1.1.1 maximum-routes 12000 
#    !
#    address-family ipv4
#       neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospf3 match external
#    !
#    address-family ipv6
#       bgp additional-paths receive
#       neighbor peer2 activate
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv6
#          route-target export 33:11
#          redistribute isis level-2
# veos(config-router-bgp)#

# Module Execution:

# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     }
#                 ],
#                 "route_target": {
#                     "mode": "export",
#                     "target": "33:11"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "router bgp 10",
#         "address-family ipv4",
#         "redistribute ospf3 match external",
#         "network 1.1.1.0/24",
#         "network 1.5.1.0/24 route-map MAP01",
#         "exit",
#         "address-family ipv6",
#         "neighbor peer2 default-originate always",
#         "bgp additional-paths receive",
#         "exit",
#         "vrf vrft",
#         "address-family ipv6",
#         "redistribute isis level-2",
#         "route-target export 33:11",
#         "exit",
#         "exit"
#     ],

# Using replaced:

# Before State:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000 
#    neighbor 1.1.1.1 maximum-routes 12000 
#    !
#    address-family ipv4
#       neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospf3 match external
#    !
#    address-family ipv6
#       bgp additional-paths receive
#       neighbor peer2 activate
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv6
#          route-target export 33:11
#          redistribute isis level-2
# veos(config-router-bgp)#
# 

  - name: Replace
    arista.eos.eos_bgp_af:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv6"
            vrf: "vrft"
            redistribute:
              - protocol: "ospf3"
                ospf_route: "external"
          - afi: "ipv6"
            redistribute:
              - protocol: "isis"
                isis_level: "level-2"
      state: replaced

# After State:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000 
#    neighbor 1.1.1.1 maximum-routes 12000 
#    !
#    address-family ipv4
#       neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospf3 match external
#    !
#    address-family ipv6
#       neighbor peer2 default-originate always
#       redistribute isis level-2
#    !
#    vrf vrft
#       address-family ipv6
#          redistribute ospf3 match external
# veos(config-router-bgp)#
# 
# 
# # Module Execution:
# 
#     "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "neighbor": [
#                     {
#                         "activate": true,
#                         "peer": "1.1.1.1"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ],
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "neighbor": [
#                     {
#                         "activate": true,
#                         "peer": "1.1.1.1"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "activate": true,
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     }
#                 ],
#                 "route_target": {
#                     "mode": "export",
#                     "target": "33:11"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "changed": true,
#     "commands": [
#         "router bgp 10",
#         "vrf vrft",
#         "address-family ipv6",
#         "redistribute ospf3 match external",
#         "no redistribute isis level-2",
#         "no route-target export 33:11",
#         "exit",
#         "exit",
#         "address-family ipv6",
#         "redistribute isis level-2",
#         "no neighbor peer2 activate",
#         "no bgp additional-paths receive",
#         "exit"
#     ],

# Using overridden (overriding af at global context):
# Before state:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000 
#    neighbor 1.1.1.1 maximum-routes 12000 
#    !
#    address-family ipv4
#       neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospf3 match external
#    !
#    address-family ipv6
#       neighbor peer2 default-originate always
#       redistribute isis level-2
#    !
#    vrf vrft
#       address-family ipv6
#          redistribute ospf3 match external
# veos(config-router-bgp)#

- name: Overridden
    arista.eos.eos_bgp_af:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv4"
            bgp_params:
              additional_paths: "receive"
            neighbor:
              - peer: "peer2"
                default_originate:
                  always: True
      state: overridden

# After State:
# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000 
#    neighbor 1.1.1.1 maximum-routes 12000 
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv6
#          redistribute ospf3 match external
# veos(config-router-bgp)#
# 
# Module Execution:
# 
# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ],
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "neighbor": [
#                     {
#                         "activate": true,
#                         "peer": "1.1.1.1"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ],
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "changed": true,
#     "commands": [
#         "router bgp 10",
#         "address-family ipv4",
#         "no redistribute ospf3 match external",
#         "no network 1.1.1.0/24",
#         "no network 1.5.1.0/24 route-map MAP01",
#         "neighbor peer2 default-originate always",
#         "no neighbor 1.1.1.1 activate",
#         "bgp additional-paths receive",
#         "exit",
#         "no address-family ipv6"
#     ],

# using Overridden (overridding af in vrf context):

# Before State:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000 
#    neighbor 1.1.1.1 maximum-routes 12000 
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       no neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospf3 match external
#    !
#    address-family ipv6
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv6
#          route-target export 33:11
#          redistribute isis level-2
#          redistribute ospf3 match external
# veos(config-router-bgp)#


- name: Overridden
    arista.eos.eos_bgp_af:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv4"
            bgp_params:
              additional_paths: "receive"
            neighbor:
              - peer: "peer2"
                default_originate:
                  always: True
            vrf: vrft
      state: overridden

# After State:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000 
#    neighbor 1.1.1.1 maximum-routes 12000 
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospf3 match external
#    !
#    address-family ipv6
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv4
#          bgp additional-paths receive
# veos(config-router-bgp)#
# 
# Module Execution:
# 
# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     },
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ],
#                 "route_target": {
#                     "mode": "export",
#                     "target": "33:11"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "changed": true,
#     "commands": [
#         "router bgp 10",
#         "vrf vrft",
#         "address-family ipv4",
#         "neighbor peer2 default-originate always",
#         "bgp additional-paths receive",
#         "exit",
#         "exit",
#         " vrf vrft",
#         "no address-family ipv6"
#     ],

# Using Deleted:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000 
#    neighbor 1.1.1.1 maximum-routes 12000 
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       no neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospf3 match external
#    !
#    address-family ipv6
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv4
#          bgp additional-paths receive
# veos(config-router-bgp)#

- name: Delete
    arista.eos.eos_bgp_af:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv6"
            vrf: "vrft"
          - afi: "ipv6"
      state: deleted

# After State:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000 
#    neighbor 1.1.1.1 maximum-routes 12000 
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       no neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospf3 match external
#    !
#    vrf vrft
#       address-family ipv4
#          bgp additional-paths receive
# veos(config-router-bgp)#
# 
# Module Execution:
# 
# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },

# Using parsed:

# parsed_bgp_af.cfg :

# router bgp 10
#    neighbor n2 peer-group
#    neighbor n2 next-hop-unchanged
#    neighbor n2 maximum-routes 12000
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000
#    network 1.1.1.0/24
#    network 1.5.1.0/24 route-map MAP01
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       redistribute ospf3 match external
#    !
#    address-family ipv6
#       no bgp additional-paths receive
#       neighbor n2 next-hop-unchanged
#       redistribute isis level-2
#    !
#    vrf bgp_10
#       ip access-group acl01
#       ucmp fec threshold trigger 33 clear 22 warning-only
#       !
#       address-family ipv4
#          route-target import 20:11
#    !
#    vrf vrft
#       address-family ipv4
#          bgp additional-paths receive
#       !
#       address-family ipv6
#          redistribute ospf3 match external

  - name: parse configs
    arista.eos.eos_bgp_af:
      running_config: "{{ lookup('file', './parsed_bgp_af.cfg') }}"
      state: parsed

# Module Execution:
# "parsed": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "neighbor": [
#                     {
#                         "next_hop_unchanged": true,
#                         "peer": "n2"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv4",
#                 "route_target": {
#                     "mode": "import",
#                     "target": "20:11"
#                 },
#                 "vrf": "bgp_10"
#             },
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "vrf": "vrft"
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ],
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     }
# }

# Using gathered:

# Device config:
# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer-group
#    neighbor peer2 maximum-routes 12000 
#    neighbor 1.1.1.1 maximum-routes 12000 
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       no neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospf3 match external
#    !
#    vrf vrft
#       address-family ipv4
#          bgp additional-paths receive
# veos(config-router-bgp)#

  - name: gather configs
    arista.eos.eos_bgp_af:
      state: gathered

# Module Execution:
# "gathered": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospf3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },

# using rendered:

  - name:  Render
    arista.eos.eos_bgp_af:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv4"
            redistribute:
              - protocol: "ospf3"
                ospf_route: "external"
            network:
              - address: "1.1.1.0/24"
              - address: "1.5.1.0/24"
                route_map: "MAP01"
          - afi: "ipv6"
            bgp_params:
              additional_paths: "receive"
            neighbor:
              - peer: "peer2"
                default_originate:
                  always: True
          - afi: "ipv6"
            redistribute:
              - protocol: "isis"
                isis_level: "level-2"
            route_target:
              mode: "export"
              target: "33:11"
            vrf: "vrft"

      state: rendered

# Module Execution:

# "rendered": [
#         "router bgp 10",
#         "address-family ipv4",
#         "redistribute ospf3 match external",
#         "network 1.1.1.0/24",
#         "network 1.5.1.0/24 route-map MAP01",
#         "exit",
#         "address-family ipv6",
#         "neighbor peer2 default-originate always",
#         "bgp additional-paths receive",
#         "exit",
#         "vrf vrft",
#         "address-family ipv6",
#         "redistribute isis level-2",
#         "route-target export 33:11",
#         "exit",
#         "exit"
#     ]
# 

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
