# Diabetes Risk Assessment with LLM

This project demonstrates how to pair **OpenAI chat completions** with a **strict validation layer**: patient-style data goes to the model, the response must be JSON with a fixed shape, and **Pydantic** enforces that structure so incomplete or invalid outputs are caught before you trust them.

It is **not** a regulated medical device or substitute for professional care—scope is educational and portfolio use only.

---

**What this showcases**

- **Structured LLM outputs** via OpenAI JSON response mode (`gpt-3.5-turbo`)
- **Schema enforcement** with a Pydantic `Assessment` model (`risk_level`, `key_factors`, `recommendations`)
- **Reliable testing** through mocked OpenAI clients—the full test suite runs **without** live API calls or billing

---

**Requirements**

Python 3.10+, `pip`, and an OpenAI API key when exercising the live API path.

---

**Setup**

```bash
git clone https://github.com/yourusername/llm_output_validation.git
cd llm_output_validation

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# Set OPENAI_API_KEY in .env
```

---

**Usage (Python)**

```python
from diabetes_diagnosis import get_risk

patient_data = {
    "age": 45,
    "bmi": 28.5,
    "glucose_level": 110,
    "family_history": "Father had type 2 diabetes",
    "symptoms": ["increased thirst", "frequent urination"],
    "blood_pressure": "130/85",
    "cholesterol": {"total": 210, "hdl": 45, "ldl": 130},
    "physical_activity": "sedentary",
}

result = get_risk(patient_data)
print(result)
```

Run the included sample end-to-end:

```bash
python diabetes_diagnosis.py
```

---

**Project layout**

- `diabetes_diagnosis.py` — `get_risk`, `validate`, `validate_llm_output`
- `conftest.py` — pytest fixtures (mocked OpenAI)
- `tests/` — validation, edge cases, and mock API scenarios
- `scripts/run_tests.sh` — pytest with HTML output under `reports/`
- `DOCUMENTATION.md` — deeper technical notes

---

**Tests**

```bash
pytest tests/
```

HTML report (pytest-html is listed in `requirements.txt`):

```bash
bash scripts/run_tests.sh
```

Coverage (optional):

```bash
pip install pytest-cov
pytest --cov=diabetes_diagnosis tests/
pytest --cov=diabetes_diagnosis --cov-report=html tests/
```

---

**Contributing**

Use a branch, run `pytest tests/` before opening a PR, and describe the change in the PR. Black, isort, and mypy are optional local tools—they are not pinned in `requirements.txt`.
