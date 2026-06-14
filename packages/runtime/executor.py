import logging
from ..core.engine import Engine


class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.logger = logging.getLogger(__name__)

    def execute_policy(self, policy):
        self.engine.execute_policy(policy)

    def dispatch_task(self, task):
        self.engine.dispatch_task(task)

    def compile_policy(self, policy):
        self.engine.compile_policy(policy)

    def get_status(self):
        return self.engine.get_status()