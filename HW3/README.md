1. Установить и запустить Docker Desktop, убедиться что работает
![docker](https://github.com/yuzik/itmo_devops/assets/60525058/871815f2-4b67-4eb4-8079-567df166a698)
3.  Установить и запустить  minikube, убедиться что работает
![minikube](https://github.com/yuzik/itmo_devops/assets/60525058/8969e42f-1cf9-4b81-a03d-87c95513851c)
5. Создаем объекты через CLI. 3 объекта + 1 некстклайд
![created](https://github.com/yuzik/itmo_devops/assets/60525058/087188fe-33ee-4e49-b6d9-ac253446eee8)
6. Прогнать манифесты, чтоб описанные объекты создались в кластере
![run](https://github.com/yuzik/itmo_devops/assets/60525058/05a36254-d737-45ee-9e4c-99a5ae60d1ee)
7. Проверить, что все ресурсы успешно создались
![getall](https://github.com/yuzik/itmo_devops/assets/60525058/b8c16a4c-a3c8-4789-85ab-4b7dafdb1aab)
8. После успешного запуска пода можно проверить состояние некстклауд
![installed](https://github.com/yuzik/itmo_devops/assets/60525058/e52ae205-03d1-4cfa-bc80-1424fd65011d)

UDP после проверки 

9. Для некстклауда добавлены Liveness и Readiness пробы в самый конец nextcloud.yml
   
![for_nextcloud](https://github.com/yuzik/itmo_devops/assets/60525058/ee5619a2-b0bf-44d7-aeb1-c459490f81c4)
11. Для постгреса перенести POSTGRES_USER и POSTGRES_PASSWORD из конфигмапы в секреты pg_secrets.yml

![for_pg](https://github.com/yuzik/itmo_devops/assets/60525058/a0576248-00ca-4af8-aa7e-b2d159b7a468)
12. Для некстклауда перенесены его переменные (NEXTCLOUD_UPDATE, ALLOW_EMPTY_PASSWORD и проч.) из деплоймента в конфигмапу nextcloud_configmap.yml

![for_nextcloud_configmap](https://github.com/yuzik/itmo_devops/assets/60525058/c2723017-1dfd-403e-a603-53664a39ee41)
* Вопросы
Важен ли порядок выполнения этих манифестов? Почему?

* Ответы 
Да, важен, т.к конфиги определяют переменные переиспользуемые в дальнейшем , также без конфига kind: Secret хранить пароли небезопасно 

* Вопросы
Что (и почему) произойдет, если отскейлить количество реплик postgres-deployment в 0, затем обратно в 1, после чего попробовать снова зайти на Nextcloud?

* Ответы 
Когда реплики постгри будут 0, некстклауд не сможет подключиться к бд (т.к бд нет) и выдаст ошибку, когда опять 1, постгря поднимется, но уже без данных, т.к мы не монтировали вольюмы, в итоге некстклауд все равно будет выдавать ошибку  
