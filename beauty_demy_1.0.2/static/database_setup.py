#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



Base = declarative_base()

# basic user login system not completed more secuirty will be added
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    paid = Column(Integer(1), default=0)
    role = Column(Integer(2))



# contains all home page editable content will hold various type of data
# for example, contents, images, pages background-color, some data for anlasysis
# every thing we need stor in the home page to database
class Home(Base):
    __tablename__ = 'home'

    id = Column(Integer, primary_key=True)
    meta_name = Column(String(250))
    meta_key = Column(String(250))
    meta_value = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'meta_name': self.key_name,
            'meta_key': self.key_value,
            'meta_value': self.meta_value

        }



# contains Courses Menu List for all courses in the website
class CoursesMenu(Base):
    __tablename__ = 'courses_menu'

    id = Column(Integer, primary_key=True)
    # the link open the lessons menu for that course
    url_to_course_menu = Column(String(400))
    title = Column(String(250), nullable=False)
    #who in  the  course videos
    course_by =  Column(String(250), nullable=False)
    course_img = Column(String(500), nullable=False)
    course_img_intro = Column(String(500))
    tags =  Column(String(1000))
    paid = Column(Integer(1), default=1)
    publish_date = Column(String(250))
    # user who added this course to the website
    added_by = Column(String(250))
    short_summary = Column(String(250))
    full_description = Column(String(10000))
    course_intro_page = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'url_to_course_menu': self.id,
            'title': self.title,
            'course_by': self.course_by,
            'course_img': self.course_img,
            'course_img_intro': self.course_img_intro,
            'tags': self.tags,
            'paid': self.paid,
            'publish_date': self.publish_date,
            'added_by': self.added_by,
            'short_summary': self.short_summary,
            'full_description': self.full_description,
            'course_intro_page': self.course_intro_page
        }

# contains Lessons Menu for Each course in the Courses Menu Table
class LessonsMenu(Base):
    __tablename__ = 'lessons_menu'

    id = Column(Integer, primary_key=True)
    img = Column(String(250), nullable=False)
    title = Column(String(250), nullable=False)
    short_summary = Column(String(250))
    full_description = Column(String(10000))
    tags = Column(String(250))
    url_to_lesson_page = Column(String(250))
    menu_id = Column(Integer, ForeignKey('courses_menu.id'))
    menu = relationship(CoursesMenu)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'img': self.img,
            'title': self.title,
            'short_summary': self.short_summary,
            'full_description': self.full_description,
            'tags': self.tags,
            'url_to_lesson_page': self.url_to_lesson_page,
            'menu_id': self.menu_id,
        }

# Single lesson Item (this is the Lesson it self, videos, lesson content)
class Lesson(Base):
    __tablename__ = 'lesson'

    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    short_summary = Column(String(250))
    full_description = Column(String(250))
    tags = Column(String(250))
    menu_id = Column(Integer, ForeignKey('lessons_menu.id'))
    menu = relationship(LessonsMenu)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'title': self.title,
            'short_summary': self.short_summary,
            'full_description': self.full_description,
            'tags': self.tags,
        }



    class LessonsMeta(Base):
    __tablename__ = 'lessons_meta'

    id = Column(Integer, primary_key=True)
    meta_name = Column(String(250))
    meta_key = Column(String(250))
    meta_value = Column(String(250))
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    lesson = relationship(Lesson)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'meta_name': self.title,
            'meta_key': self.short_summary,
            'meta_value': self.full_description,
            'lesson_id': self.tags,
        }


    class UsersMessages(Base):
    __tablename__ = 'users_message'

    id = Column(Integer, primary_key=True)
    message_title = Column(String(250))
    message_content = Column(String(10000))
    message_file = Column(String(250))
    message_date = Column(String(250))
    sender_id = Column(Integer, ForeignKey('user.id'))
    sender = relationship(User)
    receiver_id = Column(Integer, ForeignKey('user.id'))
    receiver = relationship(User)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'reciver_id': self.reciver_id,
            'message_title': self.message_title,
            'message_content': self.message_content,
            'message_files': self.message_files,
            'message_date': self.message_date
        }

    class OuterMessages(Base):
    __tablename__ = 'outer_message'

    id = Column(Integer, primary_key=True)
    sender_mail = Column(String(250))
    sender_name = Column(String(250))
    message_title = Column(String(250))
    message_content = Column(String(10000))
    message_files = Column(String(250))
    message_date = Column(String(250))
    receiver_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'sender_mail': self.sender_mail,
            'sender_name': self.sender_name,
            'message_title': self.message_title,
            'message_content': self.message_content,
            'message_files': self.message_files,
            'message_date': self.message_date
        }


# contains News Data scraped / API Not completed yet
class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    scraped_title = Column(String(250))
    scraped_image = Column(String(700))
    scraped_url = Column(String(250))
    scraped_content = Column(String(700))
    scraped_date = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.menu_type,
            'scraped_title': self.id,
            'scraped_image': self.menu_type,
            'scraped_url': self.id,
            'scraped_content': self.menu_type,
            'scraped_date': self.id,
        }



engine = create_engine('sqlite:///makup.db')
Base.metadata.create_all(engine)
