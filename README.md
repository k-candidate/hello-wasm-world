# hello-wasm-world

To create the wasm:
```
py2wasm hello-wasm-world.py -o hello-wasm-world.wasm
```

To run the wasm:
```
wasmer run hello-wasm-world.wasm
```
## Docker
How does Docker work with WASM?  
cli <-> dockerd <-> containerd <-> shim <-> wasm rt (replacing runc) <-> registry

To create the wasm docker image:
```
docker build -t kcandidate/hello-wasm-world:v1 --platform wasi/wasm32 .
```

To use a wasm runtime for docker, use these instructions: 
https://docs.docker.com/engine/daemon/alternative-runtimes/.
But those instructions are incomplete.  
The daemon configuration file is `/etc/docker/daemon.json`:
```
{
  "features": {
    "containerd-snapshotter": true
  }
}
```
To build the wasmtime binary, you'll need `protobuf-compiler` and `libseccomp-dev` which are not present in the build stage image used in the Docker docs. Alternatively, you can just get the precompiled binary from https://github.com/containerd/runwasi/releases
```
docker build --output . - <<EOF
FROM rust:latest as build
RUN apt update && apt install -y protobuf-compiler libseccomp-dev
RUN cargo install \
    --git https://github.com/containerd/runwasi.git \
    --bin containerd-shim-wasmtime-v1 \
    --root /out \
    containerd-shim-wasmtime
FROM scratch
COPY --from=build /out/bin /
EOF
```
To run the wasm docker image:
```
docker run --runtime=io.containerd.wasmtime.v1 --platform=wasi/wasm kcandidate/hello-wasm-world:v1
```

## Results
Running `python hello-wasm-world.py`:
```
Elapsed time for range sum: 0.001385 seconds
Pystone(1.1) time for 50000 passes = 0.124373
This machine benchmarks at 402016 pystones/second
```  
Running `wasmer run hello-wasm-world.wasm`:
```
Elapsed time for range sum: 0.000775 seconds
Pystone(1.1) time for 50000 passes = 0.227372
This machine benchmarks at 219904 pystones/second
```  
Running `docker run --runtime=io.con
tainerd.wasmtime.v1 --platform=wasi/wasm32 kcandidate/hello-wasm-world:v1`:
```
Elapsed time for range sum: 0.000921 seconds
Pystone(1.1) time for 50000 passes = 0.238069
This machine benchmarks at 210023 pystones/second
```