# pip-additions
**Additional Python pip utilities**


## parse_requirements

#### Description
**parse_requirements** returns "supported" and "unsupported requirements.  Supported requirements are those that can be installed through pip using **setuptools.setup**; any package in PyPi.  Unsupported requirements are those that cannot be installed through pip and setuptools, but _can_ be installed through pip itself; mainly, private github repositories.

#### Usage
```
import pip_additions
requirements_results = pip_additions.parse_requirements()
supported_requirements = requirements_results.req
unsupported_requirements = requirements_results.ureq
```

## install_unsupported

#### Description
**install_unsupported** allows easy installation of unsupported packages.

#### Usage
```
import pip_additions
requirements_results = pip_additions.parse_requirements()
supported_reqs = requirements_results.req
unsupported_reqs = requirements_results.ureq

pip_additions.install_unsupported(unsupported_reqs)
```
