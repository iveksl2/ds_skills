# List candidate distributions to evaluate
list_of_dists = ["laplace", "norm", "expon"]
for i in list_of_dists:
    dist = getattr(st, i)
    # Fit the data to the probability distribution
    param = dist.fit(dia['ldl'])
    # Perform the ks test to evaluate goodness-of-fit
    result = st.kstest(dia['ldl'], i, args=param)
    print(result)

# -- sensitivity analysis ----
def profit_next_year_mc(mean_inflation, mean_volume, n):
  profits = []
  for i in range(n):
    # Generate inputs by sampling from the multivariate normal distribution
    rate_sales_volume = st.multivariate_normal.rvs(mean=[mean_inflation,mean_volume], cov=cov_matrix,size=1000)
    # Deterministic calculation of company profit
    price = 100 * (100 + rate_sales_volume[:,0])/100
    volume = rate_sales_volume[:,1]
    loan_and_cost = 50 * volume + 45 * (100 + 3 * rate_sales_volume[:,0]) * (volume/100)
    profit = (np.mean(price * volume - loan_and_cost))
    profits.append(profit)
  return profits

# Run a Monte Carlo simulation 500 times using a mean_inflation of 2 and a mean_volume of 500
profits = profit_next_year_mc(2, 500, 500)

# Create a displot of the results
sns.displot(profits)
plt.show()

# Complete the hexbin to visualize sensitivity analysis results
df_sa.plot.hexbin(x='Inflation',
     y='Volume',
     C='Profit',
     reduce_C_function=np.mean,
     gridsize=10,
     cmap="viridis",
     sharex=False)
plt.show()
