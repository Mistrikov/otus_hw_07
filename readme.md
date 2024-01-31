<h1>Домашнее задание #11 (Создать rest-api для сайта)</h1>
<p>В api реализована авторизация по JWTAuthentication по ссылке http://localhost:8000/api/token/. В корне проекта есть файл console_client.py, в котором содержится код проверки авторизации и получения токена.</p>
<p>Реализованы две группы пользователей со своим набором прав. Teachers (Преподаватели), CourseCreators (Создатели курсов). Права пользователей учитываются на Django и DRF.</p>
<p>CourseCreators - полные права на модели Course, CategoryCouse, Lesson</p>
<p>Teachers - полные права на модели Course, Lesson, Shedule. На модель CategoryCouse права - правка</p>
<p>После создания БД проекта нужно обязательно запустить "установку", чтобы создать группы.</p>
<h3>Алгоритм проверки</h3>
<ul>
<li> Создать БД <b>make migrate</b></li>
<li> Запустить первоначальную установку <b>make install</b>, создаются группы пользователей и суперадмин admin/admin</li>
<li> Заполнить БД демоданными: <b>make fill_db</b> Создаются пользователи учитель (teacher1/1), создатель курсов (creator1/1)</li>
<li> Запустить проект: <b>make runserver</b> или <b>python manage.py runserver</b></li>
</ul>
