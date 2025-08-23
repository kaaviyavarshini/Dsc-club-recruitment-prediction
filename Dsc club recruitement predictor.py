import pandas as pd
#Creation of a smaple dataset containing few features of 10 candidates 
data = pd.DataFrame({
    "Programming efficiency":["High","Low","Medium","High","Low","Medium","High","Medium","Low","High"],
    "Logic implementation dsa":["Good","Poor","Average","Good","Poor","Average","Good","Good","Average","Average"],
    "Eventparticipation":["Active","None","Occasional","Active","None","Occasional","Active","Active","None", "Active"],
    "Speakingskills":["Strong","Weak","Moderate","Moderate","Weak","Moderate","Strong","Moderate","Weak","Strong"],
    "Achievements":[6,1,3,4,0,2,8,5,1,7],
    "Mindset of candidate": ["Growth","Fixed","Neutral","Growth","Fixed","Neutral","Growth","Growth","Neutral","Growth"],
    "Eligibility":["Approve","Reject","Approve","Approve","Reject","Reject","Approve","Approve","Reject","Approve"]})
#Defining a function-basically knwng if the candidate should be selected or not
def isselectedornot(pefficiency,dsalogic,participation,speaking,achievements,mindset):
    if pefficiency=="High" and logic=="Good" and mindset=="Growth":
        return "Approve"
    elif pefficiency in ["High","Medium"] and participation=="Active" and achievements>=3:
        return "Approve"
    elif dsalogic=="Average" and speaking in ["Strong","Moderate"] and mindset=="Growth":
        return "Approve"
    else:
        return "Reject"

data["Recruited"]=data.apply(lambda row: isselectedornot(
    row["Programming efficiency"],
    row["Logic implementation dsa"],
    row["Eventparticipation"],
    row["Speakingskills"],
    row["Achievements"],
    row["Mindset of candidate"]),axis=1)

C=sum(data["Eligibility"]==data["Recruited"])
print("Accuracy of model on the dataset provided: %d/%d\n"%(C,len(data)))

#Taking input from the user
PE=input("Programming efficiency of candidate(High/Medium/Low):choose one").capitalize()
DSAL=input("Logic implementation of candidate in solving DSA(Good/Average/Poor):choose one").capitalize()
EP=input("Participation of candidate in events(Active/Occasional/None):choose one").capitalize()
SS=input("Speaking skills(Strong/Moderate/Weak):choose one").capitalize()
Achive=int(input("Achievements made so far(0 to 10):choose one"))
Mindset=input("Mindset of candidate(Growth/Neutral/Fixed):choose one").capitalize()

#Calling out the before decalred function
prediction=isselectedornot(PE,DSAL,EP,SS,Achieve,Mindset)
print("\nHurray you are recruited in our club!!*%s* this guyy"%prediction)
