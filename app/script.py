import pandas as pd
from sqlalchemy import create_engine
import logging
import os

db_user = os.getenv("POSTGRES_USER")
db_pass = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")
db_port = str(os.getenv("POSTGRES_PORT"))
db_host = os.getenv("POSTGRES_HOST")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def preprocess(df, paper_df, category_df, author_df):
    category_df = df[['category_code','category']].drop_duplicates()
    category_df = category_df.rename(columns={'category_code': 'category_id'})

    df['authors'] = df['authors'].apply(lambda x: x if isinstance(x,str) else str(x))
    author_df = df['authors'].explode().drop_duplicates().reset_index(drop=True).to_frame(name="author_name")
    # df['authors'] = df['authors'].apply(lambda x:str(len(', '.join(x))))     
    
    # author_df = author_df.rename(columns={'authors': 'author_name'})

    paper_df = df[['id','title','category_code','authors','published_date','updated_date','summary','summary_word_count']]
    # paper_df['auth_len'] = paper_df.loc[:,'authors'].apply(lambda x:str(len(x)))

    # print(category_df.head())
    # print(author_df.head())
    # print(max(paper_df.loc[:,'authors'].apply(lambda x:len(x))))
    return paper_df, category_df, author_df

def loadData(paper_df, category_df, author_df):
    try:
        engine = create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db}")
        print(engine)
        with engine.begin() as connection:
            logging.info('Inserting Category data')
            category_df.to_sql("category", con=connection, if_exists="append", index=False)
            logging.info('Inserting Author data')
            author_df.to_sql("author", con=connection, if_exists="append", index=False)
            logging.info('Inserting Papers data')
            paper_df.to_sql("papers", con=connection, if_exists="append", index=False)
            print('Success!!')
    except Exception as e:
        logging.info(e)
        print(e)


df = pd.read_csv('data/arXiv_scientific_dataset.csv')
paper_df = pd.DataFrame()
category_df = pd.DataFrame()
author_df = pd.DataFrame()
paper_df, category_df, author_df = preprocess(df, paper_df, category_df, author_df)
loadData(paper_df, category_df, author_df)




