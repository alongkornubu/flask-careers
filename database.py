from sqlalchemy import create_engine, text
engine = create_engine(
    "mysql+pymysql://root:@localhost/tone_careers?charset=utf8mb4"
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        return jobs



def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM  jobs WHERE id = :val"),
           {"val":id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0]._mapping)


