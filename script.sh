cd /Users/liuchunhua/Documents/GitHub/Server/python/wqm
rm -rf db.sqlite3
rm -rf app001/migrations
rm -rf appA/migrations

python manage.py makemigrations
python manage.py migrate

python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'root@example.com', 'root')" | python manage.py shell

python manage.py makemigrations app001
python manage.py migrate app001

python manage.py makemigrations appA
python manage.py migrate appA

