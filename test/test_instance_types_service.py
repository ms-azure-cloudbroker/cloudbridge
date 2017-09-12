from test import helpers

from test.helpers import ProviderTestBase
from test.helpers import standard_interface_tests as sit

import six


class CloudInstanceTypesServiceTestCase(ProviderTestBase):

    @helpers.skipIfNoService(['compute.instance_types'])
    def test_instance_type_properties(self):
        for inst_type in self.provider.compute.instance_types:
            sit.check_repr(self, inst_type)
            self.assertIsNotNone(
                inst_type.id,
                "InstanceType id must have a value")
            self.assertIsNotNone(
                inst_type.name,
                "InstanceType name must have a value")
            self.assertTrue(
                inst_type.family is None or isinstance(
                    inst_type.family,
                    six.string_types),
                "InstanceType family family be None or a"
                " string but is: {0}".format(inst_type.family))
            self.assertTrue(
                inst_type.vcpus is None or (
                    isinstance(inst_type.vcpus, six.integer_types) and
                    inst_type.vcpus >= 0),
                "InstanceType vcpus family be None or a positive integer")
            self.assertTrue(
                inst_type.ram is None or inst_type.ram >= 0,
                "InstanceType ram must be None or a positive number")
            self.assertTrue(
                inst_type.size_root_disk is None or
                inst_type.size_root_disk >= 0,
                "InstanceType size_root_disk must be None or a positive number"
                " but is: {0}".format(inst_type.size_root_disk))
            self.assertTrue(
                inst_type.size_ephemeral_disks is None or
                inst_type.size_ephemeral_disks >= 0,
                "InstanceType size_ephemeral_disk must be None or a positive"
                " number")
            self.assertTrue(
                isinstance(inst_type.num_ephemeral_disks,
                           six.integer_types) and
                inst_type.num_ephemeral_disks >= 0,
                "InstanceType num_ephemeral_disks must be None or a positive"
                " number")
            self.assertTrue(
                inst_type.size_total_disk is None or
                inst_type.size_total_disk >= 0,
                "InstanceType size_total_disk must be None or a positive"
                " number")
            self.assertTrue(
                inst_type.extra_data is None or isinstance(
                    inst_type.extra_data, dict),
                "InstanceType extra_data must be None or a dict")

    @helpers.skipIfNoService(['compute.instance_types'])
    def test_instance_types_standard(self):
        """
        Searching for an instance by name should return an
        InstanceType object and searching for a non-existent
        object should return an empty iterator
        """
        instance_type_name = helpers.get_provider_test_data(
            self.provider,
            "instance_type")
        inst_type = self.provider.compute.instance_types.find(
            name=instance_type_name)[0]

        sit.check_standard_behaviour(
            self, self.provider.compute.instance_types, inst_type)
