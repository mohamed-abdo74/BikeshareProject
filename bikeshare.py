from tokenize import group
import numpy as np
import pandas as pd
from datetime import datetime, date
import time

# CITY_FILES dictionary refers to path of citites
CITY_FILES = {
    'chicago' : 'chicago.csv',
    'new york' : 'new_york_city.csv',
    'washington' : 'washington.csv'
}

cities = ['chicago','new york','washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']

def print_spaces():
    print("\n")
    print("-"*100)

def check_inputs(input_str, input_type):
    while True:
        input_read = input(input_str).lower()
        try:
            if input_read in cities and input_type == 1:
                break
            elif input_read in months and input_type == 2:
                break
            elif input_read in days and input_type == 3:
                break
            else:
                if input_type == 1:
                    print("Invalid City! You must choose Chicago, New York or Washington")
                if input_type == 2:
                    print("Invalid Month! You must choose from January to June")
                if input_type == 3:
                    print("Invalid Day!")
        except ValueError:
            print('Sorry! Invalid Input')
    return input_read


def get_filters():
    print('\nHello! Let\'s explore some Us bikeshare data!\n')
    # Input for CITY (Chicago, New York, Washington)
    city = check_inputs('Please enter the city (Chicago, New York, Washington)...',1)
    # Input for Month (All, January, February, March, April, May, June)
    month = check_inputs('Please enter any month from January to June or enter \"All\" that refers to all first six months ...',2) 
    # Input for Day (All, Saturday, Sunday, Monday, Tuesday, Wedensday, Thursday, Friday)
    day = check_inputs('Please enter any day or \"All\" that refers to all days in week ...',3)
    
    print_spaces()

    return city, month, day


def load_data(city, month, day):
    # Read csv file
    df = pd.read_csv(CITY_FILES[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    # Filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_states(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = datetime.now().time()
    t1 = datetime.combine(date.min, start_time)
    print("Start time is : {}".format(start_time))

    # Display the most common month
    month_num = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}
    most_month = df['month'].value_counts().idxmax()
    print("\nThe most common month is {} ({}).".format(most_month,month_num[most_month]))

    # Display the most common day of week
    most_day = df['day_of_week'].mode()[0]
    print("\nThe most common day is {}.".format(most_day))

    # Display the most common start hour
    most_hour = df['hour'].mode()[0]
    print("\nThe most common hour is {}.".format(most_hour))

    end_time = datetime.now().time()
    t2 = datetime.combine(date.min, end_time)
    print("\nEnd time is : {}".format(end_time))

    print("\nThe time taken for these operations is : {}. i.e. {} Seconds".format(t2 - t1,(t2-t1).seconds))
   
    print_spaces()


def station_states(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = datetime.now().time()
    t1 = datetime.combine(date.min, start_time)
    print("Start time is : {}".format(start_time))

    # Display most commonly used start station 
    most_start_station = df['Start Station'].value_counts().idxmax()
    print("\nThe most common used start station is : {}".format(most_start_station))

    # Display most commonly used end station
    most_end_station = df['End Station'].value_counts().idxmax()
    print("\nThe most common used end station is : {}".format(most_end_station))

    # Display most frequent combination of start station and end station trip
    group_field = df.groupby(['Start Station','End Station'])
    print("\nThe most frequent combination of start station and end station tip is :\n")
    print(group_field.size().sort_values(ascending=False).head(1))

    end_time = datetime.now().time()
    t2 = datetime.combine(date.min, end_time)
    print("\nEnd time is : {}".format(end_time))
    
    print("\nThe time taken for these operations is : {}. i.e. {} Seconds".format(t2 - t1,(t2-t1).seconds))
    
    print_spaces()


def trip_duration_states(df):
    print('\nCalculating Trip Duration...\n')

    start_time = datetime.now().time()
    t1 = datetime.combine(date.min, start_time)
    print("Start time is : {}".format(start_time))

    # Display Total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nTotal Trip Duration = {}".format(total_travel_time))

    # Display Mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nMean Trip Duration = {}".format(mean_travel_time))

    end_time = datetime.now().time()
    t2 = datetime.combine(date.min, end_time)
    print("\nEnd time is : {}".format(end_time))
    
    print("\nThe time taken for these operations is : {}. i.e. {} Seconds".format(t2 - t1,(t2-t1).seconds))
    
    print_spaces()
    

def user_states(df,city):
    print('\nCalculating User Stats...\n')

    start_time = datetime.now().time()
    t1 = datetime.combine(date.min, start_time)
    print("Start time is : {}".format(start_time))

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print("\nUser types are : \n{}".format(counts_of_user_types))

    # Display count of gender
    if city != 'washington':
        counts_of_gender = df['Gender'].value_counts()
        print("\nGender is : \n{}".format(counts_of_gender))
        most_birth_year = df['Birth Year'].value_counts().idxmax()
        print("\nMost Birth Year is : {}".format(most_birth_year))
        earliest_birth_year = df['Birth Year'].min()
        print("\nEarliest Birth Year is {}".format(earliest_birth_year))
        most_recent_birth_year = df['Birth Year'].max()
        print("\nMost Recent Birth Year is : {}".format(most_recent_birth_year)) 

    end_time = datetime.now().time()
    t2 = datetime.combine(date.min, end_time)
    print("\nEnd time is : {}".format(end_time))
    
    print("\nThe time taken for these operations is : {}. i.e. {} Seconds".format(t2 - t1,(t2-t1).seconds))
    
    print_spaces()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df)
        print_spaces()
        time_states(df)
        station_states(df)
        trip_duration_states(df)
        user_states(df,city)
        restart_program = input("Do you need to continue? yes or no ...")
        if restart_program != 'yes':
            break
    

if __name__ == "__main__":
    main()