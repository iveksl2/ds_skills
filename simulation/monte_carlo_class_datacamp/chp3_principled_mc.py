# Create a pairplot of tc, ldl, and hdl
sns.pairplot(dia[['tc', 'ldl', 'hdl']])
plt.show()

# Calculate correlation coefficients
print(dia[['tc', 'ldl', 'hdl']].corr())

# --- Try Dist -----
distributions = [st.uniform, st.norm, st.expon]
mles = []
for distribution in distributions:
    # Fit the distribution and obtain the MLE value
    pars = distribution.fit(dia['age'])
    mle = distribution.nnlf(pars, dia['age'])
    mles.append(mle)
print(mles)

sns.histplot(clerk_data)
plt.show()

# Define a list of distributions to evaluate: uniform, normal and exponential
distributions = [st.uniform, st.norm, st.expon]
mles = []
for distribution in distributions:
    # Fit each distribution, extract the MLE value, and append it to mles
    pars = distribution.fit(clerk_data)
    mle = distribution.nnlf(pars, clerk_data)
    mles.append(mle)
print(mles)


