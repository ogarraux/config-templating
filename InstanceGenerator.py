import shutil
import os
import tempfile
from jinja2 import Environment, FileSystemLoader


class InstanceGenerator:
    def __init__(self, template_file_path):
        self._temp_dir = tempfile.mkdtemp()
        template_file_name = os.path.split(template_file_path)[1]
        shutil.copy(template_file_path, "{td}/{tfn}".format(
            td=self._temp_dir, tfn=template_file_name))
        self._template_env = Environment(
            loader=FileSystemLoader(self._temp_dir))
        self._template = self._template_env.get_template(template_file_name)

    def __del__(self):
        shutil.rmtree(self._temp_dir)

    def generate(self, input_datasource):
        pass
