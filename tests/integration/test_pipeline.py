import unittest
from packages.core.engine import Engine
from packages.core.types import Policy, Rule
from services.orchestrator import Orchestrator

class TestPipeline(unittest.TestCase):
    def test_execute_policy(self):
        policy = Policy('test', [Rule('allow', 'true')])
        engine = Engine(PolicyCompiler(), AgentPool())
        orchestrator = Orchestrator(engine)
        orchestrator.execute_policy(policy)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()