<!-- Copyright 2026 Anthropic PBC -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Incident-2277

> **Workshop sample.** Not maintained and not accepting contributions.

> **It's 2am. PagerDuty fires: checkout p99 latency is 10× baseline.**
> You know the drill — open the dashboard, grep logs, scroll deploys, guess,
> check, repeat. Forty minutes later you find it: someone shipped an N+1 query.
>
> This workshop builds the agent that does that forty minutes for you.

A working incident dashboard for a fictional e-commerce stack. The Metrics,
Logs, and Deploys pages run out of the box from mock data. There's an
**SRE Agent** chat panel on the side of every page — and it's offline.
Bringing it online is the workshop: seven small functions in one file, each a
single [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)
API call.

When you're done, you ask it *"what caused the latency spike?"* and watch it
grep a 70k-line log inside its own cloud sandbox, call your local tools to
pull metrics and deploys, correlate the timestamps, fetch the offending diff,
and name the commit.

## Setup

You need Python **3.10+** and an [Anthropic API key](https://console.anthropic.com/settings/keys).

```bash
git clone https://github.com/anthropic-experimental/cwc-workshops
cd cwc-workshops/ship-your-first-managed-agent

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env               # then put your ANTHROPIC_API_KEY in .env
streamlit run app.py
```

The dashboard opens at `localhost:8501`. Click around — Metrics, Logs,
Deploys all work. The SRE Agent panel on the right says
*"agent offline — implement `setup_agent()` in `agent.py`"*.

## What you build

Open **`agent.py`**. Seven functions, all `raise NotImplementedError`. Fill them
in and the panel comes online one step at a time.

| # | Function | API call | Lines |
|---|---|---|---|
| 1 | `setup_agent()` | `client.beta.agents.create` | 3 |
| 2 | `setup_environment()` | `client.beta.environments.create` | 4 |
| 3 | `upload_log()` | `client.beta.files.upload` | 2 |
| 4 | `start_session()` | `client.beta.sessions.create` | 5 |
| 5 | `stream_reply()` | `client.beta.sessions.events.stream` + `.send` | 12 |
| 6 | `handle_tool()` | runs locally — reads `data/*.json` | 7 |
| 7 | `delete_session()` | `client.beta.sessions.delete` | 1 |

That's ~34 lines total. Everything else — the system prompt, tool schemas,
the chat UI, the session picker — is provided in `provided.py`.

Other content omitted for brevity in this commit
