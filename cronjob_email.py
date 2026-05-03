def mail_trigger(): 
    import pandas as pd
    import numpy as np
    import smtplib, ssl
    from email.message import EmailMessage
    df = pd.read_csv('data.csv', parse_dates=['Due_Date', 'Target_Date', 'Completion_Date'], infer_datetime_format=True)
    df.drop(['Entity_id'], axis=1, inplace=True)
    df['Due_Date'] =  pd.to_datetime(df['Due_Date'], format='%d%b%Y')
    df['Target_Date'] =  pd.to_datetime(df['Target_Date'], format='%d%b%Y:')
    df['Completion_Date'] =  pd.to_datetime(df['Completion_Date'], format='%d%b%Y')
    df["date_diff"] = (df['Completion_Date'] - df['Due_Date'])/np.timedelta64(1,'D')
    df["date_diff"] = df["date_diff"].apply(np.int64)
    # print(df['date_diff'])
    # print(type(df['date_diff']))
    # df.to_csv("date_diff.csv")
    subject_1 = 'Finance Activity Tracker Status - Gentle Reminder!'
    body_1 = """
    \n This is a Gentle Reminder to fill your respective details in the Finance Activity Tracker Dashboard. Less than 7 days left to complete your pending activities.
    \n Please hurry up and fill the details!. 
    """
    subject_2 = 'Finance Activity Tracker Status - Escalation level 1'
    body_2 = """
    \n This is a Urgent Reminder to fill your respective details in the Finance Activity Tracker Dashboard. Less than 2 days left to complete your pending activities.
    \n Please hurry up and fill the details!.
    \n Escalation level 1: System is forwarding your pending details to your immediate reporting manager.
    """
    subject_3 = 'Finance Activity Tracker Status - Escalation level 2'
    body_3 = """
    \n This is a Super urgent Reminder to fill your respective details in the Finance Activity Tracker Dashboard. Less than 1 day left to complete your pending activities.
    \n Please hurry up and fill the details!. 
    \n Escalation level 2: System is forwarding your pending details to the Managing Director Mr. Naveen Prabhu!.
    """
    subject_4 = 'Finance Activity Tracker Status - Escalation level 3'
    body_4 = """
    \n This is a Super urgent Reminder to fill your respective details in the Finance Activity Tracker Dashboard. You have already delayed in filling your respective pending activities.
    \n Escalation level 3: System is forwarding your delayed status to the Managing Director.
    \n Please write a proper explaination for the delay and forward the details to the Managing Director Mr. Naveen Prabhu!.
    """

    email_sender = 'contact.nityo.ai@gmail.com'
    email_password = "tmkcjbjqvlrgdwjr"
    email_receiver_1 = ["riddhisahani08@gmail.com"] # only team members
    
    em_1 = EmailMessage()
    em_1['From'] = email_sender
    em_1['To'] = email_receiver_1
    em_1['Subject'] = subject_1
    em_1.set_content(body_1)

    em_2 = EmailMessage()
    em_2['From'] = email_sender
    em_2['To'] = email_receiver_2
    em_2['Subject'] = subject_2
    em_2.set_content(body_2)
    
    em_3 = EmailMessage()
    em_3['From'] = email_sender
    em_3['To'] = email_receiver_3
    em_3['Subject'] = subject_3
    em_3.set_content(body_3)

    em_4 = EmailMessage()
    em_4['From'] = email_sender
    em_4['To'] = email_receiver_4
    em_4['Subject'] = subject_4
    em_4.set_content(body_4)
        
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        # if (df["date_diff"] > float(-2)) &  (df["date_diff"] > float(-7)):
        # if df["date_diff"] > int(0):
        np.where(df["date_diff"] > int(0), smtp.sendmail(email_sender, email_receiver_1, em_1.as_string()), None)    
        np.where(df["date_diff"] > int(-2), smtp.sendmail(email_sender, email_receiver_2, em_2.as_string()), None) 
        np.where(df["date_diff"] > int(-7), smtp.sendmail(email_sender, email_receiver_3, em_3.as_string()), None)   
        np.where(df["date_diff"] > int(-7), smtp.sendmail(email_sender, email_receiver_4, em_4.as_string()), None)  
            # smtp.sendmail(email_sender, email_receiver_1, em_1.as_string())
        # elif (df["date_diff"] > float(-1)) &  (df["date_diff"] > float(-2)):
        # elif (df["date_diff"] > float(-2)):
        #     smtp.sendmail(email_sender, email_receiver_2, em_2.as_string())
        # # elif (df["date_diff"] > float(-1)) &  (df["date_diff"] > float(0)):
        # elif (df["date_diff"] > float(-1)):
        #     smtp.sendmail(email_sender, email_receiver_3, em_3.as_string())
        # else:
        #     smtp.sendmail(email_sender, email_receiver_4, em_4.as_string())
    return "Sucess"

if __name__ == '__main__':
    mail_trigger()
 
