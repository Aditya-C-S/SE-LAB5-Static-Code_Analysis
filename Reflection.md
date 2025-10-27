### Reflection

1️⃣ The easiest issues to fix were PEP 8 style violations and unused imports flagged by Flake8. These only required formatting or simple removals.

2️⃣ The hardest issues were security vulnerabilities like the `eval()` call and the bare `except:` block. These required a deeper understanding of safe coding and proper exception handling.

3️⃣ No false positives were observed. Each tool provided meaningful warnings that improved the code.

4️⃣ I would integrate these tools into a CI pipeline (GitHub Actions) and also use pre-commit hooks so code is always scanned before merging. This ensures long-term maintainability.

5️⃣ After applying fixes, the code became more readable, secure, robust and aligned with Python best practices. It now handles invalid inputs better and avoids hidden exceptions.
