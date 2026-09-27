import argparse
import os
from google.antigravity import Agent, Workspace, CapabilitiesConfig

def main():
    parser = argparse.ArgumentParser(description="Autonomous AI Agent Runner")
    parser.add_argument("--file", type=str, required=True, help="Path to the downloaded input file")
    parser.add_argument("--prompt", type=str, required=True, help="Instructions for the AI")
    args = parser.parse_args()

    workspace_path = "./output_workspace"
    os.makedirs(workspace_path, exist_ok=True)

    # Initialize the workspace mapped to the directory
    workspace = Workspace(workspace_path)

    # Load the downloaded file into the workspace
    if args.file and os.path.exists(args.file):
        workspace.load_file(args.file)

    # Initialize the Agent with the specified model and full capabilities
    agent = Agent(
        model="gemini-3.1-pro",
        capabilities=CapabilitiesConfig()
    )

    # Trigger the execution loop
    agent.run(task=args.prompt, workspace=workspace)

if __name__ == "__main__":
    main()
  
