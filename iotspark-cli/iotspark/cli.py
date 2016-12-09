import sys
import argparse
import logging

from commands import init_sub_commands

from subprocess import list2cmdline

from iotspark.utils.log import SLogger

SLogger('iotspark').set()
logger = logging.getLogger(__name__)


# [\033[92mOK\033[0m]

class SubParserHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _format_action(self, action):
        """
        Handles sub commands
        :param action:
        :return:
        """
        s_class = super(argparse.RawDescriptionHelpFormatter, self)
        parts = s_class._format_action(action)

        if action.nargs == argparse.PARSER:
            parts = "\n".join(parts.split("\n")[1:])

        return parts


def create_cli_args():
    parser = argparse.ArgumentParser(prog="iotspark",
                                     description="IoT SPark infrastructure manager",
                                     formatter_class=SubParserHelpFormatter,
                                     epilog="Run 'iotspark COMMAND --help' for more information on a command.")

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='provide more detailed output')

    sub_parser = parser.add_subparsers(title='Commands')

    # init sub commands
    init_sub_commands(sub_parser)

    return parser.parse_args()


def _init_command():
    create_cli_args()


def main():
    try:
        _init_command()

        # Logging input cmd
        logger.debug('Command: %s', list2cmdline(sys.argv))
        logger.info("Preparing to install ...")
    except Exception as e:
        logger.error("%s", e)
        return 1
    except KeyboardInterrupt:
        print '\n Exiting ...'
        return 1


if __name__ == "__main__":
    main()
