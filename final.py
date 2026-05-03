from enum import unique


def mail_trigger():
    import csv 
    import pandas as pd
    import numpy as np
    import smtplib, ssl
    from email.message import EmailMessage
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from sqlalchemy import create_engine

    conn_aws = create_engine('mysql+pymysql://sandeep:SandeepsinghNityo@devdbrds.cfgu9s5ykxy0.ap-southeast-1.rds.amazonaws.com/devai')   
    query = "SELECT * FROM devai.reminder_email;"
    df = pd.read_sql(query,conn_aws)   

    subject_1 = 'Finance Activity Tracker Status - Gentle Reminder!'   
    html_1 = """\
    <html>
      <head></head>
      <body>
      This is a Gentle Reminder to fill your respective details in the Finance Activity Tracker Dashboard. Less than 7 days left to complete your pending activities.
      
      <br>
      
      
      Please use below link to view your pending Activites in Finance Activity Tracker Dashboard.
      
      https://devfinancedashboard.nityo.in/admin/login/?next=/admin/
      
      
     {0}
    
      </body>
    </html>
""".format(df[df["status"] == "Pending"].to_html(index=False))


    email_sender = 'contact.nityo.ai@gmail.com'
    email_password = "tmkcjbjqvlrgdwjr"
    em_1 = MIMEMultipart("alternative")
    em_1['From'] = email_sender
    em_1['Subject'] = subject_1
    text_with_df = MIMEText(html_1, 'html')
    em_1.attach(text_with_df)
    
    pending_df = df[df["status"] == "Pending"].drop_duplicates()
    unique_mail = pending_df["user_mail"].drop_duplicates()
    print(unique_mail)
    # ontime_df = df[df["status"] == "On-Time"].drop_duplicates()
    # delayed_df = df["user_mail"][df["status"] == "Delayed"].drop_duplicates()
    # print(pending_df)          
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        # smtp.sendmail(email_sender, email_receiver_1, em_1.as_string())
        np.where(pending_df, smtp.sendmail(email_sender, pending_df["user_mail"],em_1.as_string()), None)
        # lst_unique = list(set(lst))
        # print(res)

        # print(type(pending_df["user_mail"]))
        # np.where(ontime_df, smtp.sendmail(email_sender, ontime_df["user_mail"],em_1.as_string()), None)
        # np.where(delayed_df, smtp.sendmail(email_sender, delayed_df["user_mail"],em_1.as_string()), None)
        # if mail_reminder['status'].isin(['Pending']):
        # for i,j in pd.Series(mail_reminder["user_mail"].unique()).iteritems():
        #   np.where(mail_reminder['status'].isin(['On-Time']), smtp.sendmail(email_sender,j, em_1.as_string()), None)

if __name__ == '__main__':
    mail_trigger()
    