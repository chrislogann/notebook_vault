---
domain: 01-computer-science
class: 02-reference
subject: 03-python
type: reference
status: draft
created: 2026-07-30 22:02
updated: 2026-07-30 22:02
aliases: []
author: ''
source: gemma4
tags: []
---

# Virtual Python Environment

## Overview
> A virtual environment is a self-contained directory that contains specific versions of Python interpreters and third-party packages for a project. Its core purpose is to isolate dependencies, ensuring that different projects running on the same machine do not conflict with required library versions.

## Core Concepts
- **Isolation:** Each project gets its own set of libraries and executables, meaning changes or installations in one environment will not affect another system-wide installation or project.
- **Dependency Management:** It allows developers to explicitly lock down a specific working combination of packages (e.g., recording dependencies via `requirements.txt`), ensuring reproducibility across different machines.
- **Interpreter Path Modification:** Activating the virtual environment temporarily changes the system's PATH variable so that Python and pip point only to the executables within the isolated project directory, rather than the global system installation.

## Connections & References
- [[dependency-management]]
- [[virtualization]]
- [[python-interpreter]]
