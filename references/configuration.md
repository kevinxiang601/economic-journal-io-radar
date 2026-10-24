# Local configuration

If `references/configuration.local.md` exists, read it for the user's digest directory, paper directory, optional laureate roster, and optional extra historical records. This local file is excluded from Git. Never publish local reports, PDFs, logs, credentials, personal paths, or automation state with the skill.

Otherwise use `./digests` and `./papers` under the task's working directory; omit laureate emphasis unless the user supplies a roster. Do not assume another user's desktop path exists. Digest filename: `经济学顶刊速览-YYYY-MM-DD.md`; paper subfolder: `YYYY-MM-DD/`. Use Asia/Shanghai dates unless the user configures another timezone. Pass the digest directory explicitly to `collect_candidates.py --history-dir`.
