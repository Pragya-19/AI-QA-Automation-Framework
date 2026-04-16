def generate_test_cases(requirement: str):
    print("\n[Test Generator Agent]")

    test_cases = [
        "TC01 - Valid login",
        "TC02 - Invalid username",
        "TC03 - Invalid password",
        "TC04 - Empty fields",
        "TC05 - Boundary inputs"
    ]

    for tc in test_cases:
        print(tc)

    return test_cases