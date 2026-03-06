# Web — React Frontend

Frontend application for the Happy Bank project, built with React 19, TypeScript, Vite, Tailwind CSS v4, and shadcn/ui.

The chosen technologies are:
- **React 19**: UI library for building component-based interfaces.
- **TypeScript**: Typed superset of JavaScript for safer, more maintainable code.
- **Vite**: Fast build tool and dev server with hot module replacement.
- **Tailwind CSS v4**: Utility-first CSS framework.
- **shadcn/ui**: Accessible, composable UI components built on Radix UI.
- **React Router v7**: Client-side routing.
- **Sonner**: Toast notifications.

## Requirements

- **Node.js** v20 or higher (includes npm)
- **Backend** running on `http://localhost:8000` — API calls to `/api/*` are proxied automatically during development

## Install Node.js

If you don't have Node.js installed, the recommended way is to use `nvm` (Node Version Manager).

- On Unix based systems (macOS, Linux):

    ```bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
    ```

    Then restart your terminal and install Node.js:

    ```bash
    nvm install 20
    nvm use 20
    ```

- On Windows, download and run the installer from [nodejs.org](https://nodejs.org).

Verify the installation:

```bash
node -v
npm -v
```

## Setup and run

1. Navigate to the web directory:

    ```bash
    cd resources/web
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Start the development server:

    ```bash
    npm run dev
    ```

Open your browser and navigate to `http://localhost:5173` to access the application.

## Available scripts

| Command | Description |
|---|---|
| `npm run dev` | Start the dev server with HMR at `http://localhost:5173` |
| `npm run build` | Type-check and build for production (output → `dist/`) |
| `npm run preview` | Serve the production build locally for preview |
| `npm run lint` | Run ESLint |

## Project structure

```
src/
  components/
    ui/           # shadcn/ui primitives (auto-generated, do not edit manually)
    AppLayout.tsx # Root layout with sidebar and breadcrumbs
  pages/          # Route-level page components
  services/       # API call functions
  types/          # Shared TypeScript types
  main.tsx        # Application entry point
```

Path alias `@` resolves to `src/`, e.g. `import { Button } from '@/components/ui/button'`.

## dist folder

The `dist/` folder contains a **pre-built production bundle** and is committed to the repository intentionally.

This allows contributors who are not working on the frontend (e.g. backend developers) to run the full application without needing Node.js or any frontend tooling — the backend serves the static files from `dist/` directly.

> If you make changes to the frontend source, run `npm run build` and commit the updated `dist/` folder so it stays in sync with the source code.
