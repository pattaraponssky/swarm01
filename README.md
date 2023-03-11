# SWARM01
## Ref awaresome-compose
* https://github.com/docker/awesome-compose/tree/master/fastapi

## WakaTime Project
* https://wakatime.com/@spcn11/projects/hmshipoaft

## Url
* https://spcn11swarm01.xops.ipv9.me/

## ขั้นตอนการสร้าง

- เลือก awesome-compose ที่ต้องการแล้วทำการ clone มาแก้ไขใน vscode

   - https://github.com/docker/awesome-compose

- แก้ไขข้อความที่ต้องการจะแสดงใน main.py

![image](https://user-images.githubusercontent.com/113360594/224477986-e75ff722-8d85-4727-b36c-41f2d44ea2ea.png)

- build images จากตัว Dockerfile

![image](https://user-images.githubusercontent.com/113360594/224477756-2ffc6121-fbb5-4be0-962c-10beadf07996.png)

- เข้าสู่ระบบ docker hub โดยใช้คำสั่ง 

      docker login

- แล้ว push ขึ้น docker hub ของเรา

      docker push pattaraponssky/swarm01-fastapi:1.0

### STACK DEPLOY

 - สร้างไฟล์คำสั่งไว้

        version: '3.3'
        services:
          api:
            image: pattaraponssky/swarm01-fastapi:1.0
            container_name: fastapi-application
            environment:
             PORT: 8000
            restart: "no"
            networks:
              - webproxy
            logging: 
              driver: json-file
            deploy:
              replicas: 1
              labels:
                - traefik.docker.network=webproxy
                - traefik.enable=true
                - traefik.http.routers.spcn11swarm01-https.entrypoints=websecure
                - traefik.http.routers.spcn11swarm01-https.rule=Host("spcn11swarm01.xops.ipv9.me")
                - traefik.http.routers.spcn11swarm01-https.tls.certresolver=default
                - traefik.http.services.spcn11swarm01.loadbalancer.server.port=8000   
        networks:
          webproxy:
            external: true

- deploy stack ที่ https://portainer.ipv9.me/ 

![image](https://user-images.githubusercontent.com/113360594/224478743-ef9649a9-197d-45b0-8d9e-b9e21e55ac52.png)

- ตรวจสอบ url ที่ใช้งาน
   
   - https://spcn11swarm01.xops.ipv9.me/

![image](https://user-images.githubusercontent.com/113360594/224477935-7b018e2f-0cd8-4e8b-b8e9-3ec17d1c8dba.png)
