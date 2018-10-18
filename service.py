import service_utils
import os


class Service:

    # Defines service default paths
    CWD = os.getcwd()
    CONFIG_PATH = CWD + "/config"
    SERVICE_PATH = CWD + "/service"
    SPEC_PATH = SERVICE_PATH + "/service_spec"

    # TODO: Everything from here on
    def __init__(self, service_info):
        """Checks dependencies, service information and fills instance attributes."""
        # Checks that the dependencies are installed
        # service_utils.check_dependencies()

        # Checks that the user provided info is correct
        # self._check_input_info(service_info)

        # Fill instance attributes
        # self.service_info = self._fill_service_parameters(service_info)

        print(service_info)  # just so pycharm stops complaining :)
        pass

    def _check_input_info(self, service_info):
        """Checks that (user provided) information is valid."""
        pass

    def _fill_service_parameters(self, service_info):
        """Fills service object attributes with (user provided) information from service_info."""
        pass

    def create_service_json(self):
        """Creates service json file for service registration."""
        pass

    def create_proto_file(self):
        """Creates protobuf message file."""
        pass

    def compile_proto_file(self):
        """Compiles protobuf message file."""
        pass


if __name__ == '__main__':
    service_utils.test()
    service = Service("a")
