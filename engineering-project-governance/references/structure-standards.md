# Structure Standards

Select one standard based on the confirmed stack.

## JavaScript / TypeScript (Web App)

- `src/`: app code
- `src/components/`: UI components
- `src/pages/` or `src/routes/`: route-level views
- `src/services/`: API/service layer
- `src/store/`: state management
- `src/utils/`: pure utilities
- `public/`: static assets
- `tests/` or `__tests__/`: test code

## React + Vite

- `src/app/`: app bootstrap, providers, router
- `src/features/<feature>/`: feature modules
- `src/shared/`: shared UI/util/types
- `src/assets/`: local assets
- `tests/`: integration/e2e/unit by strategy

## Vue 3 + Vite

- `src/main.ts`: app entry
- `src/app/`: app setup, router guards
- `src/modules/<feature>/`: domain modules
- `src/shared/`: shared composables/components/utils
- `src/services/`: API clients
- `src/assets/`: assets
- `tests/`: unit/e2e

## Python

- `pyproject.toml`: project config
- `src/<package_name>/`: package source
- `src/<package_name>/api/`: API layer
- `src/<package_name>/domain/`: domain logic
- `src/<package_name>/infra/`: infrastructure adapters
- `tests/`: test suite mirrored by module

## Java (Spring)

- `src/main/java/...`: app source
- `src/main/resources/`: configs/templates
- `src/test/java/...`: tests
- `controller/`, `service/`, `repository/`, `domain/` by layered or hexagonal design

## Go

- `cmd/<app>/`: entrypoints
- `internal/`: private app packages
- `pkg/`: reusable public packages (optional)
- `configs/`: config files
- `test/` or co-located `_test.go`

## Rust

- `src/main.rs` or `src/lib.rs`: entry/library
- `src/bin/`: extra binaries
- `crates/`: workspace packages (if multi-crate)
- `tests/`: integration tests

## C# (.NET)

- `src/<ProjectName>/`: app source
- `tests/<ProjectName>.Tests/`: tests
- `Directory.Build.props`: shared build settings (optional)
- `Solution.sln`: solution root

## Monorepo

- `apps/`: deployable apps
- `packages/` or `libs/`: shared libraries
- `tools/`: scripts/tooling
- `docs/`: architecture decisions and standards
- root workspace config (`pnpm-workspace.yaml`, `turbo.json`, etc.)
