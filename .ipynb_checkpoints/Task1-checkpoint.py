import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_excel('/Users/dhartipatel/Documents/GitHub/PRODIGY_DS_01/Data.xlsx')

print(list(data.columns))

data = data.drop("Country Code", axis=1)
data = data.drop("Series Name", axis=1)

#Extracted top ten countries of total population


# Filter data for total population
total_population_data = data[data["Series Code"] == "SP.POP.TOTL"]

# Sort data based on the total population for 2022
total_population_sorted = total_population_data.sort_values(by= 2022, ascending=False)

# Get the top ten countries with the highest total population for 2022
total_top_ten_countries = total_population_sorted.head(10)
print("Top ten countries of total population")
print(total_top_ten_countries )

def add_value_labels(ax, spacing=10):

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



#Top ten countries of total population in year 2022 and 2016
        
# Create the bar plot
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x=2022, y="Country Name", data=total_top_ten_countries)
plt.title("Top Ten Countries of Total Population (2022)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x=2016, y="Country Name", data=total_top_ten_countries)
plt.title("Top Ten Countries with Total Population (2016)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()



#Top ten countries of total population in year 2010 and 2001

# Create the bar plot
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x=2010, y="Country Name", data=total_top_ten_countries)
plt.title("Top Ten Countries of Total Population (2010)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x=2001, y="Country Name", data=total_top_ten_countries)
plt.title("Top Ten Countries with Total Population (2001)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()




#Extracted bottom ten countries of total population

# Sort data based on the total population for 2022
total_population_sorted1 = total_population_data.sort_values(by=2022, ascending=True)

# Get the bottom ten countries of total population for 2022
total_bottom_ten_countries = total_population_sorted1.head(10)
print("Bottom ten countries of total population")
print(total_bottom_ten_countries )



#Bottom ten countries of total population in year 2022 and 2016

# Create the bar plot
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x=2022, y="Country Name", data=total_bottom_ten_countries)
plt.title("Bottom Ten Countries of Total Population (2022)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x=2016, y="Country Name", data=total_bottom_ten_countries)
plt.title("Bottom Ten Countries with Total Population (2016)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()



#Bottom ten countries of total population in year 2010 and 2001

# Create the bar plot
plt.figure(figsize=(20, 16))
plt.rcParams['axes.facecolor'] = 'black'

plt.subplot(2,2,1)
plot=sns.barplot(x=2010, y="Country Name", data=total_bottom_ten_countries)
plt.title("Bottom Ten Countries of Total Population (2010)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.subplot(2,2,2)
plot=sns.barplot(x=2001, y="Country Name", data=total_bottom_ten_countries)
plt.title("Bottom Ten Countries with Total Population (2001)")
plt.xlabel("Total Population")
plt.ylabel("Country")
add_value_labels(plot)

plt.tight_layout()


