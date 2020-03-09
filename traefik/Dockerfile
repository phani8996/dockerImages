FROM traefik:1.7.2-alpine
COPY traefik.toml /
COPY acme.json /
RUN ln -s /var/run/balena.sock /var/run/docker.sock
CMD ["traefik", "-l", "INFO"]
