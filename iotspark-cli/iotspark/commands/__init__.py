from .run import RunCommand


def init_sub_commands(sub_parser):
    """
    Creates sub commands
    :param sub_parser: sub parser
    :return:
    """
    RunCommand.init_args(sub_parser)
