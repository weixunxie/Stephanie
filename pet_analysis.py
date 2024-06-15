import pandas as pd
from datetime import datetime

# Function to load data from a CSV file
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to clean data
def clean_data(df):
    # Initial columns print for debugging
    print("Initial columns:", df.columns.tolist())
    
    # Rename the columns based on their positions
    df.columns = ['Name', 'Birthdate', 'Price', 'Species', 'SpecialFeature', 'Extra']
    
    # Columns after renaming
    print("Columns after renaming:", df.columns.tolist())
    
    # Drop the last column
    df.drop(columns=['Extra'], inplace=True)
    
    # Columns after dropping 'Extra'
    print("Columns after dropping 'Extra':", df.columns.tolist())
    
    # Add a new column for PetID
    df.insert(0, 'PetID', range(1, 1 + len(df)))
    
    # Columns after adding 'PetID'
    print("Columns after adding 'PetID':", df.columns.tolist())
    
    # Check if PetID exists
    if 'PetID' in df.columns:
        print("PetID column successfully added.")
    else:
        print("Failed to add PetID column.")
    
    return df

# Function to calculate the average price of pets in a specific species
def calculate_average_price(df, species):
    species_df = df[df['Species'] == species]
    return species_df['Price'].mean()

# Function to find pets with a specific special feature
def find_pets_with_feature(df, feature):
    feature_df = df[df['SpecialFeature'] == feature]
    return feature_df['Name'].tolist()

# Function to calculate the age from birthdate
def calculate_age(birthdate):
    try:
        birthdate = pd.to_datetime(birthdate, errors='coerce')
        if pd.isnull(birthdate):
            return None
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    except Exception as e:
        print(f"Error calculating age for birthdate '{birthdate}': {e}")
        return None

# Function to calculate species statistics
def get_species_statistics(df):
    statistics = {}
    for species in df['Species'].unique():
        species_df = df[df['Species'] == species]
        average_price = species_df['Price'].mean()

        # Calculate average age
        species_df['Age'] = species_df['Birthdate'].apply(calculate_age)
        average_age = species_df['Age'].mean()

        statistics[species] = {'Average Price': average_price, 'Average Age': average_age}

    return statistics
