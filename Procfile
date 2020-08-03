web: gunicorn pur_beurre_project.wsgi --log-file -
python manage.py flush
python manage.py migrate
python manage.py dtb_builder