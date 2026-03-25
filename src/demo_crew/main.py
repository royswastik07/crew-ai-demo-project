from demo_crew.crew import DemoCrew


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI Agents in coding'
    }

    try:
        DemoCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")