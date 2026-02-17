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
```
## Backend Image Publishing ##
On every push to the main branch, the build-and-publish.yaml GitHub Actions workflow is triggered.
The workflow automatically builds the backend Docker image and publishes it to GitHub Container Registry (GHCR) with an incremented version tag.

For simplicity, versions are represented as plain sequential numbers.
In the example below, you can see an automatically generated image with version 9.
<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/6a2b1fae-d97f-4881-a8be-dca60e6077ba" />
