# AsBuild demo

A small Python project whose pull requests show [AsBuild](https://github.com/hevelius-ai/asbuild)'s four verdicts. AsBuild checks an AI agent's pull request against tests a person approved, and records the result in a plain receipt. What it is, how to install it and what it does not prove: [AsBuild's README](https://github.com/hevelius-ai/asbuild#readme).

Its first story, [S1: count words](dev-docs/stories/S1/story.md), asks the app to count the words in a text file (`python -m app count <file>`); it was agreed and approved in [#2](https://github.com/hevelius-ai/asbuild-demo/pull/2). The first four pull requests below were built against it; #7 and #8 show two more cases that wait for you. Each shows its verdict, its receipt and its CI run. They stay open, so you can read them as they are:

| Pull request | What it does | Verdict |
| --- | --- | --- |
| [#3](https://github.com/hevelius-ai/asbuild-demo/pull/3) | Builds the story as agreed | PROVEN |
| [#4](https://github.com/hevelius-ai/asbuild-demo/pull/4) | Builds it, but the missing-file message differs from the agreed one | NOT PROVEN |
| [#5](https://github.com/hevelius-ai/asbuild-demo/pull/5) | Weakens a locked check so that it passes | WAITING FOR YOU |
| [#6](https://github.com/hevelius-ai/asbuild-demo/pull/6) | Breaks the test setup, so no results can be read | UNRESOLVED |
| [#7](https://github.com/hevelius-ai/asbuild-demo/pull/7) | Changes the README, which no story covers | WAITING FOR YOU |
| [#8](https://github.com/hevelius-ai/asbuild-demo/pull/8) | A new story's checks, for the owner to approve | WAITING FOR YOU |

MIT licence. Copyright (c) 2026 Hevelius AI Group LLC.
