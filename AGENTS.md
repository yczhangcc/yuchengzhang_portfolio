# AGENTS.md

Shared instructions for Codex, Claude Code, and other coding agents working on Yucheng (Cecilia) Zhang's portfolio.

## Project Purpose

This repository contains Cecilia's portfolio website, LaTeX resume system, and professional materials. Present her as a Software Engineer, AI/ML Engineer, Applied Researcher, Quantitative Analyst, and creative technologist with photography and painting interests.

Core narrative: an engineer who builds reliable AI systems, applies machine learning to real-world problems, and connects technical work with human-centered creativity.

## Current Structure

- `index.html`: portfolio homepage.
- `css/styles.css`: shared website styles.
- `photograph/index.html`: photography gallery page.
- `painting/index.html`: painting gallery page.
- `imgs/`: website images.
- `cv/`: LaTeX resume sources and generated website PDFs.
- `tmp/`: temporary QA artifacts.

Do not reorganize folders, rename PDF paths, or move website assets unless the user explicitly asks for a structure migration. The current website links to files under `cv/`.

## Highest Priority Rules

Accuracy beats polish. Never invent or exaggerate projects, technologies, responsibilities, metrics, publications, job titles, locations, or technical ownership. Never turn a supporting contribution into a leadership claim.

If information is uncertain, ask for clarification instead of guessing. The goal is stronger communication, not fictional enhancement.

Before modifying resume or website content, identify the audience: SWE recruiter, ML recruiter, research professor, quant recruiter, or website visitor. Then check the main message, supporting evidence, and technical accuracy.

## Resume Writing Rules

Use bullets that follow:

`Action + Technical Method + Problem Solved + Result`

Good: `Built an end-to-end credit risk modeling pipeline using SQL Server and Python, engineering borrower features and validating Logistic Regression and Random Forest models with ROC/AUC analysis.`

Bad: `Used Python and machine learning for risk analysis.`

Avoid generic AI-sounding phrases such as `leveraged cutting-edge technology`, `enhanced scalability`, `improved reliability`, `supported innovation`, and `optimized performance` unless the specific mechanism is explained.

Prefer concrete language: implemented API validation, designed database schema, automated model refresh workflow, reduced manual reporting effort, filtered LLM context before provider calls.

## Resume Versions

### Master CV

Use for the portfolio website, graduate applications, and research networking. Include complete experience, research, publications, leadership, and creative interests. Do not remove meaningful achievements just to make the page sparse.

### Software Engineering Resume

Target roles: Software Engineer, Backend Engineer, Full Stack Engineer, AI Engineer.

Prioritize system design, backend architecture, APIs, databases, frontend/backend integration, testing, deployment, and maintainable engineering workflows.

Important keywords when truthful: React, TypeScript, Flask, REST API, PostgreSQL, SQLAlchemy, Alembic, Docker, Git, testing.

### AI / ML / Data Science Resume

Target roles: ML Engineer, AI Engineer, Applied Scientist, Data Scientist, Research Engineer.

Prioritize machine learning methods, datasets, feature engineering, model evaluation, statistical analysis, LLM systems, and AI applications.

Important keywords when truthful: Python, PyTorch, TensorFlow, Scikit-learn, Machine Learning, Large Language Models (LLMs), OpenAI API, Gemini, Claude, LangChain, model evaluation, ROC/AUC.

### Quantitative / Financial Resume

Target roles: Risk Analyst, Quantitative Analyst, Financial Data Scientist, Decision Science, Fraud Analytics.

Prioritize credit risk, fraud analytics, financial data pipelines, statistical modeling, SQL analytics, Python, Power BI, ETL, and model validation.

Do not position Cecilia as a trading researcher or derivatives researcher unless the user provides evidence.

## Key Experience Facts

### CodeAssist

Describe as a full-stack AI feedback system for programming education. Students edit code, upload files, submit assignments, and receive AI chatbot feedback for debugging, algorithm complexity, test case correctness, and programming concepts.

Relevant details: React, Flask, PostgreSQL, Docker, OpenAI, Gemini, Claude, local LLM providers, instructor-configurable AI behavior, prompt templates, context permissions, model selection, usage limits, and backend authorization.

Do not describe it only as `AI settings configuration`.

### Toyota Industries Commercial Finance

Describe as applied credit risk analytics and machine learning. Use `end-to-end credit risk modeling pipeline`; do not use `full-stack credit risk pipeline`.

Relevant details: SQL Server, PayNet data, loan servicing data, ETL, feature engineering, Logistic Regression, Random Forest, ROC/AUC, backtesting, risk segmentation, Power BI reporting.

### Echo

Describe as an interactive AI voice simulation system, not a generic chatbot.

Facts: University of Texas at Austin; Mentor: Prof. Bo Xie; Austin, TX; Jun. 2026 - Present.

Relevant details: Next.js, TypeScript, OpenAI API, browser TTS, event-driven responses, AI-generated voice interaction.

### FinChat

Describe as an AI-powered financial analysis system.

Facts: Dallas, TX (Remote Hybrid). Relevant details: SEC filings, EDGAR extraction, financial data processing, LLM workflows, LangChain, CrewAI.

### Kiwifruit Quality Grading

Describe as a machine learning computer vision research project.

Facts: Wuhan, China (Hybrid). Relevant details: image feature extraction, color/texture/shape analysis, model evaluation, published research.

## ATS Compatibility

All resumes must work for both Applicant Tracking Systems (ATS) and human reviewers.

Maintain ATS-friendly formatting:

- single-column layout
- standard section headings such as `Education`, `Technical Skills`, `Work Experience`, `Research Experience`, `Projects`, and `Publications`
- searchable text, not resume text embedded only in images
- clear company names, titles, dates, locations, technologies, and project names
- conservative typography and simple bullets

Avoid multi-column layouts, text boxes for important content, icons replacing text, images containing resume text, decorative graphics, unusual fonts, and headers/footers containing critical information only.

Use complete keywords naturally at least once when truthful:

- `Machine Learning`, not only `ML`
- `Large Language Models (LLMs)`, not only `LLM`
- `PostgreSQL`, not only `Postgres`
- `REST API`, not only `API`

Before finalizing resume changes:

- edit `.tex` source files, not PDFs directly
- compile PDFs from source
- verify intended page count
- extract text with a parser such as `pdfplumber` or `pypdf`
- confirm extracted text includes name, contact, education, company names, titles, dates, locations, skills, and project names
- visually inspect rendered PDF pages for spacing, clipping, overlap, or unreadable glyphs
- keep generated PDFs synchronized with LaTeX source

## Website Guidelines

The website should feel like `AI researcher + engineer + artist`.

Style: professional, minimal, elegant, research-oriented, visually strong.

Avoid hacker themes, excessive animations, generic developer templates, and decorative effects that distract from the work.

Recommended sections: Home, About, Research, Engineering, Publications, Photography, Painting, Resume, Contact.

Photography and painting are part of Cecilia's identity. Keep them visually connected to the portfolio but separate from engineering content.

## Code Rules

When changing website code, preserve existing functionality and links, keep HTML/CSS readable, avoid unnecessary dependencies, avoid duplicated copy or logic, and consider responsive behavior.

Before major changes, explain affected files, reason for the change, and likely risks. After changes, report files modified, functionality changed, and validation performed.

## Decision Priority

1. Accuracy
2. Technical correctness
3. Clear communication
4. Recruiter readability
5. ATS compatibility
6. Visual quality
7. Conciseness
