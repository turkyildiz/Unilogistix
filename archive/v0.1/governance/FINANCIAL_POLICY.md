# Financial policy

Version 0.1 | Proposed internal controls

## Purpose and activation

Finance serves reliable operations and durable ventures. This policy defines proposed operational controls, not investment, tax, or jurisdiction-specific accounting advice.

Before monetary activity, record the authorized account owner, currency, funding source, signatory or delegated access, applicable accounting setup, and the venture's adopted budget. No account access or spending authority is created by this document.

## Budget controls

Track cash, realized receipts, accrued costs, reserved commitments, liabilities, and forecast expenditure separately. Forecast revenue is not cash.

Check every commitment against per-action, period, recurring, venture, and portfolio caps. Include taxes, fees, foreign-exchange allowances, cancellation terms, and the full committed period where applicable. Do not split purchases to evade a limit.

Reserve funds atomically before an action so concurrent agents cannot spend the same balance. Release unused reservations on confirmed cancellation or failure. Unknown payment status must be reconciled before retrying; use idempotency controls to prevent duplicate charges.

Provider-level quotas and payment controls should enforce caps independently of the model.

## Payments and collections

Use approved providers and allowlisted counterparties. Verify changed payment destinations through a trusted channel independent of the change request. Require distinct AI verification for disbursements and account changes.

Issue invoices and apply pricing, credits, collections, refunds, and chargeback responses only within adopted customer and financial limits. Preserve the source document, authorization, transaction reference, ledger entry, and reconciliation outcome.

Never commit credentials or raw financial records to this public repository.

## Capital allocation

AI finance may allocate resources within an explicit portfolio envelope, preserving each venture's customer obligations and required reserve. Cross-venture transfers require recorded allocation authority and entries in both ventures' records.

Debt, guarantees, equity, ownership changes, and commitments exceeding delegation go to the board. Investing treasury assets or speculative trading requires a separate explicit mandate; it is not implied by authority to control business finances.

## Close and reporting

Reconcile active payment accounts daily by default; produce a monthly close covering revenue, expenses, commitments, receivables, payables, cash movement, and venture allocations. Flag unreconciled items rather than inventing balances.

Forecast runway using documented assumptions and scenarios. Include model and infrastructure usage, warranty or return exposure, support, supplier commitments, and shared parent costs.

If a limit is reached or funds are uncertain, stop new discretionary commitments, preserve previously funded essential obligations, and notify the board with options. Finance agents cannot raise their own caps.
