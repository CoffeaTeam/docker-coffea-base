FROM continuumio/miniconda3:latest

# XRootD + CA + VOMS + Coffea
RUN conda install --yes --freeze-installed \
      -c conda-forge \
      conda-build \
      voms \
      python==3.8.* \
      ca-policy-lcg \
      xrootd==5.0.3 \
      coffea==0.6.45 \
      && conda clean -tipsy \
      && find /opt/conda/ -type f,l -name '*.a' -delete \
      && find /opt/conda/ -type f,l -name '*.pyc' -delete \
      && find /opt/conda/ -type f,l -name '*.js.map' -delete \
      && rm -rf /opt/conda/pkgs \
      && conda build purge-all
