import logging

from iotspark.commands.base import Base

logger = logging.getLogger(__name__)


class RunCommand(Base):
    def run(self):
        logger.info("Deploying environment ...")

    @staticmethod
    def init_args(sub_parser):
        # init sub command
        run = sub_parser.add_parser(
            'run', help='Deploy infrastructure'
        )

        node_group = run.add_mutually_exclusive_group(required=True)

        node_group.add_argument('-l', '--local', action='store_true',
                                help='deploy on local node only')

        node_group.add_argument('-r', '--remote', action='store_true',
                                help='deploy on remote or virtual nodes')
