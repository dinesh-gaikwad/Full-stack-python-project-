# DSG Developer — Neuro Arcade X v2

A large, polished, runnable full-stack developer learning + arcade platform rebuilt from the supplied WhatsApp/Meta AI transcript. Branding is **DSG Developer**.

## What is inside

- 150 game catalog entries with IDs, categories, modes, difficulty and XP rewards
- 35 learning/workspace modules
- Dashboard with XP, level, wins and mission cards
- Searchable cheat-sheet engine
- HTML, CSS, JavaScript, Python, React, Node, Django, SQL, MongoDB, DSA and AI/ML labs
- Career roadmaps
- Project Factory for portfolio projects
- Code Snippet Vault
- Render Deployment Center
- Level Editor / Creator Lab
- Marketplace route
- Analytics dashboard
- Local notes
- Developer profile
- LocalStorage progression
- Responsive premium dark/neon UI
- Express API: /api/health, /api/meta, /api/games, /api/modules, /api/feedback
- render.yaml Blueprint
- Dockerfile
- environment template
- smoke test script

## Local run

```bash
npm install
npm start
```

Open http://localhost:10000

## VS Code

1. Extract the ZIP.
2. Open the extracted folder in VS Code.
3. Open terminal.
4. Run `npm install`.
5. Run `npm start`.
6. Open `http://localhost:10000`.

## Render deployment

This project is prepared as a Node Web Service. In Render, connect the GitHub repository and use:

- Runtime: Node
- Build Command: `npm install`
- Start Command: `npm start`
- Health Check: `/api/health`
- Root Directory: repository root

The included `render.yaml` can also be used as a Blueprint.

## GitHub

Suggested repository name:
`dsg-neuro-arcade-x`

Suggested commit:
`feat: launch DSG Developer Neuro Arcade X v2`

## Branding

Developer: **DSG Developer**
Product: **Neuro Arcade X**
Version: **2.0.0**

## Production expansion

The current package is deliberately dependency-light and runnable. For a production release, connect MongoDB/Postgres for persistent users, JWT/OAuth for authentication, object storage for creator assets, Socket.io/WebRTC for real-time features, and a CI pipeline for tests and deployment.
