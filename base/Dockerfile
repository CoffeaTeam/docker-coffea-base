FROM condaforge/mambaforge:4.11.0-0

ENV DEBIAN_FRONTEND="noninteractive"
ENV TZ="Etc/UTC"

RUN apt-get update \
     && apt-get install -yq --no-install-recommends libarchive-dev \
     && apt-get clean && rm -rf /var/lib/apt/lists/*

# XRootD + CA + VOMS + Coffea
RUN mamba install --yes \
      -c conda-forge -c pytorch \
      conda-build \
      voms \
      jupyterlab \
      ipympl \
      dask_labextension \
      python==3.8.* \
      ca-policy-lcg \
      xrootd==5.4.0 \
      "uproot>=4.0.8" \
      "numpy<1.22" \
      coffea==0.7.18 \
      vector xgboost \
      lz4 python-xxhash zstandard \
      pytables \
      python-rapidjson grpcio geventhttpclient \
      protobuf brotli onnxruntime \
      pytorch cpuonly \
     && mamba clean -y --all \
     && pip install --no-cache-dir \
      --extra-index-url https://google-coral.github.io/py-repo/ \
      "fastjet==3.3.4.0rc9" \
      tritonclient[all] \
      tflite_runtime

# Make a symbolic link between installation /opt/conda/etc/grid-security and actual directory /etc/grid-security
RUN ln -s /opt/conda/etc/grid-security /etc/grid-security
