# Currency Converter

Enter a bill in the local currency to see its value in your other currencies and compare four tip options. Both versions run in your browser and save settings on the device.

| Version | Original release on GitHub Pages | Calculator |
| --- | --- | --- |
| [v1](#v1) | [August 29, 2026](https://github.com/gleoba/gleoba.github.io/actions/runs/33259238598/job/99118279725) | [Open v1](https://gleoba.github.io/playground/currency.html) |
| [v2](#v2) | [November 22, 2026](https://github.com/gleoba/gleoba.github.io/actions/runs/45032462118/job/137239038369) | [Open v2](https://gleoba.github.io/playground/currency-v2.html) |

## v1

The original calculator pairs instant conversions with manually maintained exchange rates. It starts with **CZK** as the local currency and includes **ILS**, **EUR**, and **USD**. [Original commit](https://github.com/gleoba/gleoba.github.io/commit/0fa300b567ce4bf8e16526c0be2d60c07fa125e0)

- **Convert a bill.** Type the local amount once. Each currency row shows the converted amount and the rate for one unit of local currency.
- **Compare tips.** Four color-coded rows show the bill, tip, and total at **7%, 10%, 12%, and 15%**.
- **Manage currencies.** Choose **Configure** to change the local currency, add or remove currencies, and edit rates by hand. **Save & Return** keeps edits in this browser. **Cancel** discards ordinary edits. To restore the original currencies and rates, tap **Reset to Defaults** twice to confirm.

## v2

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
