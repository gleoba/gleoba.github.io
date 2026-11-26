# Currency Converter

Enter a bill in the local currency to see its value in your other currencies and compare four tip options. Both versions run in your browser and save settings on the device.

| Version | First appearance on GitHub Pages | Calculator |
| --- | --- | --- |
| [v1](#v1) | [August 29, 2026](https://github.com/gleoba/gleoba.github.io/actions/runs/33259238598/job/99118279725) | [Open v1.0.0 archive](https://gleoba.github.io/playground/versions/currency-v1.0.0.html) |
| [v2](#v2) | [November 22, 2026](https://github.com/gleoba/gleoba.github.io/actions/runs/45032462118/job/137239038369) | [Open preview](https://gleoba.github.io/playground/preview/currency.html) |

[Open the stable calculator](https://gleoba.github.io/playground/currency.html) · [Read the changelog](#changelog)

## v1

The original calculator pairs instant conversions with manually maintained exchange rates. It starts with **CZK** as the local currency and includes **ILS**, **EUR**, and **USD**. [Original commit](https://github.com/gleoba/gleoba.github.io/commit/0fa300b567ce4bf8e16526c0be2d60c07fa125e0)

- **Convert a bill.** Type the local amount once. Each currency row shows the converted amount and the rate for one unit of local currency.
- **Compare tips.** Four color-coded rows show the bill, tip, and total at **7%, 10%, 12%, and 15%**.
- **Manage currencies.** Choose **Configure** to change the local currency, add or remove currencies, and edit rates by hand. **Save & Return** keeps edits in this browser. **Cancel** discards ordinary edits. To restore the original currencies and rates, tap **Reset to Defaults** twice to confirm.

## v2

**Preview.** V2 has been verified on mobile and is available for testing. The installed calculator URL currently serves v1.

V2 adds on-demand rate updates and currency lookup. The current version also makes totals easier to compare and explains what happened when a lookup or save fails. [Original v2 pull request](https://github.com/gleoba/gleoba.github.io/pull/3) · [Subsequent improvements](https://github.com/gleoba/gleoba.github.io/pull/4)

> [!TIP]
> If you used v1 in this browser, open v2 here too. On first use, v2 imports your saved local currency, currency list, and rates.

### Fetch rates and add currencies

1. Open **Configure** using the gear in the upper-right corner. Select your local currency.
2. Choose **Fetch latest rates** to get Frankfurter reference rates for the currencies in your list. The result shows the quote dates. If a quote is missing, your existing entry is kept. You can also enter rates manually.
3. To add a currency, enter its code and its rate per unit of local currency, then choose **Add**. For example, entering `RU` offers **Use RUB · Russian Ruble** and fills in **₽** when selected. If the code is unsupported or the catalog is unavailable, choose **Add … manually**.
4. Choose **Save & return** to apply the draft or **✕** to cancel. Fetched rates and **Reset to defaults** take effect when you save.

### Enter an amount and read the results

- **Local amount** accepts up to eight whole digits and two decimal places, without thousands separators. The largest amount is `99999999.99`. Both `12.50` and `12,50` mean twelve and a half. An invalid edit or paste preserves the previous amount and calculations.
- **Converted amounts** show the rate beside the currency code, for example **ILS** followed by **0.15 for 1 CZK**. The displayed rate is rounded to two decimals. Saved rates and calculations retain their precision.
- **Tip assistant** lines up the **Tip** and **Total** columns across all four percentages. A centered dot separates the columns, and the local currency symbol appears on the right. On phones the panels stack. On wider screens conversions and tips appear side by side.

### Notifications

The notification bar appears below the header on both screens. Select a message with a disclosure arrow to expand its details. The release announcement links to this guide in a separate tab.

| Message | What to expect |
| --- | --- |
| **Information** | Routine confirmations such as **Settings saved** disappear after six seconds. Hover over the message or focus its dismiss button to pause the timer. |
| **Announcement** (violet) | Stays until dismissed. Once closed, it can appear again on the next page reload. |
| **Warning** (orange) | Explains partial results or changes that could be lost, such as a missing quote or unavailable browser storage. |
| **Error** (red) | Explains a failed operation and how to recover, such as retrying a fetch or entering rates manually. |

Warnings and errors remain available until dismissed or until the affected operation is retried or superseded. Screen readers announce updates, and the disclosure and dismiss controls work with a keyboard.

## Release process

Plan work in the version milestone, develop it on a feature branch, and attach its PRs to the milestone. Use the `currency` label for the app and `preview` or `stable` for the release stage. The [v1 milestone](https://github.com/gleoba/gleoba.github.io/milestone/1) is closed. The [v2 milestone](https://github.com/gleoba/gleoba.github.io/milestone/2) stays open through [stable promotion](https://github.com/gleoba/gleoba.github.io/issues/6).

1. Tag the tested commit using `currency-vMAJOR.MINOR.PATCH`. For a test build, append `-alpha.N`, `-beta.N`, or `-rc.N` and publish it as a GitHub **pre-release**. The tagged commit supplies `playground/currency-vMAJOR.html`. Historical v1 uses `playground/currency.html`.
2. Publishing a Currency Release dispatches the Pages workflow on `master`. Every deployment builds the whole site and selects the highest stable currency version for `/playground/currency.html`. The preview URL serves the highest version including pre-releases. A final release takes precedence over a pre-release of the same version.
3. To promote a verified build, publish a stable tag at that commit. Every stable build also has a permanent archive at `/playground/versions/currency-vMAJOR.MINOR.PATCH.html`. Check the installed URL and close the milestone after promotion.
4. For a retrospective tag whose commit predates the release workflow, run **Deploy gleoba.github.io site to GitHub Pages** on `master` manually. A manual run uses the same release selection rules.

## Changelog

### November 26, 2026 — v2.0.0 beta 2

- New installs and **Reset to defaults** use the November 26 reference rates. One USD buys 22.319 CZK, 3.3631 ILS, or 0.91312 EUR. Existing settings keep their saved rates. [Dated Frankfurter quotes](https://api.frankfurter.dev/v2/rates?base=USD&date=2026-11-26&quotes=CZK,ILS,EUR)
- The first time you open **Configure** after loading the page, a reminder points to **Fetch latest rates**. Reloading the page makes the reminder available again. [Issue #8](https://github.com/gleoba/gleoba.github.io/issues/8)

### November 26, 2026 — Stable and preview channels

- Recorded the original v1 commit as the stable release and the mobile-verified v2 commit as a beta. The dates above record the original Pages deployments. [v1.0.0 release](https://github.com/gleoba/gleoba.github.io/releases/tag/currency-v1.0.0) · [v2.0.0 beta 1 pre-release](https://github.com/gleoba/gleoba.github.io/releases/tag/currency-v2.0.0-beta.1)
- Kept existing installations on v1 at `/playground/currency.html` and moved v2 testing to `/playground/preview/currency.html`. The playground links to both.
- Updated the Pages build to preserve playground subdirectories and include the stable calculator, preview, and stable archives in each site deployment.
