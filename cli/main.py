import argparse
from packages.core.engine import Engine
from services.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description='Sentinel Hive CLI')
    parser.add_argument('--policy', type=str, help='Policy name')
    args = parser.parse_args()

    engine = Engine(PolicyCompiler(), AgentPool())
    orchestrator = Orchestrator(engine)
    orchestrator.execute_policy(args.policy)

if __name__ == '__main__':
    main()