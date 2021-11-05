from sqlalchemy import Column, Integer, Unicode, String, ForeignKey, Enum, DateTime

from domain.jobs.entities import JobStatus
from providers.databases.postgres import Base


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
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
    posted_at = Column(DateTime(), nullable=False)
    status = Column(Enum(JobStatus), nullable=False)


class JobPayment(Base):
    __tablename__ = 'job_payments'

    id = Column(Integer, primary_key=True)
    payment_id = Column(String(256), nullable=False)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=False)
