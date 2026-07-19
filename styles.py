"""
DeepResearch — Gradio UI
=========================

A case-file / research-desk interface for a deep research agent.

WIRE UP YOUR AGENT
-------------------
Everything below `run_deep_research()` is UI scaffolding. The only function
you need to touch is `run_deep_research`. It's a generator so the report can
stream in as your agent works — replace the placeholder body with a call
into your actual agent, e.g.:

    def run_deep_research(query, history):
        for chunk in your_agent.stream(query):
            yield chunk

If your agent isn't a generator, just `yield` once with the final markdown.
"""

import datetime
import time

import gradio as gr

CASE_DATE = datetime.date.today().strftime("%b %d, %Y")

EXAMPLES = [
    "Most popular AI agent frameworks in 2026",
    "Most commercially successful agentic AI implementations in 2026",
    "Celebrities who don't like cheese",
]

FONT_LINKS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link
    href="https://fonts.googleapis.com/css2?family=Newsreader:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap"
    rel="stylesheet"
>
"""

HEADER_HTML = f"""
<header class="dr-header">
    <div class="dr-brand">
        <div class="dr-logo" aria-hidden="true">
            <span class="dr-logo-card dr-logo-card-1"></span>
            <span class="dr-logo-card dr-logo-card-2"></span>
            <span class="dr-logo-card dr-logo-card-3"></span>
        </div>

        <div class="dr-brand-copy">
            <div class="dr-eyebrow">
                <span class="dr-status-dot"></span>
                Archive &nbsp;/&nbsp; Research desk
            </div>

            <h1>
                Deep<em class="dr-title-accent">Research</em>
            </h1>

            <p>
                Open a case file on any topic. Every claim gets traced back to a source.
            </p>
        </div>
    </div>

    <div class="dr-header-meta">
        <span class="dr-meta-label">Case opened&nbsp;{CASE_DATE}</span>
        <span class="dr-meta-divider"></span>
        <span class="dr-meta-label">No. 2026&#8209;07</span>
    </div>
</header>

<section class="dr-intro">
    <h2>What are you investigating?</h2>
    <p>
        Name a topic, company, person, or trend. The more specific the brief,
        the sharper the file that comes back.
    </p>
</section>
"""

CSS = """
:root {
    color-scheme: dark;
}

.gradio-container {
    --dr-bg: #10162a;
    --dr-bg-secondary: #161d38;
    --dr-panel: #1b2340;
    --dr-panel-border: #2c3560;
    --dr-paper: #ece2c6;
    --dr-paper-soft: #e2d6b3;
    --dr-ink: #1d2233;
    --dr-ink-soft: #454c6b;

    --dr-text: #ece7d8;
    --dr-text-soft: #b7bcd8;
    --dr-muted: #7d84a8;

    --dr-rust: #b3452f;
    --dr-rust-hover: #973824;
    --dr-brass: #c9a227;
    --dr-brass-soft: rgba(201, 162, 39, 0.14);

    --dr-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.35);
    --dr-shadow-md:
        0 22px 48px rgba(4, 6, 16, 0.45),
        0 2px 8px rgba(4, 6, 16, 0.3);

    max-width: 1080px !important;
    min-height: 100vh !important;
    margin: 0 auto !important;
    padding: 2.25rem 2rem 5rem !important;

    background: transparent !important;
    color: var(--dr-text) !important;

    font-family: "IBM Plex Sans", ui-sans-serif, system-ui, sans-serif !important;
}

html,
body {
    min-height: 100%;
}

body {
    margin: 0;
    background:
        radial-gradient(circle at 10% -6%, rgba(201, 162, 39, 0.08), transparent 32rem),
        radial-gradient(circle at 96% 8%, rgba(179, 69, 47, 0.09), transparent 28rem),
        var(--dr-bg, #10162a) !important;
}

/* faint paper-grain / desk texture */
body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    opacity: 0.5;
    background-image:
        repeating-linear-gradient(
            0deg,
            rgba(255, 255, 255, 0.012) 0px,
            rgba(255, 255, 255, 0.012) 1px,
            transparent 1px,
            transparent 3px
        );
}

/* =========================================================
   HEADER
   ========================================================= */

.dr-header {
    position: relative;
    z-index: 1;

    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 2rem;

    padding: 0.5rem 0 1.9rem;
    margin-bottom: 3rem;

    border-bottom: 1px dashed var(--dr-panel-border);
}

.dr-brand {
    display: flex;
    align-items: center;
    gap: 1.3rem;
}

.dr-logo {
    position: relative;
    width: 50px;
    height: 44px;
    flex-shrink: 0;
}

.dr-logo-card {
    position: absolute;
    top: 4px;
    left: 0;
    width: 38px;
    height: 30px;
    border-radius: 3px;
    box-shadow: var(--dr-shadow-sm);
    animation: dr-card-enter 0.45s ease both;
}

.dr-logo-card-1 {
    background: var(--dr-paper);
    transform: rotate(-9deg);
    z-index: 1;
}

.dr-logo-card-2 {
    background: var(--dr-brass);
    left: 8px;
    top: 8px;
    transform: rotate(4deg);
    z-index: 2;
    animation-delay: 0.06s;
}

.dr-logo-card-3 {
    background: var(--dr-rust);
    left: 12px;
    top: 2px;
    width: 26px;
    height: 20px;
    transform: rotate(-3deg);
    z-index: 3;
    animation-delay: 0.12s;
}

@keyframes dr-card-enter {
    from {
        opacity: 0;
        transform: translateY(4px) rotate(0deg);
    }
}

.dr-brand-copy {
    min-width: 0;
}

.dr-eyebrow {
    display: flex;
    align-items: center;
    gap: 0.5rem;

    margin-bottom: 0.5rem;

    color: var(--dr-muted);
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.66rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}

.dr-status-dot {
    width: 7px;
    height: 7px;
    background: var(--dr-rust);
    border-radius: 999px;
    box-shadow: 0 0 0 4px rgba(179, 69, 47, 0.16);
}

.dr-brand-copy h1 {
    margin: 0;

    color: var(--dr-text);
    font-family: "Newsreader", Georgia, serif;
    font-size: clamp(2rem, 4.6vw, 2.9rem);
    font-weight: 600;
    letter-spacing: -0.01em;
    line-height: 1;
}

.dr-title-accent {
    font-style: italic;
    font-weight: 500;
    color: var(--dr-brass);
}

.dr-brand-copy > p {
    max-width: 560px;
    margin: 0.7rem 0 0;

    color: var(--dr-muted);
    font-size: 0.92rem;
    line-height: 1.5;
}

.dr-header-meta {
    display: flex;
    align-items: center;
    gap: 0.8rem;

    padding-bottom: 0.25rem;

    color: var(--dr-muted);
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    white-space: nowrap;
}

.dr-meta-divider {
    width: 3px;
    height: 3px;
    background: var(--dr-panel-border);
    border-radius: 999px;
}

/* =========================================================
   INTRO
   ========================================================= */

.dr-intro {
    position: relative;
    z-index: 1;
    max-width: 700px;
    margin-bottom: 1.6rem;
}

.dr-intro h2 {
    margin: 0 0 0.5rem;

    color: var(--dr-text);
    font-family: "Newsreader", Georgia, serif;
    font-size: clamp(1.3rem, 3vw, 1.65rem);
    font-weight: 600;
    letter-spacing: -0.01em;
}

.dr-intro p {
    margin: 0;
    color: var(--dr-muted);
    font-size: 0.95rem;
    line-height: 1.6;
}

/* =========================================================
   QUERY COMPOSER — "request slip"
   ========================================================= */

.dr-query-row {
    position: relative;
    z-index: 1;

    display: flex !important;
    align-items: stretch !important;
    gap: 0.65rem !important;

    padding: 0.6rem !important;

    background: var(--dr-panel) !important;
    border: 1px solid var(--dr-panel-border) !important;
    border-radius: 10px !important;
    box-shadow: var(--dr-shadow-md) !important;

    transition: border-color 0.18s ease, box-shadow 0.18s ease !important;
}

.dr-query-row:focus-within {
    border-color: var(--dr-brass) !important;
    box-shadow: 0 0 0 3px var(--dr-brass-soft), var(--dr-shadow-md) !important;
}

#dr-query,
#dr-query > div,
#dr-query .wrap,
#dr-query .form,
#dr-query .block {
    flex: 1 1 auto !important;
    margin: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    box-shadow: none !important;
}

#dr-query label {
    margin: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

#dr-query .label-wrap {
    display: none !important;
}

#dr-query textarea,
#dr-query input {
    width: 100% !important;
    min-height: 58px !important;
    max-height: 180px !important;

    padding: 0.95rem 1rem !important;

    background: transparent !important;
    color: var(--dr-text) !important;

    border: none !important;
    outline: none !important;
    box-shadow: none !important;

    font-family: "IBM Plex Sans", sans-serif !important;
    font-size: 1rem !important;
    line-height: 1.5 !important;

    resize: none !important;
}

#dr-query textarea::placeholder,
#dr-query input::placeholder {
    color: var(--dr-muted) !important;
    opacity: 0.75 !important;
}

#dr-run {
    align-self: stretch !important;

    min-width: 150px !important;
    min-height: 58px !important;
    padding: 0.85rem 1.3rem !important;

    background: var(--dr-rust) !important;
    color: var(--dr-paper) !important;

    border: 1px solid var(--dr-rust) !important;
    border-radius: 6px !important;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;

    font-family: "IBM Plex Mono", monospace !important;
    font-size: 0.76rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;

    transition: background 0.15s ease, transform 0.1s ease !important;
}

#dr-run::after {
    content: "  \\2192";
}

#dr-run:hover {
    background: var(--dr-rust-hover) !important;
    transform: translateY(-1px);
}

#dr-run:active {
    transform: translateY(1px) !important;
}

#dr-run:focus-visible {
    outline: 2px solid var(--dr-brass) !important;
    outline-offset: 2px !important;
}

/* =========================================================
   EXAMPLES — index cards
   ========================================================= */

.dr-examples-label {
    position: relative;
    z-index: 1;

    display: flex;
    align-items: center;
    gap: 0.8rem;

    margin: 1.9rem 0 0.9rem;

    color: var(--dr-muted);
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}

.dr-examples-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: var(--dr-panel-border);
}

#dr-examples,
#dr-examples > div,
#dr-examples .wrap,
#dr-examples .block {
    margin: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

#dr-examples label {
    margin: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

#dr-examples .label-wrap {
    display: none !important;
}

#dr-examples table {
    width: 100% !important;
    background: transparent !important;
    border: none !important;
    border-collapse: separate !important;
    border-spacing: 0 !important;
}

#dr-examples thead {
    display: none !important;
}

#dr-examples tbody {
    display: block !important;
    width: 100% !important;
}

#dr-examples tr {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 0.9rem !important;
    width: 100% !important;
    background: transparent !important;
    border: none !important;
}

#dr-examples td,
#dr-examples button {
    position: relative;

    display: inline-flex !important;
    align-items: center !important;

    width: auto !important;
    max-width: 300px;
    margin: 0 !important;
    padding: 0.7rem 1rem 0.7rem 1.15rem !important;

    background: var(--dr-paper) !important;
    color: var(--dr-ink) !important;

    border: 1px solid var(--dr-paper-soft) !important;
    border-left: 4px solid var(--dr-brass) !important;
    border-radius: 3px !important;
    box-shadow: var(--dr-shadow-sm) !important;

    cursor: pointer !important;

    font-family: "IBM Plex Sans", sans-serif !important;
    font-size: 0.83rem !important;
    font-weight: 500 !important;
    line-height: 1.35 !important;
    text-align: left !important;

    transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease !important;
}

#dr-examples tr td:nth-child(1) button,
#dr-examples tr td:nth-child(1) { transform: rotate(-0.6deg); }
#dr-examples tr td:nth-child(2) button,
#dr-examples tr td:nth-child(2) { transform: rotate(0.5deg); }
#dr-examples tr td:nth-child(3) button,
#dr-examples tr td:nth-child(3) { transform: rotate(-0.3deg); }

#dr-examples td:hover,
#dr-examples button:hover {
    border-left-color: var(--dr-rust) !important;
    box-shadow: 0 6px 16px rgba(4, 6, 16, 0.35) !important;
    transform: translateY(-2px) rotate(0deg) !important;
}

/* =========================================================
   REPORT — case file
   ========================================================= */

#dr-report {
    position: relative;
    z-index: 1;

    min-height: 40px;
    margin-top: 3.4rem !important;
    padding: 0 !important;

    background: transparent !important;
    color: var(--dr-ink) !important;

    border: none !important;
    box-shadow: none !important;
}

#dr-report > div,
#dr-report .prose {
    max-width: none !important;
    background: transparent !important;
    color: var(--dr-ink) !important;
}

#dr-report:not(:empty)::before {
    content: "Case file";
    display: block;
    margin-bottom: 1.1rem;

    color: var(--dr-muted);
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
}

#dr-report:not(:empty)::after {
    content: "Traced & sourced";
    position: absolute;
    top: -18px;
    right: 30px;
    z-index: 2;

    width: 104px;
    height: 104px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 12px;

    color: var(--dr-rust);
    background: transparent;
    border: 2px solid var(--dr-rust);
    border-radius: 50%;
    box-shadow: 0 0 0 3px var(--dr-bg);
    transform: rotate(-10deg);
    opacity: 0.82;

    font-family: "IBM Plex Mono", monospace;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    line-height: 1.3;
    pointer-events: none;
}

#dr-report:not(:empty) {
    padding: clamp(1.5rem, 4vw, 2.7rem) !important;

    background: var(--dr-paper) !important;
    border: 1px solid var(--dr-paper-soft) !important;
    border-radius: 10px !important;
    box-shadow: var(--dr-shadow-md) !important;

    animation: dr-report-enter 0.35s ease both;
}

@keyframes dr-report-enter {
    from {
        opacity: 0;
        transform: translateY(8px);
    }
}

/* =========================================================
   REPORT TYPOGRAPHY
   ========================================================= */

#dr-report h1,
#dr-report h2,
#dr-report h3,
#dr-report h4 {
    color: var(--dr-ink);
    font-family: "Newsreader", Georgia, serif;
    line-height: 1.25;
}

#dr-report h1 {
    margin: 0.4rem 0 1.2rem;
    padding-bottom: 0.9rem;
    border-bottom: 1px solid var(--dr-paper-soft);
    font-size: clamp(1.55rem, 4vw, 2.05rem);
    font-weight: 600;
}

#dr-report h2 {
    margin: 2.2rem 0 0.75rem;
    font-size: 1.28rem;
    font-weight: 600;
}

#dr-report h2::before {
    content: "";
    display: inline-block;
    width: 4px;
    height: 0.9em;
    margin-right: 0.5rem;
    background: var(--dr-rust);
    vertical-align: -0.08em;
}

#dr-report h3 {
    margin: 1.7rem 0 0.6rem;
    font-size: 1.05rem;
    font-weight: 600;
}

#dr-report h4 {
    margin: 1.3rem 0 0.5rem;
    color: var(--dr-ink-soft);
    font-family: "IBM Plex Sans", sans-serif;
    font-size: 0.92rem;
    font-weight: 700;
}

#dr-report p {
    margin: 0.75rem 0;
    color: var(--dr-ink-soft);
    font-family: "IBM Plex Sans", sans-serif;
    font-size: 0.97rem;
    line-height: 1.72;
}

#dr-report strong {
    color: var(--dr-ink);
    font-weight: 700;
}

#dr-report a {
    color: var(--dr-rust);
    font-weight: 600;
    text-decoration: underline;
    text-decoration-color: rgba(179, 69, 47, 0.4);
    text-underline-offset: 3px;
}

#dr-report a:hover {
    text-decoration-color: currentColor;
}

#dr-report ul,
#dr-report ol {
    margin: 0.8rem 0;
    padding-left: 1.35rem;
}

#dr-report li {
    margin: 0.4rem 0;
    color: var(--dr-ink-soft);
    font-family: "IBM Plex Sans", sans-serif;
    line-height: 1.65;
}

#dr-report li::marker {
    color: var(--dr-rust);
}

#dr-report hr {
    height: 1px;
    margin: 1.9rem 0;
    background: var(--dr-paper-soft);
    border: none;
}

#dr-report code {
    padding: 0.1rem 0.38rem;
    background: rgba(29, 34, 51, 0.06);
    color: var(--dr-rust);
    border: 1px solid rgba(29, 34, 51, 0.1);
    border-radius: 4px;
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.86em;
}

#dr-report pre {
    overflow-x: auto;
    margin: 1.1rem 0;
    padding: 1rem 1.15rem;
    background: rgba(29, 34, 51, 0.05);
    border: 1px solid var(--dr-paper-soft);
    border-radius: 6px;
}

#dr-report pre code {
    padding: 0;
    background: transparent;
    color: var(--dr-ink-soft);
    border: none;
}

#dr-report blockquote {
    margin: 1.3rem 0;
    padding: 0.9rem 1.1rem;
    background: rgba(179, 69, 47, 0.06);
    color: var(--dr-ink-soft);
    border: none !important;
    border-left: 3px solid var(--dr-rust) !important;
    border-radius: 0 6px 6px 0;
}

#dr-report blockquote p {
    margin: 0;
}

#dr-report .table-wrap,
#dr-report > div {
    overflow-x: auto;
}

#dr-report table {
    width: 100%;
    margin: 1.2rem 0;
    background: #f4ecd8;
    border: 1px solid var(--dr-paper-soft);
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 6px;
    overflow: hidden;
}

#dr-report th,
#dr-report td {
    padding: 0.68rem 0.8rem;
    color: var(--dr-ink-soft);
    border-right: 1px solid var(--dr-paper-soft);
    border-bottom: 1px solid var(--dr-paper-soft);
    font-family: "IBM Plex Sans", sans-serif;
    font-size: 0.87rem;
    line-height: 1.5;
    text-align: left;
    vertical-align: top;
}

#dr-report th:last-child,
#dr-report td:last-child {
    border-right: none;
}

#dr-report tr:last-child td {
    border-bottom: none;
}

#dr-report th {
    background: rgba(29, 34, 51, 0.05);
    color: var(--dr-ink);
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

/* =========================================================
   MISC
   ========================================================= */

::selection {
    background: var(--dr-brass);
    color: var(--dr-ink);
}

footer {
    display: none !important;
}

/* =========================================================
   RESPONSIVE
   ========================================================= */

@media (max-width: 760px) {
    .gradio-container {
        padding: 1.1rem 1rem 3.5rem !important;
    }

    .dr-header {
        align-items: flex-start;
        margin-bottom: 2.4rem;
    }

    .dr-header-meta {
        display: none;
    }

    .dr-query-row {
        flex-direction: column !important;
        gap: 0.4rem !important;
    }

    #dr-run {
        width: 100% !important;
        min-height: 50px !important;
    }

    #dr-examples tr {
        flex-direction: column !important;
    }

    #dr-examples td,
    #dr-examples button {
        width: 100% !important;
        max-width: none;
        transform: none !important;
    }

    #dr-report:not(:empty)::after {
        display: none;
    }
}

@media (max-width: 430px) {
    .dr-brand-copy h1 {
        font-size: 1.7rem;
    }

    .dr-brand-copy > p {
        display: none;
    }
}

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
"""

JS = """
() => {
    const initialize = () => {
        const queryInput = document.querySelector("#dr-query textarea, #dr-query input");
        const runButton = document.querySelector("#dr-run");

        if (!queryInput) {
            return false;
        }

        queryInput.focus();

        if (!queryInput.dataset.drInitialized) {
            queryInput.dataset.drInitialized = "true";

            queryInput.addEventListener("keydown", (event) => {
                const submitShortcut =
                    event.key === "Enter" && (event.ctrlKey || event.metaKey);

                if (submitShortcut && runButton) {
                    event.preventDefault();
                    runButton.click();
                }
            });
        }

        if (runButton && !runButton.dataset.drInitialized) {
            runButton.dataset.drInitialized = "true";
            runButton.setAttribute("title", "Open case file — Ctrl/Cmd + Enter");
        }

        return true;
    };

    if (!initialize()) {
        let attempts = 0;
        const interval = setInterval(() => {
            attempts += 1;
            if (initialize() || attempts >= 30) {
                clearInterval(interval);
            }
        }, 100);
    }
}
"""


# ---------------------------------------------------------------------------
# Agent hook — replace this function's body with your real agent call.
# It must be a generator (use `yield`) so the report can stream into the UI.
# ---------------------------------------------------------------------------
def run_deep_research(query: str):
    query = (query or "").strip()
    if not query:
        yield "Enter a topic above to open a case file."
        return

    # --- placeholder streaming behavior, delete once your agent is wired in ---
    yield f"# {query}\n\n*Opening file — locating sources…*"
    time.sleep(0.5)

    yield (
        f"# {query}\n\n"
        "## Summary\n\n"
        "_Replace `run_deep_research()` in app.py with a call into your agent. "
        "This placeholder just simulates a streaming report so you can see the "
        "UI end-to-end._\n\n"
        "## Findings\n\n"
        "- Point one, with a source trail\n"
        "- Point two, with a source trail\n"
        "- Point three, with a source trail\n\n"
        "## Sources\n\n"
        "1. Example Source — example.com\n"
        "2. Example Source — example.com\n"
    )


with gr.Blocks(title="DeepResearch") as demo:
    gr.HTML(HEADER_HTML)

    with gr.Row(elem_classes=["dr-query-row"]):
        query = gr.Textbox(
            placeholder="e.g. Who is quietly winning the humanoid robotics race?",
            show_label=False,
            lines=1,
            max_lines=6,
            elem_id="dr-query",
        )
        run_btn = gr.Button("Investigate", elem_id="dr-run")

    gr.HTML('<div class="dr-examples-label">Open cases</div>')
    gr.Examples(examples=EXAMPLES, inputs=query, elem_id="dr-examples")

    report = gr.Markdown(elem_id="dr-report")

    run_btn.click(run_deep_research, inputs=query, outputs=report)
    query.submit(run_deep_research, inputs=query, outputs=report)

    demo.load(None, None, None, js=JS)

if __name__ == "__main__":
    # css/head moved to launch() in Gradio >= 6.0. If you're on an older
    # Gradio (< 6.0), swap these into the `gr.Blocks(...)` constructor above
    # instead: gr.Blocks(css=CSS, head=FONT_LINKS, title="DeepResearch")
    demo.launch(css=CSS, head=FONT_LINKS)