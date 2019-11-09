FROM rust:latest AS builder

run set -xe; \
	apt-get update; \
	apt-get install -y musl musl-tools; \
	rm -rf /var/lib/apt/lists/*; \
	rustup target add x86_64-unknown-linux-musl; \
	cargo install --target x86_64-unknown-linux-musl mdbook; \
	mv /usr/local/cargo/bin/mdbook .; \
	rm -rf /usr/local/cargo/registry;

FROM alpine:latest

ENV MDBOOK_HOME=/opt/mdbook
ENV PATH="${MDBOOK_HOME}/bin:${PATH}"

COPY --from=builder ./mdbook ${MDBOOK_HOME}/bin/
