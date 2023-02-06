
#To reduce repetitive code, an "overview" function to investigate DataFrames.
import pandas as pd

def overview(df):

    # General Information.
    print("****General Information:****")
    display(df.info())

    # Basic description.
    print("****Basic statistical description:****")
    display(df.describe())
    
    # Shape.
    print("****Shape:****")
    display(df.shape)
    
    # Unique Values for each column.
    print("****Uniques per column:****")
    display(df.nunique())

    # How many duplicates.
    print("****Sum of duplicates:****")
    display(df.duplicated().sum())

    # And how many missing values.
    print("****Sum of missing data per column:****")
    display(df.isnull().sum()) #check here again!
    
    # Heas of the DataFrame.
    print("****Head:****")
    display(df.head(3))
    
    # A few samples of the DataFrame.
    print("****Sampling:****")
    display(df.sample(10))
    
    
#To reduce repetitive code, an "feature_analyzer" function to investigate columns in DataFrames.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew

def feature_analyzer(data_df, test_df, feature_name, target_variable):
    sns.jointplot(data=data_df, y=target_variable, x=feature_name)
    plt.show()
    
    # Description of feature in data_df.
    print("\n****Data DF Info****")
    print("Description of {} in data_df:".format(feature_name))
    print(data_df[feature_name].describe())
    
    # Value counts of feature in data_df.
    print("\n****Data DF Value Counts****")
    print("Value counts of {} in data_df:".format(feature_name))
    print(data_df[feature_name].value_counts())
    
    # Mean target_variable value by feature in data_df.
    print("\n****Data DF Mean {} by {}****".format(target_variable, feature_name))
    print("Mean {} by {} in data_df:".format(target_variable, feature_name))
    print(data_df.groupby(feature_name)[target_variable].mean())
    
    # Skewness of feature in data_df.
    if data_df[feature_name].dtype!="O":
        print("\nSkewness:",str(skew(data_df[feature_name])))
    
    # Description of feature in test_df.
    print("\n****Test DF Info****")
    print("Description of {} in test_df:".format(feature_name))
    print(test_df[feature_name].describe())
    
    # Value counts of feature in test_df.
    print("\n****Test DF Value Counts****")
    print("Value counts of {} in test_df:".format(feature_name))
    print(test_df[feature_name].value_counts())
    
    # Difference in feature values between data_df and test_df.
    print("\n****Difference in {} values between data_df and test_df****".format(feature_name))
    print("Values in data_df not in test_df:",list(set(data_df[feature_name]
                                                       .value_counts()
                                                       .index.values)
                                                   - set(test_df[feature_name]
                                                         .value_counts()
                                                         .index.values)))
    print("Values in test_df not in data_df:", list(set(test_df[feature_name]
                                                        .value_counts()
                                                        .index.values) 
                                                    - set(data_df[feature_name]
                                                          .value_counts()
                                                          .index.values)))

    
#To reduce repetitive usage of the "feature_analyzer", an iterator to use on all columns.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew

#Loop through all columns except from our targeted one
def feature_analyzer_iterator(df, target_variable):
    for feature_name in df.columns:
        if feature_name != target_variable:
            sns.jointplot(data=df, y=target_variable, x=feature_name)
            plt.show()

            # Description of feature in df.
            print("\n****Data DF Info****")
            print("Description of {} in df:".format(feature_name))
            print(df[feature_name].describe())

            # Value counts of feature in df.
            print("\n****Data DF Value Counts****")
            print("Value counts of {} in df:".format(feature_name))
            print(df[feature_name].value_counts())

            # Mean target_variable value by feature in df.
            print("\n****Data DF Mean {} by {}****".format(target_variable, feature_name))
            print("Mean {} by {} in df:".format(target_variable, feature_name))
            print(df.groupby(feature_name)[target_variable].mean())

            # Skewness of feature in df.
            if df[feature_name].dtype!="O":
                print("\nSkewness:",str(skew(df[feature_name])))
                
 
