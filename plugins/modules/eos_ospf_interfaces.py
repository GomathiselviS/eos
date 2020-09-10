#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
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
The module file for eos_ospf_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: eos_ospf_interfaces
version_added: 1.1.0
short_description: OSPF Interfaces Resource Module.
description:
- This module manages OSPF configuration of interfaces on devices running Arista EOS.
author: Gomathi Selvi Srinivasan (@GomathiselviS)
options:
  config:
    description: A list of OSPF configuration for interfaces.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name/Identifier of the interface.
        type: str
        required: True
      address_family:
        description:
        - OSPF settings on the interfaces in address-family context.
        type: list
        elements: dict
        suboptions:
          afi:
            description:
            - Address Family Identifier (AFI) for OSPF settings on the interfaces.
            type: str
            choices: ['ipv4', 'ipv6']
            required: True
          area:
            description:
            - Area associated with interface.
            - Valid only when afi = ipv4.
            type: dict
            suboptions:
              area_id:
                description:
                - Area ID as a decimal or IP address format.
                type: str
                required: True
          authentication_v2:
            description:
            - Authentication settings on the interface.
            - Valid only when afi = ipv4.
            type: dict
            suboptions:
              message_digest:
                description:
                - Use message-digest authentication.
                type: bool
              set:
                description:
                - Enable authentication on the interface.
                type: bool
          authentication_v3:
            description:
            - Authentication settings on the interface.
            - Valid only when afi = ipv6.
            type: dict
            suboptions:
              spi:
                description: IPsec Security Parameter Index.
                type: int
              algorithm:
                description: Encryption alsgorithm.
                type: str
                choices: ["md5", "sha1"]
              keytype:
                description:
                - Specifies if an unencrypted/hidden follows.
                - 0 denotes unencrypted key.
                - 7 denotes hidden key.
                type: str
              passphrase:
                description: Passphrase String for deriving keys for authentication and encryption.
                type: str
              key:
                description: 128 bit MD5 key or 140 bit SHA1 key.
                type: str
          authentication_key:
            description:
            - Configure the authentication key for the interface.
            - Valid only when afi = ipv4.
            type: dict
            suboptions:
              encryption:
                description:
                - 0 Specifies an UNENCRYPTED authentication key will follow.
                - 7 Specifies a proprietry encryption type.`
                type: str
              key:
                description:
                - password (up to 8 chars).
                type: str
          bfd:
            description: Enable BFD.
            type: bool
          cost:
            description:
            - metric associated with interface.
            type: int
          dead_interval:
            description:
            - Time interval to detect a dead router.
            type: int
          encryption_v3:
            description:
            - Authentication settings on the interface.
            - Valid only when afi = ipv6.
            type: dict
            suboptions:
              spi:
                description: IPsec Security Parameter Index.
                type: int
              encryption:
                description: encryption type.
                choices: ["3des-cbc", "aes-128-cbc", "aes-192-cbc", "aes-256-cbc", "null"]
              algorithm:
                description: algorithm.
                type: str
                choices: ["md5", "sha1"]
              keytype:
                description:
                - Specifies if an unencrypted/hidden follows.
                - 0 denotes unencrypted key.
                - 7 denotes hidden key.
                type: str
              passphrase:
                description: Passphrase String for deriving keys for authentication and encryption.
                type: str
              key:
                description: 12
          hello_interval:
            description:
            - Timer interval between transmission of hello packets.
            type: int
          ip_params:
            description:
            - Specify parameters for IPv4/IPv6.
            - Valid only when afi = ipv6.
            type: list
            elements: dict
            subotions:
              afi:
                description:
                - Address Family Identifier (AFI) for OSPF settings on the interfaces.
                type: str
                choices: ['ipv4', 'ipv6']
                required: True
              area:
                description:
                - Area associated with interface.
                - Valid only when afi = ipv4.
                type: dict
                suboptions:
                  area_id:
                    description:
                    - Area ID as a decimal or IP address format.
                    type: str
                    required: True
              bfd:
                description: Enable BFD.
                type: bool
              cost:
                description:
                - metric associated with interface.
                type: int
              dead_interval:
                description:
                - Time interval to detect a dead router.
                type: int
              hello_interval:
                description:
                - Timer interval between transmission of hello packets.
                type: int
              mtu_ignore:
                description:
                - if True, Disable MTU check for Database Description packets.
                type: bool
              network:
                description:
                - Interface type.
                type: str
                default: "point-to-point"
              priority:
                description:
                - Interface priority.
                type: int
              retransmit_interval:
                description:
                - LSA retransmission interval.
                type: int
              passive_interface:
                description:
                - Suppress routing updates in an interface.
                type: bool
              transmit_delay:
                description:
                - LSA transmission delay.
                type: int
          message_digest_key:
            description:
            - Message digest authentication password (key) settings.
            type: dict
            suboptions:
              key_id:
                description:
                - Key ID.
                type: int
              encryption:
                description:
                - 0 Specifies an UNENCRYPTED ospf password (key) will follow.
                - 7 Specifies a proprietry encryption type.
                type: str
              key:
                description:
                - Authentication key (upto 16 chars).
                type: str
          mtu_ignore:
            description:
            - if True, Disable MTU check for Database Description packets.
            type: bool
          network:
            description:
            - Interface type.
            type: str
            default: "point-to-point"
          passive_interface:
            description:
            - Suppress routing updates in an interface.
            - Valid only when afi = ipv6.
            type: bool
          priority:
            description:
            - Interface priority.
            type: int
          retransmit_interval:
            description:
            - LSA retransmission interval.
            type: int
          shutdown:
            description:
            - Shutdown OSPF on this interface.
            type: bool
          transmit_delay:
            description:
            - LSA transmission delay.
            type: int
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the EOS device by
      executing the command B(show running-config | section interface).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str

  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - parsed
    - rendered
    default: merged
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.ospf_interfaces.ospf_interfaces import (
    Ospf_interfacesArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.ospf_interfaces.ospf_interfaces import (
    Ospf_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Ospf_interfacesArgs.argument_spec,
        mutually_exclusive=[],
        required_if=[],
        supports_check_mode=False,
    )

    result = Ospf_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
