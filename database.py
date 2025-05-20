from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://root:@localhost/tone_careers?charset=utf8mb4"
)

def load_jobs_form_db():
    with engine.connect() as conn:
        jobs = conn.execute(text("select * from jobs"))
        # print(jobs.all())
        return jobs

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     print(result.all())