from sqlalchemy import Column, Integer, Unicode, String, ForeignKey, Identity

from providers.databases.postgres import Base


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    author = Column(Integer, ForeignKey('users.id'))
    title = Column(Unicode(256), nullable=False)
    location = Column(Unicode(64), nullable=False)
    job_description = Column(Unicode(5000), nullable=False)
    salary_min = Column(Integer, nullable=False)
    salary_max = Column(Integer, nullable=True)
    salary_currency_code = Column(String(3), nullable=False)
    interview_rounds = Column(Integer, nullable=False)
    interview_description = Column(String(1000), nullable=True)
    benefits = Column(String(256), nullable=True)
