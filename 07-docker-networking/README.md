# Docker Networking & Volume

## Task 1: Networking
Created frontend, backend, and db networks. Connected backend to both frontend and db networks. Successfully pinged db from backend, but frontend could not reach db, proving network isolation.

## Task 2: Host Network
`docker run -d --network host httpd`
Accessed apache on localhost:80 without `-p` flag.

## Task 3: Bind Mount
`docker run -d -v $(pwd)/html:/usr/share/nginx/html -p 8080:80 nginx`
Changes to `index.html` on host immediately reflected in the container.

## Task 4: Overlay Network
Overlay networks are used in Docker Swarm to allow containers on different physical host machines to communicate securely.