# see https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#specifying-config-from-python-packages
def setup_xpra():
  return {
    # batchspawner-singleuser code-server --bind-addr 0.0.0.0 --auth none
    'command': ['xpra', 'start', '--bell=no', '--daemon=no', '--clipboard=yes', '--system-tray=yes', '--exit-with-children=yes', '--no-pulseaudio', '--bind-tcp=0.0.0.0:{port}', '--html=on', '--start-child=${XPRA_RUN_SCRIPT}']
  }

# singularity exec \
#        -B /etc/profile.d \
#        --nv ${XPRA_SING_IMG} \
#        xpra start --bell=no --daemon=no --clipboard=yes --system-tray=yes --exit-with-children=yes --no-pulseaudio --bind-tcp=0.0.0.0:${RANDOM_PORT} --html=on --start-child=${XPRA_RUN_SCRIPT} &

