# see https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html#specifying-config-from-python-packages
def setup_xpra():
  import os
  vglrun_wrapper = []
  if 'VGL_DISPLAY' in os.environ:
      vglrun_wrapper = ['--exec-wrapper=/opt/VirtualGL/bin/vglrun']
  return {
    #
    'command': ['xpra', 'start', '--no-pulseaudio', '--daemon=no', '--bind-tcp=0.0.0.0:{port}', '--start-child=/usr/local/bin/xterm.sh'] + vglrun_wrapper,
    # we can take up to xx seconds to get ready
    'timeout': 60
  }
# singularity exec \
#        -B /etc/profile.d \
#        --nv ${XPRA_SING_IMG} \
#        xpra start --bell=no --daemon=no --clipboard=yes --system-tray=yes --exit-with-children=yes --no-pulseaudio --bind-tcp=0.0.0.0:${RANDOM_PORT} --html=on --start-child=${XPRA_RUN_SCRIPT} &


