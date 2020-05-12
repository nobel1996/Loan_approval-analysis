# --------------
## Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 



# code starts here
#Load Dataset

bank = pd.read_csv(path)
    
# Display categorical variable


categorical_var=bank.select_dtypes(include='object')


#print("Categorical variables : ",categorical_var)


    
#Code for numerical variable

numerical_var=bank.select_dtypes(include='number')

#print("Numerical Variables : ",numerical_var)



# code ends here


# --------------
# code starts here
bank.drop("Loan_ID",axis=1,inplace=True)
banks= bank
#print(banks)
null = banks.isnull().sum()
print(null)
bank_mode = banks.mode()
banks.fillna('bank_mode',inplace=True)
print(banks)
#code ends here


# --------------
# code starts here
#Task 1 - Load the data
## Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 



# code starts here
#Load Dataset

bank = pd.read_csv(path)
    
# Display categorical variable


categorical_var=bank.select_dtypes(include='object')


#print("Categorical variables : ",categorical_var)


    
#Code for numerical variable

numerical_var=bank.select_dtypes(include='number')

#print("Numerical Variables : ",numerical_var)



# code ends here

#Task 2 - Something is Missing!
# code starts here
bank.drop("Loan_ID",axis=1,inplace=True)
banks= bank
#print(banks)
null = banks.isnull().sum()
#print(null)
bank_mode = banks.mode().iloc[0]
#0 or ‘index’ : get mode of each column
#1 or ‘columns’ : get mode of each row
banks.fillna(bank_mode,inplace=True)
#print(banks.isnull().sum())
avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)


print (avg_loan_amount)
#code ends here
#code ends here




# --------------
# code starts here




loan_approved_se = len(banks[(banks.Self_Employed=='Yes') & (banks.Loan_Status=='Y')])
loan_approved_nse = len(banks[(banks.Self_Employed=='No') & (banks.Loan_Status=='Y')])
percentage_se = (loan_approved_se*100)/614
percentage_nse =  (loan_approved_nse*100)/614
print(percentage_se)
print(percentage_nse)
print(loan_approved_se)
print(loan_approved_nse)

# code ends here


# --------------
# code starts here



#print(banks['Loan_Amount_Term']) 
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )


big_loan_term=len(loan_term[loan_term>=25])

print(big_loan_term)

#big_loan_term = len(banks[banks.loan_term >='25'])


# code ends here


# --------------
# code starts here
banks
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)




# code ends here


