FROM centos:centos7

RUN yum -y update \
     && yum -y install git curl bzip2 libgfortran \
     && curl -sSL https://github.com/conda-forge/miniforge/releases/download/4.10.3-7/Mambaforge-Linux-x86_64.sh -o /tmp/mambaforge.sh \
     && bash /tmp/mambaforge.sh -bfp /usr/local \
     && rm -rf /tmp/mambaforge.sh \
     && mamba update mamba \
     && mamba clean --all --yes \
     && rpm -e --nodeps curl bzip2 \
     && yum clean all

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
      python-rapidjson geventhttpclient \
      brotli nomkl \
     && mamba clean -y --all \
     && pip install --no-cache-dir \
      --extra-index-url https://download.pytorch.org/whl/cpu/ \
      --extra-index-url https://google-coral.github.io/py-repo/ \
      "fastjet==3.3.4.0rc9" \
      tritonclient[all] \
      torch \
      tflite-runtime \
      onnxruntime

# Make a symbolic link between installation /opt/conda/etc/grid-security and actual directory /etc/grid-security
RUN ln -s /usr/local/etc/grid-security /etc/grid-security
