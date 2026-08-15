# System Directive: `notebook-vault` Navigation & Maintenance

You are an AI assistant tasked with managing, navigating, and generating content for `notebook-vault`. You must strictly adhere to a 4-tier hierarchical organization scheme based on biological taxonomic principles: **Domain $\rightarrow$ Class $\rightarrow$ Subject $\rightarrow$ Note**. All generated notes, suggested folder paths, and Python automation scripts must strictly follow this schema.

## 1. Vault Taxonomy Definitions & Expected File Paths

When reading, navigating, or generating file paths, you must expect and enforce the following structure: `{vault_root}/[domain]/[class]/[subject]/[note].md`.

| **Tier** | **Name** | **Definition & Constraints** | **Naming Convention** |
| --- | --- | --- | --- |
| **1** | **Domain** | The macro field of study or broad discipline. | Lowercase `kebab-case`, strictly singular noun. Must be prefixed with two-digit numbers for custom sorting (e.g., `01-computer-science`). |
| **2** | **Class** | The functional role or structural format of the note. | Lowercase `kebab-case` with numerical prefix. Allowed values: `02-reference` (static guides/specs), `02-literature` (media/book summaries), `02-evergreen` (synthesized mental models), `02-project` (actionable tasks/logs). |
| **3** | **Subject** | A specific concept, tool, or sub-domain. | Lowercase `kebab-case`, strictly singular nouns (e.g., `large-language-model` not `large-language-models`). |
| **4** | **Note** | The individual atomic markdown document (`.md`). | Lowercase `kebab-case` or `Title Case`, strictly singular nouns. Index/MOC notes sit inside the subject folder and share its exact name. |

## 2. Directory Layout & Internal Utilities

The workspace contains both vault content folders and workspace automation utilities managed via `uv` / `pyproject.toml`.

```text
notebook-vault/
├── pyproject.toml              # UV workspace configuration
├── uv.lock                     # UV dependency lockfile
├── README.md                   # System Directive for AI navigation
├── _AIOS/                      # Translation & context layer for AI agents
│   ├── me.md                   # User identity & operating context
│   ├── skills.md               # Registry of AI cognitive capabilities
│   └── vault.md                # Master index and directory map
├── _Scripts/                   # Workspace automation scripts & tools
│   ├── import books/           # Tooling for importing EPUB/PDF book notes
│   └── summarize files/        # Ollama/YAML file summarization tooling
└── 01-computer-science/        # Domain 1
    └── 02-reference/           # Class: Reference
        ├── 03-computational-thinking/
        │   ├── 03-computational-thinking.md  # Subject Index / MOC
        │   ├── abstraction.md
        │   ├── algorithm.md
        │   ├── computational-pattern-recognition.md
        │   ├── decomposition.md
        │   └── evaluation.md
        ├── 03-encoding/
        ├── 03-git/
        ├── 03-hardware/
        ├── 03-large-language-model/
        ├── 03-linux/
        ├── 03-network/
        ├── 03-operating-system/
        └── 03-ubuntu-server/

```

## 3. Core Architectural Constraints

When relocating files or generating new vault structures, you must obey these absolute rules:

* **Enforce Strict 4-Tier Depth:** Do NOT create sub-notes or child folders inside subject folders (e.g., do not create `04-notes` or sub-subject folders). The maximum folder depth must always remain `Domain / Class / Subject / Note.md`.


* **Use Parallel Subjects:** Parent/child subject relationships must be organized as parallel sibling subject folders at Tier 3. Represent hierarchical dependencies using internal `[[wikilinks]]` in index/MOC notes rather than nested subfolders.


* **Split Cross-Disciplinary Material:** Book notes live in a single primary folder under `[domain]/02-literature/[subject]/[book-note].md`. You must split secondary topics or extracted concepts into their own atomic notes within the `reference` or `evergreen` classes, linking them back to the source literature note.


* **Handle Authors as Metadata:** Authors must be recorded in YAML frontmatter (e.g., `author: Leon Trotsky`) or as wikilinked concept notes within subject folders. Never create a dedicated top-level Class or Domain for an author or entity.


* **Isolate System & AI Tools:** Keep Python workspace automation packages isolated inside `_Scripts/`, and AI context files isolated inside `_AIOS/`. Do not place script files, environment parameters, or virtual environments inside the taxonomic domain directories.



## 4. Required Frontmatter Generation

> **Note on Templates:** The `## Bibliographical Metadata` block must only be included when `class` is `02-literature`. For `02-reference`, `02-evergreen`, or `02-project`, omit this section.
> 
> 

When creating or formatting notes, you must always output the following standardized YAML properties and document structure:

```markdown
---
domain: [insert domain]
class: [insert class]
subject: [insert subject]
type: [insert format type]            
status: [insert lifecycle status]           
created: {{date}} {{time}}
updated: {{date}} {{time}}
aliases: []
author: ""
source: ""
tags: []                 
---

# {{title}}

## Overview
> A brief 1-2 sentence summary defining the core mechanism or theory of the note.

## Core Concepts
- First fundamental principle or observation.
- Second fundamental principle or observation.
- Third fundamental principle or observation.

## Connections & References
- [[03-subject-name]]
- [[related-atomic-concept-1]]
- [[related-atomic-concept-2]]

```

## 5. File System & Scripting Instructions

When generating Python scripts to process or relocate notes, you must:

* Target the exact directory layout: `{vault_root}/{domain}/{class}/{subject}/{filename}.md`.


* Ensure all generated directory names are sanitized to lowercase `kebab-case`.


* Maintain distinct filenames across the vault to avoid breaking Obsidian's link resolution, which relies on unique note titles or shortest-path settings.


* Ensure any added dependencies or workspace packages are declared using `uv` workspace specs in `pyproject.toml` rather than modifying the core markdown notes directory.



## 6. AI Operating System (`_AIOS`) Integration

When operating within `notebook-vault`, AI agents must load and consult the translation layer files located in `_AIOS/` at the start of any new session or task to ensure precise alignment with vault standards:

* **User Context (`_AIOS/me.md`):** Consult this file to understand the user's technical background, expertise, and operational expectations. Strict adherence to the interaction guidelines (e.g., maintaining precision, developer-first orientation, and avoiding conversational fluff) is mandatory.


* **Directory Navigation (`_AIOS/vault.md`):** Utilize the master directory map to locate active taxonomic domains, classes, and subjects without hallucinating paths or recursively scanning the entire vault structure.


* **Cognitive Frameworks & Automation (`_AIOS/skills.md`):** Reference the skill registry to execute correct workspace automation scripts or to apply established analytical frameworks (e.g., "Rock Tumbler" evaluation, Computational Problem Solving, Geopolitical Analysis) drawn exclusively from the vault's active knowledge base.