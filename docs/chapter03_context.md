
# Chapter 3: Context Management

## 3.6 Context Compression

Goal: Reduce token usage while preserving important information.

Three approaches:
1. Summarize: Compress old conversations into a state summary.
2. Offload: Store large outputs in workspace files.
3. Drop: Remove irrelevant or outdated information.

Important:
- Keep critical instructions and constraints.
- Use file references for large outputs.
- Do not confuse summarization with arbitrary truncation.

## 3.7 Context Pollution

Problem:
Irrelevant information can reduce model performance.

Common sources:
- Large tool outputs
- Too many RAG chunks
- Unnecessary sub-agent outputs
- Website navigation and advertisements
- Outdated memory

Solutions:
- Normalize tool outputs
- Rerank retrieved documents
- Apply size limits
- Use structured summaries
- Filter irrelevant content

## 3.8 Context Isolation

Goal:
Give each sub-agent only the context it needs.

Example:
A research agent receives:
- Task description
- Relevant constraints
- Output requirements

It does not need the full parent-agent history.

## Future Implementation

Possible module:
src/agent_lab/context.py

Future features:
- Context budget
- History summarization
- Tool output filtering
- Workspace offloading
- Sub-agent context isolation


## 3.10 Tool Result Compression

Goal:
Reduce the size of tool outputs before sending them to an LLM.

Implementation:
- File: src/agent_lab/tool_output.py
- Extract important failure and error lines.
- Preserve the process exit code.
- Keep a limited number of final output lines.
- Return a structured summary.

Limitations:
- Important details may be lost during compression.
- Keyword matching does not detect every error.
- Sensitive data must be filtered before LLM use.
- Large outputs are still held in memory.

## 3.11 Context Debugging Checklist

When an agent produces unexpected results, check:

- [ ] Required system instructions are present.
- [ ] The current user request is complete.
- [ ] Old information does not override new information.
- [ ] Retrieved documents are relevant.
- [ ] Tool results are not excessively long.
- [ ] External content does not contain malicious instructions.
- [ ] Context summaries preserve important facts.
- [ ] Context stays within the token budget.

Important:
Inspect sanitized context data during debugging.
Do not log API keys, passwords, or sensitive user data.

Future improvement:
Add automatic context validation and debugging
when the project supports real LLM calls.
