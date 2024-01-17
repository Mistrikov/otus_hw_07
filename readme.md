<h1>Домашнее задание #9 (Django №4 Очереди задач)</h1>
<p>На страницу <b>Контакты</b> добавлена форма для отправки вопросов посетителя сайта.</p>
<p>Вопросы посетитей сохраняются в базе и можно посмотреть через админку (ContactMessage)</p>
<p>Письма сохраняются в папке <b>emails</b> в корне проекта</p>
<p>Отправка письма посетителю сайта сделана через django_rq (mainapp/jobs.py), а отправка письма администраторам сайта сделано через celery (mainapp/tasks.py)</p>
<h3>Алгоритм проверки</h3>
<ul>
<li> Запустить Redis: <b>docker compose up -d redis</b></li>
<li> Создать БД <b>make migrate</b></li>
<li> Заполнить БД демоданными: <b>make fill_db</b></li>
<li> Запустить проект: <b>make runserver</b> или <b>python manage.py runserver</b></li>
<li> Запустить воркер django_rq командой <b>python manage.py rqworker</b></li>
<li> Запустить воркер celery командой <b>celery -A settings worker -l INFO</b></li>
<li> На странице <b>Контакты</b> заполнить форму и отправить сообщение</li>
<li> В папке <b>emails</b> должно появиться два письма</li>
</ul>
