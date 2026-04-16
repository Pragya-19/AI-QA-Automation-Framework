# AI-Generated Test Cases – Login Feature

## 📌 Requirement
User should be able to login using valid credentials and should see error messages for invalid inputs.

---

## ✅ Positive Test Cases

### TC_01 – Valid Login
- **Scenario:** User logs in with valid username and password
- **Steps:**
  1. Open login page
  2. Enter valid username
  3. Enter valid password
  4. Click login
- **Expected Result:** User is successfully logged in and redirected to dashboard

---

### TC_02 – Remember Me (if applicable)
- **Scenario:** User selects remember me option
- **Steps:**
  1. Enter valid credentials
  2. Select "Remember Me"
  3. Click login
- **Expected Result:** User remains logged in on next session

---

## ❌ Negative Test Cases

### TC_03 – Invalid Username
- **Scenario:** User enters incorrect username
- **Steps:**
  1. Enter invalid username
  2. Enter valid password
  3. Click login
- **Expected Result:** Error message displayed: "Invalid username"

---

### TC_04 – Invalid Password
- **Scenario:** User enters incorrect password
- **Steps:**
  1. Enter valid username
  2. Enter invalid password
  3. Click login
- **Expected Result:** Error message displayed: "Invalid password"

---

### TC_05 – Empty Fields
- **Scenario:** User submits without entering credentials
- **Steps:**
  1. Leave username blank
  2. Leave password blank
  3. Click login
- **Expected Result:** Validation message displayed for required fields

---

## ⚠️ Edge Test Cases

### TC_06 – Special Characters Input
- **Scenario:** User enters special characters in username/password
- **Steps:**
  1. Enter special characters (!@#$%)
  2. Click login
- **Expected Result:** Proper validation or rejection

---

### TC_07 – SQL Injection Attempt
- **Scenario:** User attempts SQL injection
- **Steps:**
  1. Enter `' OR '1'='1` in username/password
  2. Click login
- **Expected Result:** Input is sanitized and login fails

---

### TC_08 – Long Input Values
- **Scenario:** User enters very long username/password
- **Steps:**
  1. Enter 100+ character string
  2. Click login
- **Expected Result:** Input is handled properly or restricted

---

## 🔍 Coverage Summary

- Positive Scenarios: 2  
- Negative Scenarios: 3  
- Edge Scenarios: 3  

---

## 🤖 AI Contribution

These test cases were generated using a prompt-based AI testing approach, demonstrating how AI can assist in:
- Generating structured test scenarios
- Improving test coverage
- Identifying edge cases quickly

