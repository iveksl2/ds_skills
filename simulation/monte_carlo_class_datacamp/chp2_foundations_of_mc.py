
n = 10000
circle_points = 0 
square_points = 0 
for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    dist_from_origin = x**2 + y**2
    # Increment circle_points for any point with a distance from origin of less than .75
    if dist_from_origin < 0.75:
        circle_points += 1
    square_points += 1
pi = 4 * circle_points / square_points
print(pi)

n = 10000
circle_points = 0 
square_points = 0 
for i in range(n):
    # Sample the x and y coordinates from -1 to 1 using random.randint()
    x = random.randint(-1,1)
    y = random.randint(-1,1)
    dist_from_origin = x**2 + y**2
    if dist_from_origin <= 1:
        circle_points += 1
    square_points += 1
pi = 4 * circle_points / square_points
print(pi)

# ------ Sampling from discrete distributions ---------
# Define low and high for use in rvs sampling below
low = 1
high = 7 # not inclusive
# Sample 1,000 times from the discrete uniform distribution
samples = st.randint.rvs(low, high, size=1000)

samples_dict = {'nums':samples}
sns.histplot(x='nums', data=samples_dict, bins=6, binwidth=0.3)
plt.show()

# ------ Sampling from a geometric distribution ----------
# Set p to the appropriate probability of success
p = .2

# Sample from the geometric distribution 10,000 times
samples = st.geom.rvs(p, size=10000)
samples_dict = {"nums":samples}
sns.histplot(x="nums", data=samples_dict)  
plt.show()

# --- simulatigng a bet ----
for p in [0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9]: 
    low = 1
    high = 7
	# Simulate rolling Tom's die 10,000 times
    die_samples = st.randint.rvs(low,high,size=10000)
	# Simulate Eva's coin flips to land heads 10,000 times
    coin_samples = st.geom.rvs(p,size=10000)
    diff = np.mean(die_samples - coin_samples)
    print(diff)

# -- Changing mean of dist-------

# --- Kinda cool pairplot -----
p_sunny = 300/365
p_cloudy = 35/365
p_rainy = 30/365
num_of_days_in_a_year = 365
number_of_years = 50

# Simulate results
days = st.multinomial.rvs(num_of_days_in_a_year,
    [p_sunny, p_cloudy, p_rainy], size=number_of_years)

# Complete the definition of df_days
df_days = pd.DataFrame({"sunny": days[:, 0],
     "cloudy": days[:, 1],
     "rainy":  days[:, 2]})
sns.pairplot(df_days)
plt.show()

## -- Multivariate normal sampling -----
mean_value = [20, 500]
sample_size_value = 5000
cov_mat = np.array([[19, 950], [950, 50000]])

# Simulate the results using sampling
simulated_results = st.multivariate_normal.rvs(mean=mean_value, size=sample_size_value, cov=cov_mat)
simulated_house_price_size = pd.DataFrame({"price":simulated_results[:,0],
                         				   "size":simulated_results[:,1]})

# Visualize the results 
sns.pairplot(simulated_house_price_size)
plt.show()

# I dont get this section
