from cloudbridge.cloud.providers.azure.integration_test import helpers

from cloudbridge.cloud.providers.azure. \
    integration_test.helpers import ProviderTestBase


class AzureIntegrationInstanceTypeServiceTestCase(ProviderTestBase):
    @helpers.skipIfNoService(['compute.images'])
    def test_azure_instance_type_service(self):
        instance_type_list = self.provider.compute.instance_types.list()
        print("List Instance Types - " + str(instance_type_list))
        print("List Instance Type Properties - ")
        print("Name - " + str(instance_type_list[0].name))
        print("Id - " + str(instance_type_list[0].id))
        print("vcpus - " + str(instance_type_list[0].vcpus))
        print("size_root_disk - " +
              str(instance_type_list[0].size_root_disk))
        print("ram - " + str(instance_type_list[0].ram))
        print("size_ephemeral_disks - " +
              str(instance_type_list[0].size_ephemeral_disks))
        print("num_ephemeral_disks - " +
              str(instance_type_list[0].num_ephemeral_disks))
        self.assertTrue(instance_type_list.total_results > 0)

        # Test find
        inst_type = self.provider.compute.instance_types.find(
            name="Standard_DS1_v2")[0]
        print(str(inst_type))
