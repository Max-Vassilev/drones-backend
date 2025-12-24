# drones-backend

I integrated Redis caching for the products page.
The first request (~85 ms) hits the database and later requests (~1 ms) are served from cache showing a clear performance improvement.
Here are the backend logs showing cache miss and cache hits with Redis:
```bash
[REDIS] Cache MISS
[REDIS] Cache SET | 0.0852s
172.18.0.1 - - [24/Dec/2025 13:43:03] "GET /products HTTP/1.1" 200 -
[REDIS] Cache HIT | 0.0008s
172.18.0.1 - - [24/Dec/2025 13:43:03] "GET /products HTTP/1.1" 200 -
[REDIS] Cache HIT | 0.0010s
```
