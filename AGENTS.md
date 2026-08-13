# Ecommerce AI OS — Repository Instructions

## Repository Role

This repository is the primary repository for the Ecommerce AI OS.

Current phase:

Architecture Baseline / Project Scaffold.

## Current Boundary

This repository will eventually host the Ecommerce AI OS.

It does NOT currently inherit old architecture automatically.

The following are external/reference projects:

- Scrape Creators Provider Lab:
  /Volumes/projects/andy/0810/scrape-creators-provider-lab

- previous video-direction-workbench / SIG documents:
  reference material only

Validated Provider Lab facts may be reused later,
but they must not dictate the Ecommerce AI OS architecture.

## Current Development Rule

At the current stage:

- architecture before implementation
- small steps
- human review before freezing architecture
- do not introduce frameworks without a concrete business reason
- do not add Agent frameworks, MCP, RAG, vector databases, databases, or UI prematurely
- do not silently inherit old SIG / N01-N18 architecture
- preserve clear module boundaries
- prefer simple implementation before infrastructure complexity

## Git Rule

- do not push unless explicitly requested
- do not commit unless explicitly requested
- never commit secrets
- do not use git add . when precise staging is practical
