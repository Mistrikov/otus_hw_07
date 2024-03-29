<h1>Домашнее задание #13 (Взаимодействие с API через JavaScript)</h1>
<p>В папку проекта добавлена папка <b>frontend</b> для будущего SPA приложения на Vue</p>
<p>Взаимодействие с API через JavaScript реализовано 2 способами:</p>
<p>1. Через тестовую веб-страницу (никак не связана с Django) веб-страница доступна после запуска основного проекта по ссылке http://localhost:8000/static/test-fetch.html или http://localhost:8000/static/test-axios.html </p>
<p>Для доступа к API используется fetch и axios.</p>
<p>2. Через запуск скрипта на js через nodejs, с помощью команды <b>node ./src/index.js</b></p>
<p>В файле <b>./src/index.js</b> нужно раскоментировать функции с fetch или axios</p>
<br />
<h3>Алгоритм проверки</h3>
<ul>
<li> Создать виртуальное окружение <b>python -m venv venv</b></li>
<li> Активировать виртуальное окружение, в зависимости от ОС (venv\scripts\activate.bat или source venv/bin/activate)</li>
<li> Установить зависимости <b>pip install -r requirements.txt</b></li>
<li> Создать БД <b>make migrate</b></li>
<li> Запустить первоначальную установку <b>make install</b>, создаются группы пользователей и суперадмин admin/admin</li>
<li> Заполнить БД демоданными: <b>make fill_db</b> Создаются пользователи учитель (teacher1/1), создатель курсов (creator1/1), студент (student1/1)</li>
<li> Запустить проект: <b>make runserver</b></li>
<li> Открыть второе окно терминала, зайти в папку frontend и установить зависимости node командой <b>npm install</b></li>
<li> Запустить скрипт на исполнение командой <b>node ./src/index.js</b><br>
<p>При работе проекьа с БД SQLlite, есть проблемы с фильтрацией. При работе с БД в PostgreSQL, все работает корректно</p>
