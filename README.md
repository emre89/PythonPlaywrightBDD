# Python Playwright BDD (Test object: Läslistan)

This repository contains automated regression tests for the website [Läslistan](https://tap-vt25-testverktyg.github.io/exam--reading-list/)

## About This Framework

This is a **Python-based test automation framework** built with **Playwright** and **Behave** using the **BDD (Behavior-Driven Development)** methodology.  

Key points:

- **BDD with Behave**: Test scenarios are written in Gherkin syntax (`.feature` files) to describe user behavior in a human-readable format.  
- **Page Object Model (POM)**: Pages are represented as classes to encapsulate locators and actions, improving code reusability and maintainability. Created BasePage to contain common elements and behaviors as a parent class. 
- **Playwright for Python**: Provides fast and reliable browser automation across all modern browsers.  
- **Structured and maintainable**: Step definitions, feature files, and page objects are organized to make the framework easy to extend for future features.  

This setup allows for **clear, reusable, and easily-maintainable tests**.

## What is tested

- Catalog
- Add new books
- Add / remove favorites
- Navigation between pages

## How to run tests

Follow these steps to set up and run the tests:

### 1. Clone the repository

    git clone https://github.com/emre89/PythonPlaywrightBDD.git

### 2. Go into the project

    cd PythonPlaywrightBDD

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Run all tests

    behave src/features

#### or run only active tests (green)

    behave src/features --tags "not @skip"
