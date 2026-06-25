# Copyright 2026 Anthropic PBC
# SPDX-License-Identifier: Apache-2.0
"""
Everything pre-supplied for the workshop: the agent's system prompt, tool
schemas, the local data those tools read, and the side-chat UI. You don't
edit this file — agent.py imports from it.
"""
import json
from pathlib import Path

import streamlit as st

DATA = Path("data")

SYSTEM = """\
You are the SRE Agent — an SRE/data-analyst agent embedded in an incident
dashboard. The application log is mounted at /mnt/session/uploads/app.log (large; use
grep/python to analyze it, don't read it whole). You have local tools
(get_metrics, get_recent_deploys, get_diff) that query the same data the
dashboard shows. Correlate evidence and state findings plainly and concisely.
"""

TOOLS = [
    {"type": "agent_toolset_20260401", "default_config": {"enabled": True}},
    {"type": "custom", "name": "get_metrics",
     "description": "Timeseries for a service+metric over the incident window.",
     "input_schema": {"type": "object",
                      "properties": {"service": {"type": "string"}, "metric": {"type": "string"}},
                      "required": ["service", "metric"]}},
    {"type": "custom", "name": "get_recent_deploys", "description": "Deploys in the last 6h.",
     "input_schema": {"type": "object", "properties": {}}},
    {"type": "custom", "name": "get_diff", "description": "Unified diff for a commit SHA.",
     "input_schema": {"type": "object", "properties": {"commit": {"type": "string"}},
                      "required": ["commit"]}},
]

metrics = json.loads((DATA / "metrics.json").read_text())
deploys = (DATA / "deploys.json").read_text()
diff = (DATA / "diff.txt").read_text()
