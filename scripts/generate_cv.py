"""Generate an ATS-friendly PDF CV from portfolio content."""

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "Jorge-Mager-CV.pdf"

PORTFOLIO = "https://limbogabi.github.io/portfolio/"
LINKEDIN = "https://www.linkedin.com/in/limbogabi/"


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=16,
            leading=20,
            spaceAfter=4,
            textColor="#111111",
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            spaceAfter=10,
            textColor="#222222",
        ),
        "summary": ParagraphStyle(
            "Summary",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=13,
            spaceAfter=12,
            textColor="#222222",
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            spaceBefore=8,
            spaceAfter=6,
            textColor="#111111",
            borderPadding=0,
        ),
        "job": ParagraphStyle(
            "Job",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=13,
            spaceBefore=6,
            spaceAfter=2,
            textColor="#111111",
        ),
        "company": ParagraphStyle(
            "Company",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=12,
            spaceAfter=3,
            textColor="#333333",
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            textColor="#222222",
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            textColor="#222222",
        ),
    }


def bullets(items, s):
    return ListFlowable(
        [ListItem(Paragraph(item, s["bullet"]), leftIndent=8, value="•") for item in items],
        bulletType="bullet",
        start="•",
        leftIndent=12,
        bulletFontName="Helvetica",
        bulletFontSize=9.5,
        spaceBefore=0,
        spaceAfter=4,
    )


def build():
    s = styles()
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title="Jorge Mager - CV",
        author="Jorge Mager",
    )

    story = []
    story.append(Paragraph("Jorge Mager — CV", s["name"]))
    story.append(
        Paragraph(
            f"Phone: +972-52-473-9307 | Email: jorgemecher@gmail.com | "
            f'<link href="{LINKEDIN}">LinkedIn</link> | '
            f'<link href="{PORTFOLIO}">Portfolio</link> | '
            "Ramat Gan, Tel Aviv District, Israel",
            s["contact"],
        )
    )
    story.append(
        Paragraph(
            "Automation engineer with 10+ years building QA automation frameworks, "
            "developer tooling, and CI/CD infrastructure at Cellebrite, now focused "
            "full-time on applied, agentic AI development. Hands-on builder of full-stack "
            "production applications on the Anthropic Claude API spanning conversational "
            "reasoning, coaching/analysis, and persistent-context architectures. Fluent in "
            "the modern agentic toolchain (Claude, Claude Skills, MCP, Cursor-assisted "
            "development) and in translating ambiguous business needs into working "
            "prototypes and production builds. Track record mentoring engineers and driving "
            "AI-assisted development adoption across teams.",
            s["summary"],
        )
    )

    story.append(Paragraph("Professional Experience", s["section"]))

    story.append(Paragraph("2017 – Present — Cellebrite — Automation Developer", s["job"]))
    story.append(
        Paragraph(
            "Enterprise digital intelligence company. Building agentic AI pipelines "
            "(LangGraph-style architecture, LLM decision layers) alongside QA automation "
            "and developer tooling.",
            s["company"],
        )
    )
    story.append(
        bullets(
            [
                "Designing and building an agentic Outlook email-processing pipeline for "
                "integration-failure alerts: Outlook → n8n → Azure Service Bus → Azure "
                "Function App (Node.js/TypeScript), where an LLM reads each email plus DB "
                "history and orchestrates MCP tool calls — including Puppeteer browser "
                "automation that logs into the integration platform and auto-retries failed "
                "jobs — with runs logged to PostgreSQL for audit and future context.",
                "Architected as a multi-folder, multi-tool platform so new email sources "
                "and actions plug in without core code changes.",
                "Implemented AI-driven automation accelerators using AI-assisted development "
                "to improve engineering efficiency.",
                "Designed and implemented a BDD automation framework in JavaScript; "
                "maintain C# and Node.js automation frameworks.",
                "Built reporting services integrating third-party APIs; lead UI and API "
                "automation using WebDriverIO.",
                "Leveraged AWS automation environments; integrated GitHub Pages for QA "
                "documentation.",
                "Mentor engineers on automation, testing, and AI-assisted development; "
                "advocate for agentic and low-code AI tooling.",
            ],
            s,
        )
    )

    story.append(Paragraph("2013 – 2017 — SafeNet — Automation Leader", s["job"]))
    story.append(
        bullets(
            [
                "Developed a C# automation framework and led a small automation team.",
                "Introduced modular testing practices to improve maintainability and reuse.",
            ],
            s,
        )
    )

    story.append(Paragraph("2010 – 2013 — HP Software — QA &amp; Automation Feature Lead", s["job"]))
    story.append(
        bullets(
            [
                "Owned QA planning, testing, and reporting for feature areas.",
                "Led automation framework selection for product teams.",
            ],
            s,
        )
    )

    story.append(Paragraph("Personal Projects", s["section"]))

    story.append(
        Paragraph(
            '2015 – Present — Empathy (Tyrell) — <link href="https://shadowly.ai">shadowly.ai</link>',
            s["job"],
        )
    )
    story.append(
        bullets(
            [
                "AI companion product with zero-knowledge privacy and layered long-term "
                "memory for Daimon — Socratic, reflective conversations over months and years "
                "that build the user’s evolving “twin.”",
                "Client-side AES encryption (DEK dual-wrapped under passphrase + recovery "
                "questions); three-tier client-side memory (observations, profile synthesis, "
                "structured recall).",
                "Stack: Next.js (App Router), Vercel, Supabase, Anthropic Claude API; "
                "CI/CD with Playwright E2E, RLS, and versioned Postgres migrations.",
            ],
            s,
        )
    )

    story.append(
        Paragraph(
            'Chess Coach — <link href="https://chesscoach-app-eight.vercel.app">Live demo</link>',
            s["job"],
        )
    )
    story.append(
        bullets(
            [
                "Full-stack AI chess coaching app: PGN/FEN paste or chess.com/lichess "
                "screenshot import via Claude vision; Socratic coaching instead of direct "
                "best-move answers.",
                "Hybrid architecture: Claude for pedagogy; Stockfish + chess.js for "
                "objective evaluation, legal moves, and tool-called line simulation.",
                "Branching move-tree UI, board editor, beta access with token budgeting. "
                "Stack: Next.js, Supabase, Claude, Stockfish.",
            ],
            s,
        )
    )

    story.append(Paragraph("Core Skills", s["section"]))
    story.append(
        bullets(
            [
                "<b>Agentic AI &amp; LLM Engineering:</b> Anthropic Claude API, agentic "
                "workflow design, MCP tool integrations, prompt/system-prompt design, "
                "Claude Skills, persistent-context architecture, responsible AI practices.",
                "<b>AI-Assisted Development:</b> Claude + Cursor workflow, rapid "
                "PoC-to-production iteration, low-code/no-code AI tool evaluation.",
                "<b>Full-Stack Development:</b> Next.js/React, Node.js, TypeScript, "
                "Supabase (Postgres + Auth), REST APIs, end-to-end product architecture.",
                "<b>Automation &amp; QA:</b> C#, JavaScript/Node.js, Selenium, WebDriverIO, "
                "API testing, BDD (Gherkin), test architecture and framework design.",
                "<b>Cloud &amp; DevOps:</b> AWS, Vercel, Jenkins, GitHub Actions, CI/CD.",
                "<b>Enablement &amp; Leadership:</b> Mentorship, technical workshops, "
                "AI-adoption enablement, cross-functional collaboration.",
            ],
            s,
        )
    )

    story.append(Paragraph("Education &amp; Continuing Development", s["section"]))
    story.append(Paragraph("Software Practical Engineer", s["body"]))
    story.append(
        Paragraph(
            "Ongoing self-directed study: applied prompt engineering, agentic system "
            "design, and responsible AI practices (Anthropic technical documentation and research).",
            s["body"],
        )
    )
    story.append(Spacer(1, 6))

    story.append(Paragraph("Languages", s["section"]))
    story.append(
        Paragraph(
            "Hebrew: Native | English: Superior / full professional proficiency | Spanish: Native",
            s["body"],
        )
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
