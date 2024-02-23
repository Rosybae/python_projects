# For creativity purpose, I added the count of the total number of countries from the dataset.

minimum = 9999
minimum_country = ''
minimum_year = 0
maximum = 0
maximum_country = ''
maximum_year = 0

age_list = []
spec_min_age = 9999
spec_min_country = ''
spec_max_age = 0
spec_max_country = ''

country_count = 0
current_country = ''

selected_year = int(input('Please, enter the year of interest: ').strip())

with open('life-expectancy.csv') as le:
    for i, line in enumerate(le):
        if i == 0:
            continue
        
        line = line.strip()
        data = line.split(',')
        country = data[0]
        year = int(data[2])
        age = float(data[3])
        
        if age < minimum:
            minimum = age
            minimum_country = country
            minimum_year = year
            
        if age > maximum:
            maximum = age
            maximum_country = country
            maximum_year = year
            
        if year == selected_year:
            age_list.append(age)
            
            if age < spec_min_age:
                spec_min_age = age
                spec_min_country = country
            if age > spec_max_age:
                spec_max_age = age
                spec_max_country = country
                
        if current_country != country:
            country_count += 1
            current_country = country
spec_avg = sum(age_list) / len(age_list)

print(f'\nThe overall max life expectancy is: {maximum} from {maximum_country} in {maximum_year}') 
print(f'The overall min life expectancy is: {minimum} from {minimum_country} in {minimum_year}')     
print(f'The total number of countries on the list is: {country_count}')

print(f'\nFor the year {selected_year}:')
print(f'The average life expectancy across all countries was {spec_avg:.2f}')
print(f'The max life expectancy was in {spec_max_country} with {spec_max_age}')
print(f'The min life expectancy was in {spec_min_country} with {spec_min_age}')