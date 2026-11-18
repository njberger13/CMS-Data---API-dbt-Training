
import subprocess
import sys
from pathlib import Path

# Identify project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DBT_PROJECT = PROJECT_ROOT / "dbt_healthcare_analytics_project"

#function that specifies the step, bash command, and where to run the command
def run_step(description, command, working_directory):

    print(f"\n{'=' * 50}")
    print(f"STARTING: {description}")
    print(f"{'=' * 50}\n", flush=True)

    #run the process specified
    subprocess.run(
        command,
        cwd=working_directory,
        check=True
    )

    print(f"\nCOMPLETED: {description}", flush=True)


def main():

    print("\nSTARTING HEALTHCARE ANALYTICS PIPELINE")

    # Step 1: Ingest POS/QIES data
 #   run_step(
 #       "POS/QIES Data Ingestion",
 #       [sys.executable, "-m", "scripts.pull_pos_qies"],
 #       PROJECT_ROOT
 #   )

    # Step 2: Ingest Cost Report data
 #   run_step(
 #       "Cost Report Data Ingestion",
 #       [sys.executable, "-m", "scripts.pull_cost_reports"],
 #       PROJECT_ROOT
 #   )

    # Step 3: Execute dbt models using run or build or test
    run_step(
        "dbt Model Execution",
        ["dbt", "build"],
        DBT_PROJECT
    )

    print("\nHEALTHCARE ANALYTICS PIPELINE COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    main()
