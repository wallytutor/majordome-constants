# majordome-constants

Crate providing constants to the Majordome stack.

## Development builds

All is handled through `develop.py` script. It will build, install, and import the extension for you to inspect the contents in an interactive session. The recommended way is to run `ipython -i develop.py` to keep the interactive session alive for further testing. The most common options are listed below:

```bash
# See all available options
ipython develop.py -- -h

# Disable building the docs:
ipython develop.py -- --no-docs

# Open the docs after building:
ipython develop.py -- --open-docs

# Build in release mode:
ipython develop.py -- --release
```
