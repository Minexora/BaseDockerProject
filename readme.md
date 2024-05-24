# Docker Base Project
Projenin yapılış amacı doğrudan docker yapısının entegrasyonunun sağlanmasıdır.

## Proje Anlatımı
1. **Src** klasörünün altına proje koyulur.
2. **initDB** klasörü bu proje için mongo init database yapıları için yazılmıştır. Sizler kendi dbnize göre kaldırabilir veya buraya yapınızı yazabilirsiniz. 
3. **nginx** klasörü nginx için gerekli config dosyalarının olduğu klasördür. 
4. **docker-entrypoint.sh** dosyası normalde projenin gunicorn gibi işlemlerinin yazıldığı ssh dosyasıdır. Bu dosya **docker-compose.yml** adlı dosyada web servisinde bulunan **command** alanına "bash docker-compose.yml" şekilinde yazılarak ek işlemlerde gerçekleşttirilebilir.
 
## Kurulum
1. Docker kurulmalıdır. [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/) adresinde söylenildiği gibi kurulmalıdır.
2.Docker containerların oluşup çalışması için aşağıdaki kod yazılır.
    ```bash
    docker-compose up -d
    ```