from pathlib import Path
from prompt_templates import TEST_CASE_PROMPT

def generate_prompt_from_requirement(file_path: str):
    requirement = Path(file_path).read_text(encoding="utf-8")
    prompt = TEST_CASE_PROMPT.format(requirement=requirement)
    return prompt

if __name__ == "__main__":
    prompt = generate_prompt_from_requirement("ai_testing/sample_requirements.txt")
    print("Generated AI Prompt:\n")
    print(prompt)
