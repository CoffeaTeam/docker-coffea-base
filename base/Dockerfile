FROM continuumio/miniconda3:latest

# XRootD + CA + VOMS + Coffea
RUN conda install --yes --freeze-installed \
      -c conda-forge \
      conda-build \
      voms \
      python==3.8.* \
      ca-policy-lcg \
      xrootd==5.0.3 \
      coffea==0.6.47 \
      && conda clean --all -f -y \
      && conda build purge-all

# Make a symbolic link between installation /opt/conda/etc/grid-security and actual directory /etc/grid-security
RUN ln -s /opt/conda/etc/grid-security /etc/grid-security
