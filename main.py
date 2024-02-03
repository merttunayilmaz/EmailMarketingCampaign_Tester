# Question 1

import pandas as pd
import scipy.stats as stats

# Question 2

# Reading the dataset with pandas
data = pd.read_csv('Data/email_marketing.csv')

# Question 3

# Getting the first 10 rows from the start
first_ten = data.head(10)

# Getting the first 10 rows from the end
last_ten = data.tail(10)

print("First 10 Rows from the Start:\n", first_ten)
print("\nFirst 10 Rows from the End:\n", last_ten)

# Separating data for Campaign A and B
campaign_a = data[data['Kampanya'] == 'Kampanya A']
campaign_b = data[data['Kampanya'] == 'Kampanya B']

# Checking sample sizes for both campaigns
n_campaign_a = campaign_a.shape[0]
n_campaign_b = campaign_b.shape[0]

print(n_campaign_a, n_campaign_b)

# Question 4a

# Levene's test for variance homogeneity
levene_eao = stats.levene(campaign_a['Eposta_Acilma_Orani'], campaign_b['Eposta_Acilma_Orani'])
levene_to = stats.levene(campaign_a['Tıklama_Orani'], campaign_b['Tıklama_Orani'])
levene_sam = stats.levene(campaign_a['Satin_Alma_Miktari'], campaign_b['Satin_Alma_Miktari'])

print(levene_eao, levene_to, levene_sam)

# Question 4b

# t-test for Email Open Rates
t_stat_eao, p_value_eao = stats.ttest_ind(campaign_a['Eposta_Acilma_Orani'], campaign_b['Eposta_Acilma_Orani'])

# t-test for Click Rates
t_stat_to, p_value_to = stats.ttest_ind(campaign_a['Tıklama_Orani'], campaign_b['Tıklama_Orani'])

# t-test for Purchase Amounts
t_stat_sam, p_value_sam = stats.ttest_ind(campaign_a['Satin_Alma_Miktari'], campaign_b['Satin_Alma_Miktari'])

# Test statistics and p-values
print(t_stat_eao, p_value_eao, t_stat_to, p_value_to, t_stat_sam, p_value_sam)

# Question 5
# Re-evaluating the significance of t-test results at 5% significance level
# This involves reviewing the previously obtained p-values and determining whether they are less than 0.05.
# If p_value < 0.05, the result is significant at the 5% level.