FROM python:3.11.1

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/venv_design_search

COPY requirements.txt .

RUN pip install -r requirements.txt

# この行を削除 RUN pip install django==4.2.4
# 代わりに、requirements.txtにdjango==4.2.4を含めるべき

# RUN mkdir /usr/src/venv_design_search この行は削除する

# COPY requirements.txt ./ この行は重複しているため不要

RUN pip install --upgrade pip

# RUN pip install -r requirements.txt この行は重複しているため不要

ADD . /usr/src/venv_design_search

CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]
