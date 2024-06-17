- **Задача**
    
    Развернуть свой собственный сервис в Kubernetes, по аналогии с ЛР 3

    Развернут сервис юпитерхаба со своим кастомным образом из докерфайла и в кач-ве второго сервиса постгрес 

Требования:

- минимум два `Deployment`, по количеству сервисов
юпитер + постгря = 2 сервиса

- кастомный образ для минимум одного `Deployment` (т.е. не публичный и собранный из своего *Dockerfile*)
юпитер как кастомный из *Dockerfile*
![dockerfile](https://github.com/yuzik/itmo_devops/assets/60525058/74118083-bbeb-457f-9bde-c4325d5d1d64)
- минимум один `Deployment` должен содержать в себе контейнер и инит-контейнер
пустой инит контейнер для юпитера
![init_container](https://github.com/yuzik/itmo_devops/assets/60525058/cf4c959f-e93f-4305-9b66-038df70b3efb)
- минимум один `Deployment`
должен содержать `volume` (любой)
есть в конфиге юпитера 
  ![volumes](https://github.com/yuzik/itmo_devops/assets/60525058/8d83631a-cd1a-4bb8-a05d-551af8a92caf)
- обязательно использование `ConfigMap` и/или `Secret`
также использовано в юпитере
 ![configmap](https://github.com/yuzik/itmo_devops/assets/60525058/e91a1969-5531-4620-abc5-bfd1e8b43868)
- обязательно `Service` хотя бы для одного из сервисов (что логично, если они работают в связке)
оба обернуты как `Service` 
![pg_service](https://github.com/yuzik/itmo_devops/assets/60525058/5e95b8e1-74cb-419c-b7b2-f35285143f14)
![jup_service](https://github.com/yuzik/itmo_devops/assets/60525058/3a3ae420-d8fa-4c55-b8d2-922205bc1462)
- `Liveness` и/или `Readiness` пробы минимум в одном из `Deployment`
`Liveness` есть в юпитере
![liveness](https://github.com/yuzik/itmo_devops/assets/60525058/f115cc03-1f3e-4602-9a38-3fb559d2974a)
- обязательно использование лейблов (помимо обязательных `selector/matchLabel`, конечно)
лэйблы также в юпитере 
![labels](https://github.com/yuzik/itmo_devops/assets/60525058/d8af25a1-78a5-4d87-977f-46b0e3ddcbed)
