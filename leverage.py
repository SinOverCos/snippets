"""
How much extra money can be made from leveraging up?
"""


import matplotlib.pyplot as plt


STARTING_CAPITAL = 270000
LEVERAGE = 1.1
MARGIN_INTEREST = 0.0633
DIVIDEND_YIELD = 0.0143
DIVIDEND_TAX_RATE = 0.34 # 20% federal + 10% NYS + 4% NYC
RETURN = 0.08
ADDITIONAL_PRINCIPAL = 120000
MARGINAL_TAX_RATE = 0.35 + 0.0685 + 0.03876
YEARS_LEFT = 37

leveraged_net_worth = [STARTING_CAPITAL]
unleveraged_net_worth = [STARTING_CAPITAL]

for _ in range(YEARS_LEFT - 1):
    # Levered.
    levered_portfolio_worth = leveraged_net_worth[-1]
    loan = (LEVERAGE - 1) * levered_portfolio_worth
    levered_portfolio_worth += loan

    dividends = levered_portfolio_worth * DIVIDEND_YIELD
    true_dividends = dividends * (1 - DIVIDEND_TAX_RATE)
    returns = levered_portfolio_worth * RETURN

    interest = MARGIN_INTEREST * loan
    true_interest_cost = (1 - MARGIN_INTEREST) * interest

    levered_portfolio_worth += true_dividends
    levered_portfolio_worth += returns
    levered_portfolio_worth -= true_interest_cost
    levered_portfolio_worth += ADDITIONAL_PRINCIPAL
    leveraged_net_worth.append(levered_portfolio_worth - loan)

    # Unlevered.
    unlevered_portfolio_worth = unleveraged_net_worth[-1]
    dividends = unlevered_portfolio_worth * DIVIDEND_YIELD
    true_dividends = dividends * (1 - DIVIDEND_TAX_RATE)
    returns = unlevered_portfolio_worth * RETURN

    unlevered_portfolio_worth += true_dividends
    unlevered_portfolio_worth += returns
    unlevered_portfolio_worth += ADDITIONAL_PRINCIPAL
    unleveraged_net_worth.append(unlevered_portfolio_worth)


years = list(range(2024, 2024 + YEARS_LEFT))

for y, (u, l) in enumerate(zip(unleveraged_net_worth, leveraged_net_worth)):
    print(f"Year {y}: {u/1000000:.1f}M vs. {l/1000000:.1f}M (${int(l-u)} more money / {100*(l/u-1):.2f}% more)")

plt.plot(years, unleveraged_net_worth, linestyle='--', marker='o', label="Unlevered")
plt.plot(years, leveraged_net_worth, linestyle='--', marker='o', label=f"{LEVERAGE}x Levered")
plt.xlabel("Year")
plt.ylabel("Net Worth")
plt.legend()
plt.title("Net worth comparison")
plt.show()

