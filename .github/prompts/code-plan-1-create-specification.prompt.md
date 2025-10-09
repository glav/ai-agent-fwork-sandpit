---
description: Create or update the feature specification from a natural language feature description.
---

The user input to you can be provided directly by the agent or as a command argument - you **MUST** consider it before proceeding with the prompt (if not empty).

User input:

$ARGUMENTS

The text the user typed after `/` command in the triggering message **is** the feature description. Assume you always have it available in this conversation even if `$ARGUMENTS` appears literally below. Do not ask the user to repeat it unless they provided an empty command.

Given that feature description, do this:

1. Load $$SPEC-TEMPLATE$$ to understand required sections.
2. Write the specification file to the $$SPECIFICATIONS-DIR$$ directory. using the template structure, replacing placeholders with concrete details derived from the feature description (arguments) while preserving section order and headings.
3. The name of the specification file should be a 3 word summary of the requested feature but prefixed with the date and time in the format:
  - YYYY-MM-DD-hh-mm-ss-{feature}. For eg. 2025-03-15-09-10-47-create-api-interface.md
4. Report completion with branch name, specification file path, and readiness for the next phase.

