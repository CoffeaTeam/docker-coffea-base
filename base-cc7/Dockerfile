FROM centos:centos7

RUN yum -y update \
     && yum -y install curl bzip2 libgfortran \
     && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
     && bash /tmp/miniconda.sh -bfp /usr/local \
     && rm -rf /tmp/miniconda.sh \
     && conda update conda \
     && conda clean --all --yes \
     && rpm -e --nodeps curl bzip2 \
     && yum clean all

# XRootD + CA + VOMS + Coffea
RUN conda install mamba -n base -c conda-forge --yes
RUN mamba install --yes \
      -c conda-forge \
      conda-build \
      voms \
      jupyterlab \
      ipympl \
      dask_labextension \
      python==3.8.* \
      ca-policy-lcg \
      xrootd==5.3.0 \
      "uproot>=4.0.8" \
      coffea==0.7.8 \
      vector xgboost \
      lz4 python-xxhash zstandard \
      pytables \
     && mamba clean -tipsy \
     && pip install --no-cache-dir "fastjet==3.3.4.0rc9"

# Make a symbolic link between installation /opt/conda/etc/grid-security and actual directory /etc/grid-security
RUN ln -s /usr/local/etc/grid-security /etc/grid-security
