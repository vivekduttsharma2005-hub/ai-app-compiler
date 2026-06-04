import streamlit as st
import subprocess

from intent_extractor import extract_intent
from system_designer import design_system
from schema_generator import generate_schema
from validator import validate_schema
from repair_engine import repair_schema
from assumptions import detect_vague_prompt
from simulator import simulate_execution

st.set_page_config(
    page_title="AI App Compiler",
    layout="wide"
)

st.title("🤖 AI App Compiler")

prompt = st.text_area(
    "Describe your application",
    height=150
)

if st.button("Generate"):

    if detect_vague_prompt(prompt):

        st.warning(
            "Prompt appears vague. Default assumptions will be used."
        )

    intent = extract_intent(prompt)

    design = design_system(intent)

    schema = generate_schema(design)

    # DEBUG OUTPUT
    st.subheader("RAW SCHEMA OUTPUT")
    st.code(schema)

    validation = validate_schema(schema)

    repaired_schema = schema

    if not validation["valid"]:

        repaired_schema = repair_schema(
            schema,
            validation
        )

    runtime_result = simulate_execution(
        repaired_schema
    )

    st.subheader("Intent")
    st.code(intent, language="json")

    st.subheader("System Design")
    st.code(design, language="json")

    st.subheader("Generated Schema")
    st.code(repaired_schema, language="json")

    st.subheader("Validation")
    st.json(validation)

    st.subheader("Runtime Simulation")
    st.json(runtime_result)

st.divider()

if st.button("Run Evaluation"):

    result = subprocess.run(
        ["py", "evaluator.py"],
        capture_output=True,
        text=True
    )

    st.subheader("Evaluation Results")

    st.write("STDOUT")
    st.code(result.stdout)

    st.write("STDERR")
    st.code(result.stderr)