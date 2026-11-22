# gleoba.github.io Payground
* to view, go to `https://gleoba.github.io/playground`

## Currency Converter v2

In [Currency Converter v2](currency-v2.html), **Local amount** accepts up to eight digits before the decimal separator and up to two after it. The largest amount is `99999999.99`. Enter amounts without thousands separators. Both `12.50` and `12,50` mean twelve and a half.

Typing or pasting an invalid amount keeps the previous entry and its calculations. This limit applies only to the local amount. Exchange rates retain their precision.

Converted amounts show the rate per unit of local currency rounded to two decimal places. In the Tip assistant, read down the **Tip** column to compare tips or the **Total** column to compare final amounts. A centered dot separates the two, and the local currency symbol appears on the right.

In **Configure → Add currency**, enter a currency code and its rate per unit of local currency. **Add** checks the code against Frankfurter’s catalog. For example, entering `RU` offers **Use RUB · Russian Ruble**. Choosing it keeps the entered rate and uses ₽ for the ruble. If the code is unsupported or the catalog is unavailable, choose **Add … manually** to use your own rate.

Use **Fetch latest rates** to update supported currencies in the draft. **Save & return** applies the changes; **Cancel** discards them.

The notification bar appears below the header on both screens. Routine confirmations such as **Settings saved** disappear after six seconds. Hovering over a confirmation or focusing its dismiss button gives you more time to read it.

Violet announcements stay until dismissed and can appear again after a page reload. Select an announcement to expand its details and follow its link. Orange warnings explain partial results or changes that could be lost. Red errors explain failed operations. Both stay available until you dismiss them or the affected operation is retried or superseded.

## ROADMAP

### general capabilities
* add GitHub/gh cli - MCP for agentic Issue create, PR push, release create etc.

### FUTURE of Currency

- [ ] Display the calculator's release version in the footer.
- [ ] After deploying a new version, refresh a previously opened copy on a phone and confirm the footer shows the new version.
