FROM scratch
COPY hello-wasm-world.wasm /hello-wasm-world.wasm
ENTRYPOINT [ "/hello-wasm-world.wasm" ]