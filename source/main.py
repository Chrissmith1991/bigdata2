import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 




def main():
    df = pd.read_csv('../data/data_assignment.csv')
    question_1(df)


def question_1(frame):
    #Which city has more job? How many jobs each type (casual, fulltime, etc.) are there in each city?
    
    #Which city has more job?
    city_most_jobs = frame['Location'].value_counts()
    #print(city_most_jobs)
    
    #How many jobs each type (casual, fulltime, etc.) are there in each city?
    city_by_job_type = frame.groupby(['Location','JobType']).size()
    #print(city_by_job_type)
    
    
    
    #In each city, which are top 5 job sectors? How many jobs are there in each sector?
    locations = frame['Location'].unique()
    
    for location in locations:
        location_frame = frame[(frame['Location'] == location)]
        top_5 = location_frame['Classification'].value_counts().nlargest(5)
        #print(location)
        #print(top_5)
        
        
    #Visualise the top 5 job sectors in pie chart for each city.
    for location in locations:
        top_5_classification = frame[(frame['Location'] == location)]['Classification'].value_counts().nlargest(5)
    
        labels = top_5_classification.index.tolist()
        
        fig = plt.figure()
        ax = fig.add_axes([1,1,1,1])
        ax.axis('equal')
        langs = labels
        ax.pie(top_5_classification, labels = langs,autopct='%1.2f%%')
        plt.title (location)
        plt.show()
        
        
    #In each city, list the job salary range with the corresponding number of jobs. Which city is more well-paid?
    #Which City is most well paid??????????????????
    city_by_salary_range = frame.groupby(['Location','LowestSalary','HighestSalary']).size()
    #print(city_by_salary_range)
    
    
    #List top 5 companies in each city? Which sectors do they belong to? 
    for location in locations:
        location_df = frame[(frame['Location'] == location)]
        top_companies = location_df['Company'].value_counts().nlargest(5).index.tolist()
        print(location)
        for index, row in location_df.iterrows():
            if row['Company'] in top_companies:
                print(row['Company'] + " | " + row['Classification'])
                top_companies.remove(row['Company'])
        print('\n')
        
        
    #Between 2 cities, which do you think it is better for employees. Explain your choice.* (1.5 point)
        
        

    


        
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



    
