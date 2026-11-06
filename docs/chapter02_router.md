# Chapter 2 – Structured Router

## Objective
Build a task router that classifies user requests into chat, research, or coding.

## Implementation
- Python 3.12
- Pydantic for structured output validation
- Rule-based intent classification
- Python dispatch function
- Pytest unit tests
- CSV-based evaluation with 30 requests

## Baseline Results

| Metric | Result |
|---|---|
| Route Accuracy | 50.00% (15/30) |
| False Tool Rate | 27.27% (pending label verification) |
| Average Latency | 0.0352 ms |
| LLM API Cost | $0.00 |

## Known Limitations
1. Keyword matching does not understand user intent.
2. Classification depends on rule priority.
3. Chinese language support is limited.
4. The system has no real LLM or tool integration.
5. The evaluation set is small and may not represent real-world inputs.

## Future Improvements
- Add an LLM-based Router with structured outputs.
- Compare the LLM Router with the rule-based baseline.
- Add unseen evaluation cases.
- Measure accuracy, latency, tool decisions, and API cost.
- Add timeouts, fallback routes, and error handling.