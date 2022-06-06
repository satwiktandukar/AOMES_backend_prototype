from typing import List
from sqlalchemy import Column, Integer, String
from blog.database import Base


class MBBS(Base):

    __tablename__ = "MBBS"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)



class Nursing(Base):
    
    __tablename__ = "Nursing"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class BMLT(Base):
    
    __tablename__ = "BMLT"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class Agriculture(Base):
    
    __tablename__ = "Agriculture"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)



class Login(Base):
    
    __tablename__ = "creds"
    id = Column(Integer,primary_key=True,index=True)
    phone = Column(String)
    password = Column(String)


class Admin(Base):
    
    __tablename__ = "Admin"
    id = Column(Integer,primary_key=True,index=True)
    phone = Column(String)


class MBBS_Zoology(Base): 
    __tablename__ = "MBBS_Zoology"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class MBBS_Botany(Base): 
    __tablename__ = "MBBS_Botany"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class MBBS_Chemistry(Base): 
    __tablename__ = "MBBS_Chemistry"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class MBBS_MAT(Base): 
    __tablename__ = "MBBS_MAT"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class BMLT_Zoology(Base): 
    __tablename__ = "BMLT_Zoology"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class BMLT_Botany(Base): 
    __tablename__ = "BMLT_Botany"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class BMLT_Chemistry(Base): 
    __tablename__ = "BMLT_Chemistry"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class BMLT_MAT(Base): 
    __tablename__ = "BMLT_MAT"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)


class Agriculture_English(Base): 
    __tablename__ = "Agriculture_English"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)


class Agriculture_Physics(Base): 
    __tablename__ = "Agriculture_Physics"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class Agriculture_Chemistry(Base): 
    __tablename__ = "Agriculture_Chemistry"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class Agriculture_Maths(Base): 
    __tablename__ = "Agriculture_Maths"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class Agriculture_Botany(Base): 
    __tablename__ = "Agriculture_Botany"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class Agriculture_Zoology(Base): 
    __tablename__ = "Agriculture_Zoology"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class Agriculture_GK(Base): 
    __tablename__ = "Agriculture_GK"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)

class Agriculture_Relevant_Science(Base): 
    __tablename__ = "Agriculture_Relevant_Science"

    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)




class Nursing_License_Integrated_Science(Base): 
    __tablename__ = "Nursing_License_Integrated_Science"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)


class Nursing_License_Community_Health_Nursing(Base): 
    __tablename__ = "Nursing_License_Community_Health_Nursing"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)


class Nursing_License_Fundamental_of_Nursing(Base): 
    __tablename__ = "Nursing_License_Fundamental_of_Nursing"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)


class Nursing_License_Adult_Nursing(Base): 
    __tablename__ = "Nursing_License_Adult_Nursing"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)



class Nursing_License_Child_Health_Nursing(Base): 
    __tablename__ = "Nursing_License_Child_Health_Nursing"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)


class Nursing_License_Midwifery_and_Gynecology(Base): 
    __tablename__ = "Nursing_License_Midwifery_and_Gynecology"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)


class Nursing_License_Leadership_and_Management(Base): 
    __tablename__ = "Nursing_License_Leadership_and_Management"
    id = Column(Integer,primary_key=True,index=True)
    question = Column(String)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct = Column(String)


