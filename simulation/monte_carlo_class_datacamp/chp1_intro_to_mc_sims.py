# --- Sample with replacement ------
simu_weights = []

# Sample nine values from nba_weights with replacement 1000 times
for i in range(1000):
    bootstrap_sample = random.choices(nba_weights, k=9)
    simu_weights.append(np.mean(bootstrap_sample))

# Calculate the mean and 95% confidence interval of the mean for your results
mean_weight = np.mean(simu_weights)
upper = np.quantile(simu_weights, 0.975)
lower = np.quantile(simu_weights, 0.025)
print(mean_weight, lower, upper)

## ----- visualize results -----
# Plot the distribution of the simulated weights
sns.displot(simu_weights)

# Plot vertical lines for the 95% confidence intervals and mean
plt.axvline(lower, color="red")
plt.axvline(upper, color="red")
plt.axvline(mean_weight, color="green")
plt.show()

# -- Permutation Practice ----
# Define all_weights
all_weights = nba_weights + us_adult_weights
simu_diff = []

for i in range(1000):
	# Perform the permutation on all_weights
    perm_sample = np.random.permutation(all_weights)
    # Assign the permutated samples to perm_nba and perm_adult
    perm_nba, perm_adult = perm_sample[0:12], perm_sample[12:]
    perm_diff = np.mean(perm_nba) - np.mean(perm_adult)
    simu_diff.append(perm_diff)
mean_diff = np.mean(nba_weights) - np.mean(us_adult_weights) 
upper = np.quantile(simu_diff, 0.975)
lower = np.quantile(simu_diff, 0.025)
print(mean_diff, lower, upper)

# ---- Paired dice simulation -----
def roll_paired_biased_dice(n, seed=1231):
    results = {}
    random.seed(seed)
    for i in range(n):
        bag_index = random.randint(0, 1)
        dice_index1 = random.randint(0, 5)
        dice_index2 = random.randint(0, 5)
        point1 = bag1[bag_index][dice_index1]
        point2 = bag2[bag_index][dice_index2]
        key = "%s_%s" % (point1, point2)
        if point1 + point2 == 8: 
            if key not in results:
                results[key] = 1
            else:
                results[key] += 1
    return(pd.DataFrame.from_dict({"dice1_dice2":results.keys(),
		"probability_of_success":np.array(list(results.values()))*100.0/n}))

# Run the simulation 10,000 times and assign the result to df_results
df_results = roll_paired_biased_dice(10000)
sns.barplot(x="dice1_dice2", y="probability_of_success", data=df_results)
plt.show()
