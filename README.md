# DSC club recruitment prediction
To predict if the candidate will get recruited in the club or not
This project predicts if a candidate will be recruited in DSC club of SRM IST,RMP or not
It uses a sample dataset containing certain concerning features of 10 candidates comparing with the user inputed dataset
# Dataset-
The dataset includes 6 features per candidate and 1 target label-Elgibility

  ("Programming efficiency":["High","Low","Medium","High","Low","Medium","High","Medium","Low","High"],
    "Logic implementation dsa":["Good","Poor","Average","Good","Poor","Average","Good","Good","Average","Average"],
    "Eventparticipation":["Active","None","Occasional","Active","None","Occasional","Active","Active", "None", "Active"],
    "Speakingskills":["Strong","Weak","Moderate","Moderate","Weak","Moderate","Strong","Moderate","Weak","Strong"],
    "Achievements":[6,1,3,4,0,2,8,5,1,7],
    "Mindset of candidate": ["Growth","Fixed","Neutral","Growth","Fixed","Neutral","Growth","Growth","Neutral","Growth"],
    "Eligibility":["Approve","Reject","Approve","Approve","Reject","Reject","Approve","Approve","Reject","Approve")
# Logic behind-
Importing pandas library 
Using simple if-else conditions to know if the candidate is really eligible for the post or not

if pefficiency=="High" and logic=="Good" and mindset=="Growth":
        return "Approve"
    elif pefficiency in ["High","Medium"] and participation=="Active" and achievements>=3:
        return "Approve"
    elif dsalogic=="Average" and speaking in ["Strong", "Moderate"] and mindset=="Growth":
        return "Approve"
    else:
        return "Reject"
