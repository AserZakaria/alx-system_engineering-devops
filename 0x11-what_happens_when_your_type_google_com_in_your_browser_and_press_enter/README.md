# What Happens When You Type `https://www.google.com` in Your Browser?

## Beginning
The article explains the step-by-step process that occurs when you type `https://www.google.com` in your browser and press Enter. Let's dive into each stage:

### 1. DNS Request
- Your browser sends a DNS request to a resolver.
- The resolver looks up the IP address associated with `www.google.com`.

### 2. TCP/IP
- Your browser initiates a TCP connection to the obtained IP address.
- TCP ensures reliable data transmission.

### 3. Firewall
- The request passes through any firewalls or security measures.
- Firewalls can block or allow traffic based on rules.

### 4. HTTPS/SSL
- The browser establishes an SSL/TLS connection with the server.
- SSL certificates verify authenticity and encrypt data.

### 5. Load Balancer
- If used, the request reaches a load balancer.
- Load balancers distribute requests across servers.

### 6. Web Server
- load balancer forwards the request to a web server.
- Web server processes the request and constructs an HTTP response.

### 7. Application Server
- For dynamic, the request goes to an application server.
- Server-side code (As Python) generates dynamic content.

### 8. Database
- The application server queries a database.
- The database retrieves requested data.

## Conclusion
1. The application server constructs an HTTP response.
2. The response travels back to your browser.
3. You see the google page
