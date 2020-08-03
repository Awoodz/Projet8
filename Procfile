release : python manage.py migrate
release : python manage.py dtb_builder
web: gunicorn pur_beurre_project.wsgi --log-file -
