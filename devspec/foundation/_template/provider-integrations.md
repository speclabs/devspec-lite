# Provider Integrations

Use this policy to resolve external work items during `/devspec.story`. Keep provider-specific lookup behind MCP servers or equivalent integration tools. Manual intake is an explicit fallback, available only when provider resolution is unavailable or intentionally skipped.

## Resolution Policy

| Policy area | Requirement |
|---|---|
| Workflow boundary | Keep work-item intake provider-agnostic; provider-specific lookup belongs in integration tools. |
| Resolution preference | Prefer exact provider URLs or provider-qualified identifiers over inferred matches. |
| Ambiguity handling | Ask one structured clarification before resolving an ambiguous provider or identifier. |
| Manual fallback | Allow manual intake only when external resolution is unavailable and the developer explicitly chooses to proceed. |
| Work-item creation gate | Do not create or update the work-item folder from provider input until the resolved item is shown to the developer and explicitly confirmed. |
| Secret handling | Keep provider authentication, credentials, and secrets outside prompt artifacts. |

## Supported Provider Inputs

| Provider | Preferred input | Accepted shorthand | Validation guardrail |
|---|---|---|---|
| GitHub | Full issue URL or supported pull request URL | `owner/repo#123` | Reject bare numbers unless repository context is configured. |
| Jira | Full issue URL | Issue key such as `ABC-123` | Reject malformed keys or keys outside configured project patterns. |
| Azure DevOps | Full work item URL | Numeric ID only with configured organization and project context | Reject numeric IDs when organization or project context is missing. |
| GitLab | Full issue URL | Provider-qualified identifier | Reject shorthand without configured project context. |

## Resolution Outcomes

| Condition | Required handling |
|---|---|
| Invalid input format | Stop intake and explain why the input is invalid. |
| Ambiguous provider | Ask one structured clarification to identify the provider. |
| Known provider cannot resolve item | Stop intake and classify the failure as not found, access denied, or integration unavailable when possible. |
| Integration unavailable | Offer manual intake as an explicit fallback. |
| Provider resolution succeeds | Show the confirmation summary and require structured confirmation before creating or updating the work-item folder. |
| Unverified provider input | Treat as blocked or manual fallback only; do not create a normal resolved work item. |

## Confirmation Requirements

Show provider, identifier, title, type when available, current external status when available, canonical link, and short summary. Ask one interactive multiple-choice question with these actions: Confirm and continue, Reject and retry input, Switch to manual intake, Cancel, and Custom Answer. Give every action an example, show exactly one recommendation and justification, and do not create or update the work-item folder until confirmation.

## Integration Tooling and Access

| Area | Requirement |
|---|---|
| Tooling model | Use a provider-specific MCP server or one internal MCP server that wraps multiple providers. |
| Lookup tools | Validate and fetch work items by URL or provider-specific identifier. |
| Returned data | Include title, description, status, labels or type, links, and relevant metadata. |
| Failure detail | Distinguish not found, unauthorized, malformed input, and transient provider failures. |
| Authentication configuration | Keep provider authentication outside prompt artifacts. |
| Privilege model | Use least-privilege tokens or service identities. |
| Access mode | Prefer read-only access for intake and review unless write-back is separately required. |