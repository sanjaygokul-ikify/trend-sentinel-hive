import logging
from .types import Policy, Task, Agent
from .exceptions import PolicyCompilationError, TaskExecutionError


class Engine:
    def __init__(self, policy_compiler, agent_pool):
        self.policy_compiler = policy_compiler
        self.agent_pool = agent_pool
        self.logger = logging.getLogger(__name__)

    def compile_policy(self, policy: Policy) -> bool:
        try:
            compiled_policy = self.policy_compiler.compile(policy)
            return True
        except PolicyCompilationError as e:
            self.logger.error(f"Failed to compile policy: {e}")
            return False

    def dispatch_task(self, task: Task) -> bool:
        try:
            agent = self.agent_pool.get_available_agent()
            if agent:
                agent.execute(task)
                return True
            else:
                self.logger.warning("No available agents in the pool")
                return False
        except TaskExecutionError as e:
            self.logger.error(f"Failed to execute task: {e}")
            return False

    def execute_policy(self, policy: Policy):
        compiled_policy = self.policy_compiler.compile(policy)
        tasks = compiled_policy.get_tasks()
        for task in tasks:
            self.dispatch_task(task)

    def get_status(self):
        status = {}
        status['policy_compiler'] = self.policy_compiler.get_status()
        status['agent_pool'] = self.agent_pool.get_status()
        return status


class PolicyCompiler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def compile(self, policy: Policy):
        # Compile policy into a set of tasks
        tasks = []
        for rule in policy.get_rules():
            task = Task(rule.get_action(), rule.get_condition())
            tasks.append(task)
        return tasks

    def get_status(self):
        return "Policy compiler is online"


class AgentPool:
    def __init__(self):
        self.agents = []
        self.logger = logging.getLogger(__name__)

    def get_available_agent(self):
        for agent in self.agents:
            if agent.is_available():
                return agent
        return None

    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    def get_status(self):
        status = {}
        for agent in self.agents:
            status[agent.get_name()] = agent.get_status()
        return status


class Agent:
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(__name__)

    def get_name(self):
        return self.name

    def is_available(self):
        # Check if the agent is available
        return True

    def execute(self, task: Task):
        # Execute the task
        pass

    def get_status(self):
        return "Agent is online"
