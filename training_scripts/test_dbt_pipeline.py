
import subprocess
from pathlib import Path

# Identify the dbt project directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DBT_PROJECT = PROJECT_ROOT / "dbt_healthcare_analytics_project"


def run_pipeline():

    print("\nSTARTING DBT PIPELINE TEST")

    # Build all dbt models and execute their tests
    subprocess.run(
        ["dbt", "build"],
        cwd=DBT_PROJECT,
        check=True
    )

    print("\nDBT PIPELINE COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    run_pipeline()
