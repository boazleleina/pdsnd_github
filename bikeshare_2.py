import time
import pandas as pd
import numpy as np

# Define a dictionary mapping city names to their corresponding data files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# Function to get user input for city, month, and day to analyze
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose city to view data from, please choose either chicago, new york city or washington: \n ")
        city = city.lower()
        if city not in CITY_DATA.keys():
            print("Please select the correct city from the options :(")
            continue
        else:
            #We're okay with the value provided
            break

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    while True:
        month = input('Enter month to filter by between January and June or all to filter by none: \n')
        month = month.lower()
        if month in months:
            break
        else:
            print("Invalid input. Please select from the provided options: ", months)

        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:    
        day = input('Enter day to filter by or all to filter by none: \n')
        day = day.lower()
        if day in days:
            break
        else:
            print("Invalid input. Please select from the provided options:", days)

    print('-'*40)
    return city, month, day


<<<<<<< HEAD
def load_data(city):
||||||| 5418b75
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
=======
# Function to load data for a specified city and filter by month and day if applicable
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
>>>>>>> documentation
    df = pd.read_csv(CITY_DATA[city])
    return df


def filter_data(df, month, day):
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


# Function to display statistics on the most frequent times of travel
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    
    print("The most common month is: ", df['month'].mode().iloc[0])

    # display the most common day of week
    
    print("The most common day of week is: ", df['day_of_week'].mode().iloc[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour is: ", df['hour'].mode().iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Function to display statistics on the most popular stations and trips
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most Common Start Station: ', df['Start Station'].mode().iloc[0])

    # display most commonly used end station
    print('Most Common End Station: ', df['End Station'].mode().iloc[0])

    # display most frequent combination of start station and end station trip
    print('Most Common Trip (Start to End): ', df.groupby(['Start Station', 'End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Function to display statistics on total and average trip duration
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Trips: ', len(df))

    # display mean travel time
    print('Average Trip Duration (minutes): ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Function to display statistics on bikeshare users
def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if 'User Type' in df.columns:
        user_type_counts = df['User Type'].value_counts().reset_index()
        user_type_counts.columns = ['User Type', 'Count']
        print("User Type Counts:\n")
        print(user_type_counts.to_string(index=False))

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts().reset_index()
        gender_counts.columns = ['Gender', 'Count']
        print("\nGender Counts:\n")
        print(gender_counts.to_string(index=False))

    if 'Birth Year' in df.columns:
        common_birth_year = df['Birth Year'].mode().iloc[0]
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        print("\nMost Common Birth Year: ", common_birth_year)
        print("Earliest Birth Year: ", earliest_birth_year)
        print("Most Recent Birth Year: ", recent_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


<<<<<<< HEAD

||||||| 5418b75
=======
# Main function to orchestrate the analysis and interaction with the user
>>>>>>> documentation
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    # Initialize a variable to keep track of the row index
    row_index = 0

    # Define the number of rows to display at each iteration
    rows_per_iteration = 5

    # Start a loop to prompt the user and display data
    while True:
        user_input = input("Do you want to see 5 lines of raw data? (yes/no): ").strip().lower()

        if user_input == 'yes':
            # Display the next 5 lines of raw data
            print(df.iloc[row_index:row_index + rows_per_iteration])
            row_index += rows_per_iteration
        elif user_input == 'no':
            break  # Exit the loop if the user says 'no'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
	main()
