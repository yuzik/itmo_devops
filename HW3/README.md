1. Установить и запустить Docker Desktop, убедиться что работает
![created](https://github.com/yuzik/itmo_devops/assets/60525058/9fc8fde1-63b1-47f2-bd73-0a538f427fab)
2.  Установить и запустить  minikube, убедиться что работает
[minikube](https://github.com/yuzik/itmo_devops/assets/60525058/432b4f6e-7937-403f-a487-24e19125dabc)
3. Создаем объекты через CLI. 3 объекта + 1 некстклайд
![created](https://github.com/yuzik/itmo_devops/assets/60525058/087188fe-33ee-4e49-b6d9-ac253446eee8)
4. Прогнать манифесты, чтоб описанные объекты создались в кластере
![run](https://github.com/yuzik/itmo_devops/assets/60525058/05a36254-d737-45ee-9e4c-99a5ae60d1ee)
5. Проверить, что все ресурсы успешно создались
![getall](https://github.com/yuzik/itmo_devops/assets/60525058/b8c16a4c-a3c8-4789-85ab-4b7dafdb1aab)
6. После успешного запуска пода можно проверить состояние некстклауд
![installed](https://github.com/yuzik/itmo_devops/assets/60525058/e52ae205-03d1-4cfa-bc80-1424fd65011d)

* Вопросы
Важен ли порядок выполнения этих манифестов? Почему?

* Ответы 
Да, важен, т.к конфиги определяют переменные переиспользуемые в дальнейшем , также без конфига kind: Secret хранить пароли небезопасно 
