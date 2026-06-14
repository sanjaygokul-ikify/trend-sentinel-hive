import unittest
from packages.core.engine import Engine, PolicyCompiler, AgentPool
from packages.core.types import Policy, Rule, Task

class TestEngine(unittest.TestCase):
    def test_compile_policy(self):
        policy = Policy('test', [Rule('allow', 'true')])
        engine = Engine(PolicyCompiler(), AgentPool())
        self.assertTrue(engine.compile_policy(policy))

    def test_dispatch_task(self):
        task = Task('allow', 'true')
        engine = Engine(PolicyCompiler(), AgentPool())
        self.assertFalse(engine.dispatch_task(task))

if __name__ == '__main__':
    unittest.main()