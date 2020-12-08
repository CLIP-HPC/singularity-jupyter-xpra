# see https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#specifying-config-from-python-packages
def setup_xpra():
  return {
    #
    'command': ['xpra', 'start', '--bell=no', '--daemon=no', '--clipboard=yes', '--system-tray=yes', '--mdns=no', '--exit-with-children=no', '--no-pulseaudio', '--bind-tcp=127.0.0.1:{port}', '--html=on', '--start-child=/usr/local/bin/xterm.sh'],
    # we can take up to xx seconds to get ready
    'timeout': 60
  }

# singularity exec \
#        -B /etc/profile.d \
#        --nv ${XPRA_SING_IMG} \
#        xpra start --bell=no --daemon=no --clipboard=yes --system-tray=yes --exit-with-children=yes --no-pulseaudio --bind-tcp=0.0.0.0:${RANDOM_PORT} --html=on --start-child=${XPRA_RUN_SCRIPT} &


