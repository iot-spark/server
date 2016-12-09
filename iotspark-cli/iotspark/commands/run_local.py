import logging

from iotspark.commands.base import Base

logger = logging.getLogger(__name__)


class RunLocal(Base):
    name = 'run_local'

    def __init__(self):
        logger.info("Preparing to install ...")
        self.run()

    def run(self):
        logger.info("Deploying local environment ...")

    @staticmethod
    def init_args(sub_parser):
        # init sub command
        run_local = sub_parser.add_parser(
            'run_local', help='Deploy infrastructure on local node only'
        )
        run_local.set_defaults(which=RunLocal.name)
