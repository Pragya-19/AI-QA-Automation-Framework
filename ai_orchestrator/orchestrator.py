from story_analyzer import analyze_story
from test_generator import generate_test_cases
from review_agent import review_test_cases

def run_pipeline():
    requirement = """
    User should be able to login with valid credentials.
    Invalid inputs should show proper error messages.
    """

    print("🚀 Starting AI QA Orchestration Pipeline")

    analysis = analyze_story(requirement)
    test_cases = generate_test_cases(requirement)
    review = review_test_cases(test_cases)

    print("\n✅ Final Status:", review)

if __name__ == "__main__":
    run_pipeline()