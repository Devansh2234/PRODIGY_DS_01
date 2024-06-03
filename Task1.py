import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_excel('/Users/dhartipatel/Documents/GitHub/PRODIGY_DS_01/Data.xlsx')

print(list(data.columns))
data = data.astype(object)

data = data.drop("Country Code", axis=1)
data = data.drop("Series Name", axis=1)

#Extracted top Fifteen countries of total population


# Filter data for total population
total_population_data = data[data["Series Code"] == "SP.POP.TOTL"]

# Sort data based on the total population for 2022
total_population_sorted = total_population_data.sort_values(by= '2022 [YR2022]', ascending=False)

# Get the top Fifteen countries with the highest total population for 2022
total_top_Fifteen_countries = total_population_sorted.head(15)
print("Top Fifteen countries of total population")
print(total_top_Fifteen_countries )

def add_value_labels(ax, spacing=15):

    # For each bar: Place a label    
    for rect in ax.patches:
        
        # Get X and Y placement of label from rect.
        x = rect.get_x() + rect.get_width() / 2
        y = rect.get_height()-3

        # Determine vertical alignment for positive and negative values
        va = 'bottom' if y >= 0 else 'top'

        # Format the label to one decimal place
        label = "{}".format(y)

        # Determine the vertical shift of the label
        # based on the sign of the y value and the spacing parameter
        y_shift = spacing * (1 if y >= 0 else -1)

        # Create the annotation
        ax.annotate(label, (x, y), xytext=(0, y_shift),textcoords="offset points", ha='center', va=va)



#Top Fifteen countries of total population in year 2022 and 2016
        
# Create the bar plot
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x='2022 [YR2022]', y="Country Name", data=total_top_Fifteen_countries)
plt.title("Top Fifteen Countries of Total Population (2022)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2016 [YR2016]', y="Country Name", data=total_top_Fifteen_countries)
plt.title("Top Fifteen Countries with Total Population (2016)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()



#Top Fifteen countries of total population in year 2010 and 2001

# Create the bar plot
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x='2010 [YR2010]', y="Country Name", data=total_top_Fifteen_countries)
plt.title("Top Fifteen Countries of Total Population (2010)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2001 [YR2001]', y="Country Name", data=total_top_Fifteen_countries)
plt.title("Top Fifteen Countries with Total Population (2001)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()




#Extracted bottom Fifteen countries of total population

# Sort data based on the total population for 2022
total_population_sorted1 = total_population_data.sort_values(by='2022 [YR2022]', ascending=True)

# Get the bottom Fifteen countries of total population for 2022
total_bottom_Fifteen_countries = total_population_sorted1.head(15)
print("Bottom Fifteen countries of total population")
print(total_bottom_Fifteen_countries )



#Bottom Fifteen countries of total population in year 2022 and 2016

# Create the bar plot
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x='2022 [YR2022]', y="Country Name", data=total_bottom_Fifteen_countries)
plt.title("Bottom Fifteen Countries of Total Population (2022)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2016 [YR2016]', y="Country Name", data=total_bottom_Fifteen_countries)
plt.title("Bottom Fifteen Countries with Total Population (2016)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()



#Bottom Fifteen countries of total population in year 2010 and 2001

# Create the bar plot
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x='2010 [YR2010]', y="Country Name", data=total_bottom_Fifteen_countries)
plt.title("Bottom Fifteen Countries of Total Population (2010)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2001 [YR2001]', y="Country Name", data=total_bottom_Fifteen_countries)
plt.title("Bottom Fifteen Countries with Total Population (2001)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()





#Extracted top Fifteen countries with highest male population


# Filter data for male population
male_population_data = data[data["Series Code"] == "SP.POP.TOTL.MA.IN"]

# Sort data based on the male population for 2022
male_population_sorted = male_population_data.sort_values(by='2022 [YR2022]', ascending=False)

# Get the top Fifteen countries with the highest male population for 2022
male_top_Fifteen_countries = male_population_sorted.head(15)
print("Top Fifteen countries of male population")
print(male_top_Fifteen_countries )



#Extracted top Fifteen countries with highest female population
# Filter data for female population
female_population_data = data[data["Series Code"] == "SP.POP.TOTL.FE.IN"]

# Sort data based on the female population for 2022
female_population_sorted = female_population_data.sort_values(by='2022 [YR2022]', ascending=False)

# Get the top Fifteen countries with the highest female population for 2022
female_top_Fifteen_countries = female_population_sorted.head(15)

print("Top Fifteen countries of female population")
print(female_top_Fifteen_countries)



#Top Fifteen countries with highest male and female population in 2022


# Create the bar plot
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x='2022 [YR2022]', y="Country Name", data=male_top_Fifteen_countries)
plt.title("Top Fifteen Countries with Highest Male Population (2022)")
plt.xlabel("Male Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2022 [YR2022]', y="Country Name", data=female_top_Fifteen_countries)
plt.title("Top Fifteen Countries with Highest Femaale Population (2022)")
plt.xlabel("Female Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()



#Top Fifteen countries with highest male and female population in 2019
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x='2019 [YR2019]', y="Country Name", data=male_top_Fifteen_countries)
plt.title("Top Fifteen Countries with Highest Male Population (2019)")
plt.xlabel("Male Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2019 [YR2019]', y="Country Name", data=female_top_Fifteen_countries)
plt.title("Top Fifteen Countries with Highest Female Population (2019)")
plt.xlabel("Female Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()



#Top Fifteen countries with highest male and female population in 2001
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x='2001 [YR2001]', y="Country Name", data=male_top_Fifteen_countries)
plt.title("Top Fifteen Countries with Highest Male Population (2001)")
plt.xlabel("Male Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2001 [YR2001]', y="Country Name", data=female_top_Fifteen_countries)
plt.title("Top Fifteen Countries with Highest Female Population (2001)")
plt.xlabel("Female Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()




#Extracted top Fifteen countries with lowest male population

# Sort data based on the male population for 2022 in ascending order
male_population_sorted = male_population_data.sort_values(by="2022", ascending=True)

# Get the top Fifteen countries with the lowest male population for 2022
male_lowest_Fifteen_countries = male_population_sorted.head(10)

print("Top Fifteen countries with lowest male population")
print(male_lowest_Fifteen_countries )

#Extracted top Fifteen countries with lowest female population
# Sort data based on the female population for 2022 in ascending order
female_population_sorted = female_population_data.sort_values(by="2022", ascending=True)

# Get the top Fifteen countries with the lowest female population for 2022
female_lowest_Fifteen_countries = female_population_sorted.head(10)

print("Top Fifteen countries with lowest female population")
print(female_lowest_Fifteen_countries )




#Top Fifteen countries with lowest male and female population in 2022
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x='2022 [YR2022]', y="Country Name", data=male_lowest_Fifteen_countries, palette="viridis")
plt.title("Top Fifteen Countries with Lowest Male Population (2022)")
plt.xlabel("Male Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x='2022 [YR2022]', y="Country Name", data=female_lowest_Fifteen_countries, palette="viridis")
plt.title("Top Fifteen Countries with Lowest Female Population (2022)")
plt.xlabel("Female Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()


#Top Fifteen countries with lowest male and female population in 2012
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x="2012", y="Country Name", data=male_lowest_Fifteen_countries, palette="viridis")
plt.title("Top Fifteen Countries with Lowest Male Population (2012)")
plt.xlabel("Male Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x="2012", y="Country Name", data=female_lowest_Fifteen_countries, palette="viridis")
plt.title("Top Fifteen Countries with Lowest Female Population (2012)")
plt.xlabel("Female Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()
