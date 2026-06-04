def detect_vague_prompt(prompt):

    if len(prompt.strip()) < 10:
        return True

    vague_keywords = [
        "app",
        "platform",
        "software",
        "system",
        "business"
    ]

    prompt_lower = prompt.lower().strip()

    return prompt_lower in vague_keywords