import pandas as pd
import texthero as hero
from sqlalchemy import create_engine
pd.set_option('display.max_columns', None)
import json


def write_df():
    # df = pd.read_csv("cv_data.csv", encoding='cp1252')

    conn_aws = create_engine('mysql+pymysql://sandeep:SandeepsinghNityo@devdbrds.cfgu9s5ykxy0.ap-southeast-1.rds.amazonaws.com/devai')
    query = "SELECT * FROM devai.nr_resume_text_livebkp limit 5;"
    df = pd.read_sql(query,conn_aws)
    df = df[["resume_id", "resume_text"]]
    ## text Cleaning --> 
    df['resume_text_clean'] = hero.clean(df["resume_text"])

    ## TFIDF representation (Word Embedding)
    df['wv_tfidf'] = hero.tfidf(df['resume_text_clean'])

    ## Writing data to Mysql database -->
    # conn_local_db = create_engine('mysql+pymysql://root:password@localhost/cron_job?charset=utf8mb4&binary_prefix=true')


    # df['wv_tfidf'] = json.dumps(df['wv_tfidf'], default=vars)
    df['wv_tfidf'] = df['wv_tfidf'].to_json(orient='records')
    # print(df.info())
    # print(df.head())
    df.to_sql(name = 'nr_resume_text_wv', con = conn_aws,  if_exists = 'replace', index = False)
    return df.head()

if __name__ == '__main__':
    write_df()