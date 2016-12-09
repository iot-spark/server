from iotspark.commands.run_local import RunLocal
from iotspark.commands.run_remote import RunRemote


class Command(object):
    """
    Initializes a certain sub command
    """
    __subcmd = {
        RunLocal.name: RunLocal,
        RunRemote.name: RunRemote
    }

    @staticmethod
    def init(name):
        """
        Create a certain instance by name
        :param name: sub command name
        :return DriverBase
        """
        sub_command = Command.__subcmd.get(name)

        if sub_command is None:
            raise NotImplementedError("The requested action '{0}' has not "
                                      "been implemented".format(name))

        return sub_command()

    @staticmethod
    def init_sub_commands(sub_parser):
        """
        Creates sub commands
        :param sub_parser: sub parser
        :return:
        """
        RunLocal.init_args(sub_parser)
        RunRemote.init_args(sub_parser)
