# Fully self-contained core_test_pipeline

def run(instruction: str) -> dict:
    """
    End-to-end test of prompt parsing, code generation, and improvement.
    """
    # --- Prompt Parser ---
    import re
    instruction_clean = instruction.strip().lower()
    if 'create' in instruction_clean or 'generate' in instruction_clean:
        action = 'create'
    elif 'analyze' in instruction_clean:
        action = 'analyze'
    elif 'test' in instruction_clean:
        action = 'test'
    elif 'optimize' in instruction_clean:
        action = 'optimize'
    else:
        action = 'unknown'
    params = re.findall(r"\b\w+\b", instruction_clean)
    parsed = {'action': action, 'params': params, 'raw': instruction_clean}

    # --- Code Generator ---
    if action == 'create':
        code = f"def generated_function():\n    \"\"\"Auto-generated function with params: {', '.join(params)}\"\"\"\n    # TODO: implement logic\n    pass"
    elif action == 'analyze':
        code = f"# Analysis routine stub\n# Parameters: {', '.join(params)}"
    elif action == 'test':
        code = f"# Test case stub\nassert True  # Placeholder test using: {', '.join(params)}"
    elif action == 'optimize':
        code = f"# Optimization placeholder\n# Improve: {', '.join(params)}"
    else:
        code = "# Unknown action. No code generated."

    # --- Self Improver ---
    suggestions = []
    if 'TODO' in code:
        suggestions.append('Replace TODOs with actual implementation.')
    if 'pass' in code and 'def' in code:
        suggestions.append('Consider implementing stub functions.')
    if 'print(' in code:
        suggestions.append('Replace print statements with proper logging.')
    if len(code.strip()) < 40:
        suggestions.append('Code is too short for meaningful analysis.')

    improvements = {
        'improvements': suggestions,
        'summary': f"Found {len(suggestions)} suggestion(s).",
        'original': code
    }

    return {
        'instruction': instruction,
        'parsed': parsed,
        'code': code,
        'improvements': improvements
    }