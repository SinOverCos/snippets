"""
Inspired by Messenger conversation with John Piasetzki on 30 December 2022.

https://www.reddit.com/r/Bogleheads/comments/up5j06/comment/i8jkata/?context=1

Re: deferring income tax (tax loss harvesting), it's basically a tax-free loan
from the IRS. This is a script that demonstrates how much value that tax-free
loan is worth (assuming you can defer for a long time, it's basically free
money). The answer is that if you can defer for a long time, the IRS has
basically given you free money.
"""


import math
import matplotlib.pyplot as plot


def present_value(amount, rate=1.08, years=30, verbose=True):
    value_in_30_years = int((rate**years) * amount)
    profit = value_in_30_years - amount
    profit_present_value = int(profit / (rate**years))
    if verbose:
        print(
            f"{amount:,} deferred {years} years at a {rate} rate is worth "
            f"{value_in_30_years:,} in future. The {profit:,} profit is worth "
            f"{profit_present_value:,} today."
        )
    return profit_present_value


amounts = list(range(25000, 500001, 25000))
present_values = [present_value(amount) for amount in amounts]
plot.plot(amounts, present_values)
plot.xlabel("Deferred Amount")
plot.ylabel("Worth Today")
plot.show()
