# Educational Coaching Backend

This is a prototype backend for an educational coaching institution(AOMES)'s entrance preparation system, built using FastAPI in Python.

## Description

This backend prototype serves as the foundation for an educational coaching platform focused on entrance exam preparations. It provides APIs to manage quizzes, assessments, online courses and more.

## Features

- Create, read, update, and delete questions and videos.
- Enroll students.
- API documentation available at `/docs`.

## Getting Started

To set up and run the project locally, follow these steps:

1. Clone this repository:

$ git clone https://github.com/satwiktandukar/AOMES_backend_prototype.git
$ cd educational-coaching-backend

2. Create a virtual environment on python
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the dependencies
$ cd ./AOMES_backend_prototype
$ pip install -r requirements.txt

4. Run it on your localhost
$ cd ./
$ uvicorn blog.main:app --reload

## For forwarding my server's address to be available globally, I used openvpn and portmap.io.

