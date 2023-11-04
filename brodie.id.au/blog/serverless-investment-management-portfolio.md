```{post} 22 November, 2024
:author: Brodie Blackburn
```
# Serverless investment management portfolio

```{figure} portfolio-demo.png
:alt: Index worksheet

[portfolio-demo.brodie.id.au](https://portfolio-demo.brodie.id.au)
```

I built a system that helps manage investments.

It does the following things:
- Automatically retrieves account balances and asset prices from various financial institutions.
- Maintains an ever-increasing ledger of balances over time.
- Creates a database containing asset values normalised to an AUD basis.
- Delegates painful emotional decisions to a robot.
- Executes a pre-determined portfolio strategy to determine how to re-orient (you still have to pull the trigger).
- Builds a single pane of glass showing key stats.
- Deploys to AWS for approximately 0 dollars (except maybe 50c per month if you don't already have a Route 53 zone).

You can check out a demo with example data [here](https://portfolio-demo.brodie.id.au),
and view source code [here](https://github.com/eidorb/portfolio).


## Investment strategy

I realised cash savings are *guaranteed* to lose value over time.
I needed to take on some risk.
The timeframe is long-term, however.
There are *guaranteed* to be ups and downs. Volatility.

If the goal is long-term than this system better be hands-off, simple and not psychologically difficult.
I've decided on some allocation between risky and less risky asset classes. The mix of which is in accordance with my personal risk tolerance.

This Bogle fella has some interesting [ideas](https://www.bogleheads.org/wiki/Rebalancing).


## The system

Several times a month, GitHub Actions triggers automated workflows.


## A plain-text ledger

Balances are written to a Beancount ledger (it's just a text file).
With Beancount you'd typically track *all* of your transactions, not just balances.
Usually the hard work is all in categorising transactions.
If we stick to just balances, it's pretty simple to automate.

Sometimes automatic retrieval breaks.
These shitty bank websites change all the time 🤣!
(At least there's [Up](https://developer.up.com.au).)

Beancount ledgers are easily updated by hand. Balance entries looks like this:

```
2023-11-26 balance Assets:Bank:Savings                              20000.0 AUD
2023-11-26 balance Liabilities:Bank:CreditCard                     -5000.0 AUD
```

It's simple to add manual entries until there's time to rework the retrieval code.

Simon Willison's concept of [Git scraping](https://simonwillison.net/2020/Oct/9/git-scraping/) is pretty cool!
Just keeping data in plain text files.
Updates are infrequent enough so it simply rebuilds the database and website every update.
GitHub Actions can make git commits on your behalf so your ledger stays up-to-date 💃.

Oh, and if those Fort Knox banks (secured with single-factor authentication) try to block your connections originating from GitHub's ASN, you can just re-route your "hacking" via home using a lightweight [VPN](https://tailscale.com)!


## Infrastructure costs

Scaling to zero is economical.

The website will have many dozens of views per month.
It's not running when you're not looking at it.
It turns out you can wrap entire Python web applications with a Lambda Function.

The downside is potentially having to wait a needless couple of hundred milliseconds.


## Security

I should be in control of who sees my financial information. There's a [Datasette plugin](https://datasette.io/plugins/datasette-auth-github) that handles this.
