def calculate_rainfall():
    #get input from user
    num_of_years = int(input("Enter the number of years:"))
    # initialize variables
    total_rainfall = 0
    avg_monthly_rainfall = 0

    # loop through each year
    for year in range (1, num_of_years+1):
        print(f"Year {year}:")
        yearly_rainfall = 0
         # get monthly rainfall data
        for month in range (1,13):
            rainfall_cm = float(input(f"Enter the rainfall amount for month {month}:"))
            yearly_rainfall += rainfall_cm

        print(f"Total rainfall for year {year}: {yearly_rainfall} cm")
        total_rainfall += yearly_rainfall
        avg_monthly_rainfall += year/ 12
    
    #print the total rainfall
    print(f"Total rainfall : {total_rainfall} cm")
    # calculate and print the average monthly rainfall
    avg_monthly_rainfall /= num_of_years
    print(f"The average monthly rainfall :{avg_monthly_rainfall:} cm")
#calling the fuction
calculate_rainfall()

