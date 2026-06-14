from packages.core.engine import Engine
from packages.core.exceptions import PolicyCompilationError, TaskExecutionError

class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.logger = logging.getLogger(__name__)

    def execute_policy(self, policy_name: str):
        try:
            policy = Policy(policy_name, []) # Initialize policy with empty rules
            compiled_policy = self.engine.policy_compiler.compile(policy)
            self.engine.execute_policy(compiled_policy)
        except PolicyCompilationError as e:
            self.logger.error(f"Failed to compile policy: {e}")
            raise
        except TaskExecutionError as e:
            self.logger.error(f"Failed to execute task: {e}")
            raise