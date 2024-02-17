<h1>Домашнее задание #12 (GraphQL)</h1>
<p>Создана схема GraphQL для получения данных: Список категорий курсов (Направления), Список курсов, Список пользователей (поле password не передается).</p>
<p>В Django реализована возможность записаться на курс.</p>
<p>Реализованы две группы пользователей со своим набором прав. Teachers (Преподаватели), CourseCreators (Создатели курсов). Права пользователей учитываются на Django и DRF.</p>
<p>CourseCreators - полные права на модели Course, CategoryCouse, Lesson</p>
<p>Teachers - полные права на модели Course, Lesson, Shedule. На модель CategoryCouse права - правка</p>
<p>После создания БД проекта нужно обязательно запустить "установку", чтобы создать группы.</p>
<p>Есть фильтрация и пагинация</p>
<h3>Алгоритм проверки</h3>
<ul>
<li> Создать БД <b>make migrate</b></li>
<li> Запустить первоначальную установку <b>make install</b>, создаются группы пользователей и суперадмин admin/admin</li>
<li> Заполнить БД демоданными: <b>make fill_db</b> Создаются пользователи учитель (teacher1/1), создатель курсов (creator1/1), студент (student1/1)</li>
<li> Запустить проект: <b>make runserver</b></li>
<li> Открыть конструктор запросов Graphql по ссылке http://localhost:8000/graphql/</li>
<li> Построить запрос, например, список курсов со списком преподавателей и подписанных студентов<br>
<pre>query MyQuery {
  courseList {
    name
    teachers {
      username
    }
    myeduSet {
      student {
        username
      }
    }
  }
}
</pre></li>
</ul>
<p>При работе проекьа с БД SQLlite, есть проблемы с фильтрацией. При работе с БД в PostgreSQL, все работает корректно</p>
