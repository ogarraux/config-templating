from InstanceGenerator import InstanceGenerator
from ConfigInstance import ConfigInstance


class SingleInstanceGenerator(InstanceGenerator):
    def generate(self, input_datasource):
        values_dict = {"values": input_datasource}
        return [(ConfigInstance(
            values=values_dict,
            output=self._template.render(values_dict)))]
