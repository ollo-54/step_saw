
Задание на разработку автотестов для проектов курса по Flask.  
https://docs.google.com/document/d/1fzfBl-oAmLyoQum0Rhh8FpL6Rc1IGkKRe2IsoqAn-58/edit?usp=sharing
  
Варианты запуска:  

pytest -s -v --link=https://URL_главной_страницы_Вашего_проекта.com/ test_main_page.py  - тесты для главной страницы, например, https://stepik-flask01.herokuapp.com/.  

pytest -s -v --link=https://URL_главной_страницы_Вашего_проекта.com/ test_departure_page.py  - тесты для страниц направлений.  
