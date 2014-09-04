from InstanceGenerator import InstanceGenerator
from ConfigInstance import ConfigInstance

# Assumptions:
#  - instance_title column = nice name for instances to return


class MultiInstanceGenerator(InstanceGenerator):
    def generate(self, input_datasource):
        instances = []
        for entry in input_datasource:
            try:
                title = entry['instance_title']
            except KeyError:
                title = "n/a"
            instances.append(ConfigInstance(
                values=entry, title=title,
                output=self._template.render(entry)))
        return instances
