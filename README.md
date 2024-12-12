# hello-wasm-world

To create the wasm:
```
py2wasm hello-wasm-world.py -o hello-wasm-world.wasm
```

To run the wasm:
```
wasmer run hello-wasm-world.wasm
```

To create the wasm docker image:
```
docker build -t kcandidate/hello-wasm-world:v1 --platform wasm32/wasi .
```

To use a wasm runtime for docker: 
https://docs.docker.com/engine/daemon/alternative-runtimes/

To run the wasm docker image:
```
docker run --runtime=io.containerd.wasmtime.v1 --platform=wasi/wasm kcandidate/hello-wasm-world:v1
```