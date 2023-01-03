from sqlalchemy.orm import Session

from db.models.course import Course
from pydantic_schemas.course import CourseCreate, CourseUpdate

from datetime import datetime

def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session):
    return db.query(Course).all()


def get_user_courses(db: Session, user_id:int):
    courses = db.query(Course).filter(Course.user_id == user_id).all()
    return courses


def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        title=course.title, 
        description=course.description,
        user_id=course.user_id)

    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def update_course(db: Session, course_id:int, course:CourseUpdate):
    db_course_upt = db.query(Course).filter(Course.id == course_id).first()
    db_course_upt.title = course.title
    db_course_upt.description = course.description
    db_course_upt.updated_at = datetime.utcnow()


    db.commit()
    db.close()

    return db_course_upt


def delete_course(db: Session, course_id:int):
    db_course_dlt = db.query(Course).filter(Course.id == course_id).first()
    db.delete(db_course_dlt)
    db.commit()
    db.close()

    return "Course deleted"