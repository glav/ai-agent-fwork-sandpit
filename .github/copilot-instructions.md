---
mode: 'agent'
---

# Generalised instructions to follow for all tasks

## Variables
AGENT-DIR = '.agent'
AGENT-LOGS-DIR = '.agent/logs'
TEMPLATES-DIR = '.agent/templates'
SPECIFICATIONS-DIR = '.agent/specifications'
MEMORY-DIR = '.agent/memory'
SPEC-TEMPLATE = '.agent/templates/code-spec-template.md'

## General Instructions
- Ensure any of the directories used in the process exist before attempting to write files to them.
- Any time you encounter $$VARIABLE$$, you should replace it with the corresponding value from the Variables section.
- Ensure any code you produce is correct.
- Ensure any changes you apply are summarised within a file in an easily readable form in the $$AGENT-DIR$$ directory.
- The name of the file should be YYYYMMDD-hhmmss-{title}.md where {title} is a s 3 word summary of the requested changes eg. create-api-interface
  - The format of the file should take the form of an Architecture Decision Record (ADR)
  - For the ADR file - it should contain the following sections:
    - Title, Context (why this is being done), Description (what was done), Consequences (if any)
    - The sections should be brief, in markdown format and can be read by a human but also used by an LLM as context
- Make sure you ask for confirmation before making any changes
- If you asked for help on what prompts, or custom prompts are available, go through the files in the ~/.github/prompts directory and summarise the purpose of each one in 1 or 2 sentences.
- If you think you need make a lot of changes (for example, more than 2 files), get confirmation first before proceeding with large scale changes. Suggest smaller changes first if possible, and suggest using a formal planning prompt to breakdown the changes.
- If any document uses placeholder tokens like `[ALL_CAPS_IDENTIFIER]`, your responsibility is to gather the values, fill or intentionally defer them, and keep all three files mutually consistent. Downstream templates or command prompts may reference these files; when they exist, update them last so they reflect the newly agreed doctrine.

