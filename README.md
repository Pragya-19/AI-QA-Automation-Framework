## 🔁 CI/CD Status

[[![QA Automation Tests](https://github.com/Pragya-19/QA-Automation-Framework-Pytest-Playwright-API-UI-CI/actions/workflows/ci.yml/badge.svg)](https://github.com/Pragya-19/QA-Automation-Framework-Pytest-Playwright-API-UI-CI/actions/workflows/ci.yml)]

🚀 QA Automation Framework + AI Testing Orchestration

🔹 End-to-End QA Pipeline · UI + API + AI

A production-ready QA Automation Framework combining:

✅ UI Automation (Playwright + Pytest + POM)
✅ API Automation (Requests + Pytest)
✅ CI/CD Integration (GitHub Actions)
🔥 AI-Powered Test Generation & Orchestration (Multi-Agent Pipeline)


🧠 Problem Statement

Traditional QA automation:

Requires manual test case creation
Is time-consuming and repetitive
Struggles with scalability and evolving requirements

👉 This project solves that by introducing AI-driven test orchestration, enabling:

Automated test case generation
Intelligent requirement analysis
Faster and scalable QA workflows
🏗️ Architecture Overview

🔧 Tech Stack

Layer	Tools

UI Automation	Playwright, Pytest

API Automation	Requests, Pytest

Design Pattern	Page Object Model (POM)

CI/CD	GitHub Actions

AI Layer	Custom Multi-Agent Orchestrator

Language	Python


📂 Project Structure

QA-Automation-Framework/

│
├── tests/

│   ├── ui/

│   ├── api/

│
├── pages/                # Page Object Model

├── api_clients/          # API abstraction layer

├── utils/                # Config & helpers

│
├── ai_testing/           # AI test generation

├── ai_orchestrator/      # Multi-agent orchestration

│
├── screenshots/          # Execution proofs

├── reports/              # Test reports

│
└── .github/workflows/    # CI/CD pipeline

🌐 UI Automation Testing
Playwright-based automation
Page Object Model (POM)

Covers:
Login flow
Validation scenarios
Negative test cases

✔ Features
Cross-browser support
Stable locators
Clean test structure

🔌 API Automation Testing
Requests + Pytest
Covers:
Users endpoint
CRUD operations
Negative scenarios

✔ Features
API validation
Response assertions

Edge case handling
🤖 AI Testing (Game Changer 🔥)
📌 AI Test Generator

Automatically generates:

Positive test cases
Negative scenarios
Edge cases


📸 Example Output:


🧠 AI Testing Orchestrator (Multi-Agent System)

A custom-built AI QA pipeline simulating real-world intelligent testing:

🔹 Agents:

Story Analyzer
Understands requirements
Identifies risks

Test Generator
Creates structured test cases

Review Agent
Validates coverage
Approves test quality


📸 Pipeline Execution: screenshots/ai_orchestrator_pipeline_output.png


🔁 CI/CD Pipeline

Integrated with GitHub Actions for:

Automated test execution
Headless browser runs
Continuous validation

📸 CI/CD Run:


📊 Test Execution
UI + API tests run together
Unified test suite
Fast execution with Pytest

📸 Test Run Output:


🎥 Test Evidence
Screenshots
Video recordings

Examples:

video-login-successful.webm
video-negative-login.webm

▶️ How to Run

1. Clone Repo
git clone https://github.com/Pragya-19/QA-Automation-Framework-Pytest-Playwright-API-UI-CI.git
cd QA-Automation-Framework-Pytest-Playwright-API-UI-CI

3. Setup Environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

5. Run Tests
pytest

7. Run AI Testing
python ai_testing/generate_test_cases.py

9. Run AI Orchestrator
python ai_orchestrator/orchestrator.py

🧪 Key Highlights

✔ End-to-End Automation Framework
✔ UI + API + CI/CD Integration
✔ AI-driven Test Case Generation
✔ Multi-Agent QA Orchestration
✔ Industry-level project structure

🚀 Future Enhancements
Allure Reporting Integration
Parallel execution
Docker support
LLM-based dynamic test execution
Cloud test execution


👩‍💻 Author

Pragya Kapil

QA Automation Engineer | AI Testing Enthusiast

Linkedin :https://www.linkedin.com/in/pragya-kapil-qa
