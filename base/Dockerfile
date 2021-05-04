FROM continuumio/miniconda3:latest

RUN apt-get update \
     && apt-get install -yq --no-install-recommends libarchive-dev \
     && apt-get clean && rm -rf /var/lib/apt/lists/*

# XRootD + CA + VOMS + Coffea
RUN conda install --yes --freeze-installed \
      -c conda-forge \
      conda-build \
      voms \
      jupyterlab \
      dask_labextension \
      python==3.8.* \
      ca-policy-lcg \
      xrootd==5.1.1 \
      coffea==0.7.2 \
      lz4 python-xxhash zstandard \
      && conda clean --all -f -y \
      && conda build purge-all

# Make a symbolic link between installation /opt/conda/etc/grid-security and actual directory /etc/grid-security
RUN ln -s /opt/conda/etc/grid-security /etc/grid-security
