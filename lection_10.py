import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = pd.read_csv("penguins.csv")
print(penguins.head())
print(penguins.columns)
print(penguins.describe())
print(penguins.isnull().sum())
penguins.dropna(inplace=True)
print(penguins.head())
print(penguins.isnull().sum())
# sns.scatterplot(data=penguins, x="species", y="body_mass_g", hue="sex")
# sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species", style="sex")
# sns.PairGrid(penguins, hue='species').map(sns.scatterplot).add_legend()
# sns.heatmap(data=penguins.corr(numeric_only=True), annot = True, vmin=-1, vmax=1, center= 0, cmap= 'crest',
#             cbar_kws= {'orientation': 'horizontal'})
# df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
# df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
# df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'
penguins.loc[penguins['bill_length_mm'] >= 42, "bill_size"] = "high"
penguins.loc[(penguins['bill_length_mm'] >= 35) & (penguins['bill_length_mm'] < 42), "bill_size"] = "middle"
penguins.loc[penguins['bill_length_mm'] < 35, "bill_size"] = "low"

sns.histplot(data=penguins, x="flipper_length_mm", hue="bill_size")
plt.show()