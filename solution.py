#importing librarires
import pandas as pd    
import numpy as np

#importing the datsets
x=pd.read_csv("User Gameplay data.csv") 
# print(x.head())           
y=pd.read_csv("Deposit Data.csv")
z=pd.read_csv("Withdrawal Data.csv")

# PART A
sum_of_deposits_per_user=pd.DataFrame(y.groupby('User Id')['Amount'].sum())   #Calculating total deposit amt per user
a=pd.DataFrame()
a['points_for_deposits']=pd.DataFrame(0.01*sum_of_deposits_per_user)          #Calculating points for deposits
sum_of_withdrawal_per_user=pd.DataFrame(z.groupby('User Id')['Amount'].sum()) #Calculating total withdraw amt per user
a['points_for_withdraws']=pd.DataFrame(0.005*sum_of_withdrawal_per_user)      #calculating points for withdraws
Num_of_GamesPlayed=pd.DataFrame(x.groupby('User Id')['GamesPlayed'].count())
a['Num_of_GamesPlayed'] = Num_of_GamesPlayed  #games played by each user
a['points_for_games_played']=pd.DataFrame(0.2*Num_of_GamesPlayed)

num_of_withdraws=pd.DataFrame(z.groupby('User Id')['User Id'].count())        #number of withdraws per user
num_of_deposits=pd.DataFrame(y.groupby('User Id')['User Id'].count())         #number of deposits per user
diff_bet_deposits_withdraw=pd.DataFrame((num_of_deposits)-(num_of_withdraws)) #difference
def transform_value(x):                                                       #removing null values
    if x > 0:
        return x
    else:
        return 0
    
diff_bet_deposits_withdraw = diff_bet_deposits_withdraw.applymap(transform_value)
a['points_for_difference']=pd.DataFrame(0.001*diff_bet_deposits_withdraw)     #calculating points for difference

a['points_for_deposits'].fillna(0,inplace=True)
a['points_for_withdraws'].fillna(0,inplace=True)
a['points_for_games_played'].fillna(0,inplace=True)
a['points_for_difference'].fillna(0,inplace=True)
a['total_loyalty_points']=a['points_for_deposits']+a['points_for_withdraws']+a['points_for_games_played']+a['points_for_difference']
#total points per user

from datetime import date,time
x['Datetime'] = pd.to_datetime(x['Datetime'], dayfirst=True, errors='coerce')
x['new_date'] = [x.date() for x in x['Datetime']]
x['new_time'] = [x.time() for x in x['Datetime']]
x['Year']=x['Datetime'].dt.year
x['month']=x['Datetime'].dt.month
x['day']=x['Datetime'].dt.day
x['hours']=x['Datetime'].dt.hour
x['minute']=x['Datetime'].dt.minute
x['second']=x['Datetime'].dt.second

#slotwise calcualtions
#for s1
s1_x=x[x['hours']<=12]
s2_x=x[x['hours']>12]
s1_x1=pd.DataFrame(s1_x.groupby('User Id')['GamesPlayed'].sum())
c=pd.merge(s1_x1,sum_of_deposits_per_user,on='User Id')
d=pd.merge(c,sum_of_withdrawal_per_user,on='User Id')
d['Loyalty_points']=(0.01*d['Amount_x'])+(0.005*d['Amount_y'])+(0.001*abs(d['Amount_x']-d['Amount_y']))+(0.2*d['GamesPlayed'])

#for s2
s2_x=x[x['hours']>12]
s2_x1=pd.DataFrame(s2_x.groupby('User Id')['GamesPlayed'].sum())
e=pd.merge(s2_x1,sum_of_deposits_per_user,on='User Id')
f=pd.merge(e,sum_of_withdrawal_per_user,on='User Id')
f['Loyalty_points']=(0.01*d['Amount_x'])+(0.005*d['Amount_y'])+(0.001*abs(d['Amount_x']-d['Amount_y']))+(0.2*d['GamesPlayed'])

# for 2nd Oct s1
# s1_x
for_oct_s1=s1_x.loc[s1_x['month']==10]
for_oct_2_s1=for_oct_s1[for_oct_s1['day']==2]
for_oct_2_s1=pd.DataFrame(for_oct_2_s1.groupby('User Id')['GamesPlayed'].sum())
g=pd.merge(for_oct_2_s1,sum_of_deposits_per_user,on='User Id')
i=pd.merge(g,sum_of_withdrawal_per_user,on='User Id')
i['Loyalty_point']=(0.01*i['Amount_x'])+(0.005*i['Amount_y'])+(0.001*abs(i['Amount_x']-i['Amount_y']))+(0.2*i['GamesPlayed'])

# for 18th Oct s1
for_oct_18_s1 = for_oct_s1[for_oct_s1['day']==18]
for_oct_18_s1=pd.DataFrame(for_oct_18_s1.groupby('User Id')['GamesPlayed'].sum())
j=pd.merge(for_oct_18_s1,sum_of_deposits_per_user,on='User Id')
k=pd.merge(j,sum_of_withdrawal_per_user,on='User Id')
k['Loyalty_point']=(0.01*k['Amount_x'])+(0.005*k['Amount_y'])+(0.001*abs(k['Amount_x']-k['Amount_y']))+(0.2*k['GamesPlayed'])
k.head()

# for 16th oct s2
for_oct_s2= s2_x.loc[s2_x['month']==10]
for_oct_16_s2 = for_oct_s2[for_oct_s2['day']==16]
for_oct_16_s2=pd.DataFrame(for_oct_16_s2.groupby('User Id')['GamesPlayed'].sum())
l=pd.merge(for_oct_16_s2,sum_of_deposits_per_user,on='User Id')
m=pd.merge(l,sum_of_withdrawal_per_user,on='User Id')
m['Loyalty_point']=(0.01*m['Amount_x'])+(0.005*m['Amount_y'])+(0.001*abs(m['Amount_x']-m['Amount_y']))+(0.2*m['GamesPlayed'])
m.head()

# for 26th oct s2
for_oct_s2= s2_x.loc[s2_x['month']==10]
for_oct_26_s2 = for_oct_s2[for_oct_s2['day']==26]
for_oct_26_s2=pd.DataFrame(for_oct_26_s2.groupby('User Id')['GamesPlayed'].sum())
n=pd.merge(for_oct_26_s2,sum_of_deposits_per_user,on='User Id')
o=pd.merge(n,sum_of_withdrawal_per_user,on='User Id')
o['Loyalty_point']=(0.01*o['Amount_x'])+(0.005*o['Amount_y'])+(0.001*abs(o['Amount_x']-o['Amount_y']))+(0.2*o['GamesPlayed'])
o.head()

# overall loyalty points earned and player ranks
a['Rank'] = a['total_loyalty_points'].rank(ascending = 0)
sorted_df = a.sort_values(by=['total_loyalty_points','Num_of_GamesPlayed'], ascending=[False,False])
sorted_df[['Rank','total_loyalty_points']]

# calculate avg deposit amt 
Avg_amount=y['Amount'].mean()
Avg_amount

# calculate avg deposit amt per user 
Avg_amount_per_user=pd.DataFrame(y.groupby('User Id')['Amount'].mean())
Avg_amount_per_user

# Calculating avg games played per user
Num_of_GamesPlayed=pd.DataFrame(x.groupby('User Id')['GamesPlayed'].count()) 
Num_of_GamesPlayed

# Part B- How much should be allocated to leaderboard?
#dividing Bonus on the basis of loyalty points
div_factor=50000/sum(sorted_df['total_loyalty_points'])
sorted_df['bonus_amt']=sorted_df['total_loyalty_points']*div_factor
sorted_df[['Rank','total_loyalty_points','bonus_amt']].head()