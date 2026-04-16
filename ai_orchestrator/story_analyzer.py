def analyze_story(requirement: str):
    print("\n[Story Analyzer Agent]")

    analysis = {
        "feature": "Login",
        "risks": [
            "Invalid credentials handling",
            "Security validation",
            "Empty input handling"
        ],
        "test_focus": [
            "Positive flow",
            "Negative scenarios",
            "Edge cases"
        ]
    }

    print("Analysis:", analysis)
    return analysis