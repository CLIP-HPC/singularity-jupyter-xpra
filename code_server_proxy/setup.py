import setuptools

setuptools.setup(
  name="jupyter-codeserver",
  # py_modules rather than packages, since we only have 1 file
  py_modules=['xpra'],
  entry_points={
      'jupyter_serverproxy_servers': [
          # name = packagename:function_name
          'xpra = xpra:setup_xpra',
      ]
  },
  install_requires=['jupyter-server-proxy'],
)

