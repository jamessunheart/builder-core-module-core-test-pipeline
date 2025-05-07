# core_test_pipeline module (manual chaining)
from prompt_parser import run as parse
from code_generator import run as generate
from self_improver import run as improve

def run(instruction: str) -> dict:
    """
    Sequentially call the parser, generator, and improver.
    """
    parsed = parse(instruction)
    action = parsed.get('action')
    params = parsed.get('params', [])

    code = generate(action, params)
    feedback = improve(code)

    return {
        'instruction': instruction,
        'parsed': parsed,
        'code': code,
        'improvements': feedback
    }