FROM condaforge/mambaforge:4.11.0-0

ENV DEBIAN_FRONTEND="noninteractive"
ENV TZ="Etc/UTC"

RUN apt-get update \
     && apt-get install -yq --no-install-recommends libarchive-dev \
     && apt-get clean && rm -rf /var/lib/apt/lists/*

# XRootD + CA + VOMS + Coffea
RUN mamba install --yes \
      -c conda-forge \
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
      coffea==0.7.19 \
      vector xgboost \
      lz4 python-xxhash zstandard \
      pytables \
      python-rapidjson geventhttpclient \
      brotli nomkl \
     && mamba clean -y --all \
     && pip install --no-cache-dir \
      --extra-index-url https://download.pytorch.org/whl/cpu/ \
      --extra-index-url https://google-coral.github.io/py-repo/ \
      "fastjet==3.4.0.0rc2" \
      tritonclient[all] \
      torch \
      tflite-runtime \
      onnxruntime \
     && pip install --no-cache-dir \
      torch-scatter torch-sparse torch-cluster torch-spline-conv -f https://data.pyg.org/whl/torch-1.12.0+cpu.html \
     && pip install --no-cache-dir \
      torch-geometric

# Make a symbolic link between installation /opt/conda/etc/grid-security and actual directory /etc/grid-security
RUN ln -s /opt/conda/etc/grid-security /etc/grid-security
