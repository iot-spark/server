import logging

from iotspark.commands.base import Base

logger = logging.getLogger(__name__)


class RunRemote(Base):
    name = 'run_remote'

    def __init__(self):
        logger.info("Preparing to install ...")
        self.run()

    def run(self):
        logger.info("Deploying remote environment ...")

    @staticmethod
    def init_args(sub_parser):
        # init sub command
        run_remote = sub_parser.add_parser(
            'run_remote',
            help='Deploy infrastructure on remote or virtual nodes'
        )
        run_remote.set_defaults(which=RunRemote.name)
