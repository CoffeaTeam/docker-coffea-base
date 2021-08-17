FROM centos:centos7 as builder

RUN yum -y update \
     && yum -y install automake autoconf make libtool curl bzip2 git gcc-c++ gcc-gfortran swig3 mpfr mpfr-devel boost boost-devel \
     && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
     && bash /tmp/miniconda.sh -bfp /usr/local/ \
     && rm -rf /tmp/miniconda.sh \
     && conda update conda \
     && conda clean --all --yes \
     && yum clean all

RUN conda install --yes --freeze-installed -c conda-forge conda-build python==3.8.* \
     && conda clean --all -f -y \
     && conda build purge-all

RUN pip install "fastjet==3.3.4.0rc8" -v

RUN mkdir -p /artifacts \
     && cp -rp $(python -c 'import fastjet; import pathlib; print(pathlib.Path(fastjet.__file__).parent)')* /artifacts

FROM centos:centos7

RUN yum -y update \
     && yum -y install curl bzip2 libgfortran \
     && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
     && bash /tmp/miniconda.sh -bfp /usr/local/ \
     && rm -rf /tmp/miniconda.sh \
     && conda update conda \
     && conda clean --all --yes \
     && rpm -e --nodeps curl bzip2 \
     && yum clean all

# XRootD + CA + VOMS + Coffea
RUN conda install --yes --freeze-installed \
      -c conda-forge \
      conda-build \
      voms \
      jupyterlab \
      dask_labextension \
      python==3.8.* \
      ca-policy-lcg \
      xrootd==5.2.0 \
      "uproot>=4.0.8" \
      coffea==0.7.6 \
      vector \
      lz4 python-xxhash zstandard \
     && conda clean --all -f -y \
     && conda build purge-all

# This is very delicate but it keeps the image size reasonable...
COPY --from=builder /artifacts /usr/local/lib/python3.8/site-packages

# Make a symbolic link between installation /opt/conda/etc/grid-security and actual directory /etc/grid-security
RUN ln -s /opt/conda/etc/grid-security /etc/grid-security
