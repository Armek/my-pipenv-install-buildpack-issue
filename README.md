I'm trying to get my build to work with Paketo's pipenv-install buildpack.  

I can build this app and run it in a docker container fine with just the pipfile + Python 3.11 base:
```shell
# Run in example-app folder
# requires nvidia gpu
docker build -t test .
docker run --gpus all test 
# outputs: [{'translation_text': "Il s'agit d'un test"}]
```

I can build the pipenv example project fine and execute it.  But as soon as I introduce my pipenv + lockfile I get:
```shell
# Run in example-app folder
# Output by: pack build test
Paketo Buildpack for CPython 1.13.0
  Resolving CPython version
    Candidate version sources (in priority order):
      Pipfile.lock -> "3.11"
                   -> ""
      <unknown>    -> ""

    Selected CPython version (using Pipfile.lock): 3.11.8

  Executing build process
    Installing CPython 3.11.8
      Completed in 5.729s

  Generating SBOM for /layers/paketo-buildpacks_cpython/cpython
      Completed in 0s


  Configuring build environment
    PYTHONPATH          -> "/layers/paketo-buildpacks_cpython/cpython"
    PYTHONPYCACHEPREFIX -> "/tmp"

  Configuring launch environment
    PYTHONPATH -> "/layers/paketo-buildpacks_cpython/cpython"

Paketo Buildpack for Pip 0.20.1
  Resolving Pip version
    Candidate version sources (in priority order):
       -> ""

    Selected Pip version (using ): 23.3.2

  Executing build process
    Installing Pip 23.3.2
      Completed in 12.489s

  Generating SBOM for /layers/paketo-buildpacks_pip/pip
      Completed in 0s

  Configuring build environment
    PIP_FIND_LINKS -> "$PIP_FIND_LINKS /layers/paketo-buildpacks_pip/pip-source"

  Configuring build environment
    PYTHONPATH -> "/layers/paketo-buildpacks_pip/pip/lib/python3.11/site-packages:$PYTHONPATH"

  Configuring launch environment
    PYTHONPATH -> "/layers/paketo-buildpacks_pip/pip/lib/python3.11/site-packages:$PYTHONPATH"

Paketo Buildpack for Pipenv 1.21.0
  Resolving Pipenv version
    Candidate version sources (in priority order):
       -> ""

    Selected Pipenv version (using ): 2023.12.1

  Executing build process
    Installing Pipenv 2023.12.1
      Completed in 6.744s

  Generating SBOM for /layers/paketo-buildpacks_pipenv/pipenv
      Completed in 0s

  Configuring build environment
    PYTHONPATH -> "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages:$PYTHONPATH"

  Configuring launch environment
    PYTHONPATH -> "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages:$PYTHONPATH"

Paketo Buildpack for Pipenv Install 0.6.19
  Executing build process
    Running 'pipenv install --deploy'
pipenv install failed:
Installing dependencies from Pipfile.lock (576229)...
Traceback (most recent call last):
  File "/layers/paketo-buildpacks_pipenv/pipenv/bin/pipenv", line 8, in <module>
    sys.exit(cli())
             ^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/vendor/click/core.py", line 1157, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/cli/options.py", line 58, in main
    return super().main(*args, **kwargs, windows_expand_args=False)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/vendor/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/vendor/click/core.py", line 1688, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/vendor/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/vendor/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/vendor/click/decorators.py", line 92, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/vendor/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/cli/command.py", line 209, in install
    do_install(
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/routines/install.py", line 164, in do_install
    do_init(
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/routines/install.py", line 680, in do_init
    do_install_dependencies(
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/routines/install.py", line 438, in do_install_dependencies
    batch_install(
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/routines/install.py", line 503, in batch_install
    deps_to_install = [
                      ^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/routines/install.py", line 506, in <listcomp>
    if not project.environment.is_satisfied(dep)
           ^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/project.py", line 512, in environment
    self._environment = self.get_environment(allow_global=allow_global)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/project.py", line 498, in get_environment
    environment = Environment(
                  ^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/environment.py", line 75, in __init__
    self._base_paths = self.get_paths()
                       ^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/environment.py", line 375, in get_paths
    c = subprocess_run(command)
        ^^^^^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_pipenv/pipenv/lib/python3.11/site-packages/pipenv/utils/processes.py", line 72, in subprocess_run
    return subprocess.run(
           ^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_cpython/cpython/lib/python3.11/subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/layers/paketo-buildpacks_cpython/cpython/lib/python3.11/subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/layers/paketo-buildpacks_cpython/cpython/lib/python3.11/subprocess.py", line 1953, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: '/workspace/.venv/bin/python'

error: exit status 1
```

I can get a simple example version of this app without torch + transformers dependencies working with the build, 
but I can't get it working with torch+transformers.  

What am I doing wrong, Paketo Community?  I've tried this on both the jammy base and full builders.  