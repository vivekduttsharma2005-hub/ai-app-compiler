import json
import time

from intent_extractor import extract_intent
from system_designer import design_system
from schema_generator import generate_schema
from validator import validate_schema
from repair_engine import repair_schema
from simulator import simulate_execution
from metrics import MetricsTracker

tracker = MetricsTracker()

with open("test_prompts.json", "r") as file:
    prompts = json.load(file)

for item in prompts:

    prompt = item["prompt"]

    start = time.time()

    try:

        intent = extract_intent(prompt)

        design = design_system(intent)

        schema = generate_schema(design)

        validation = validate_schema(schema)

        repaired = False
        final_schema = schema

        if not validation["valid"]:

            repaired = True

            final_schema = repair_schema(
                schema,
                validation
            )

        runtime = simulate_execution(
            final_schema
        )

        latency = time.time() - start

        tracker.record(
            success=runtime["success"],
            latency=latency,
            validation_failed=not validation["valid"],
            repaired=repaired
        )

    except Exception as e:

        print("ERROR:", e)

        tracker.record(
            success=False,
            latency=0
        )

print(
    json.dumps(
        tracker.report(),
        indent=2
    )
)