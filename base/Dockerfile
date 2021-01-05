FROM continuumio/miniconda3:latest

# XRootD + CA + VOMS + Coffea
RUN conda install --yes --freeze-installed \
      -c conda-forge \
      conda-build \
      voms \
      python==3.8.* \
      ca-policy-lcg \
      xrootd==5.0.3 \
      coffea==0.6.50 \
      && conda clean --all -f -y \
      && conda build purge-all

# Make a symbolic link between installation /opt/conda/etc/grid-security and actual directory /etc/grid-security
RUN ln -s /opt/conda/etc/grid-security /etc/grid-security

# Set up a working directory (user must mount)
WORKDIR work

ENV JUPYTER_PATH=/work/.jupyter
ENV JUPYTER_RUNTIME_DIR=/work/.local/share/jupyter/runtime
ENV JUPYTER_DATA_DIR=/work/.local/share/jupyter
ENV IPYTHONDIR=/work/.ipython
