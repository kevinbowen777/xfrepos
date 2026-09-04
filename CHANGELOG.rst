.. _`changelog`:

=========
Changelog
=========

``xfrepos`` issues are filed on `GitHub <https://github.com/kevinbowen777/xfrepos/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

xfrepos 0.9.1 (2026-09-04)
==========================

Contributor-facing changes
--------------------------

-  (`#29 <https://github.com/kevinbowen777/xfrepos/issues/29>`_): Add pyright section to pyproject.toml


Improved documentation
----------------------

-  (`#29 <https://github.com/kevinbowen777/xfrepos/issues/29>`_): Add towncrier 26.9.0.

xfrepos 0.9.0 (2026-09-01)
==========================

Contributor-facing changes
--------------------------

-  (`#30 <https://github.com/kevinbowen777/xfrepos/issues/30>`_): Rename master branch to main. Remove pylint.


New features
------------

-  (`#32 <https://github.com/kevinbowen777/xfrepos/issues/32>`_): Rename project to xfrepos.

xfrepos 0.8.7 (2026-08-28)
==========================

Contributor-facing changes
--------------------------

-  (`#1 <https://github.com/kevinbowen777/xfrepos/issues/1>`_): Replace os.path with pathlib.Path.

-  (`#10 <https://github.com/kevinbowen777/xfrepos/issues/10>`_): Install ruff. Drop flake8-* packages.

-  (`#11 <https://github.com/kevinbowen777/xfrepos/issues/11>`_): Add testing package(nox, coverage, ruff)

xfrepos 0.8.7 (2022-01-14)
==========================

Bug fixes
---------

- : adds error handling to failed clone attempts.

xfrepos 0.8.5 (2022-01-11)
==========================

Bug fixes
---------

- : Add error handling for KeyboardInterrupt


Contributor-facing changes
--------------------------

- : Re-factor main() & cleanup cappdata.py


New features
------------

- : Add press_any_key function.

xfrepos 0.8.4 (2021-12-31)
==========================

Bug fixes
---------

- : Menu banners improvement.

xfrepos 0.8.3 (2021-12-28)
==========================

Contributor-facing changes
--------------------------

- : Sync pyproject.toml with setup.py.

xfrepos 0.8.2 (2021-12-27)
==========================

Bug fixes
---------

- : Remove www group from clean & install scripts.


Contributor-facing changes
--------------------------

- : Add intial test placeholders.

- : Implement Poetry for dependency management & project info.

xfrepos 0.8.1 (2021-12-23)
==========================

Bug fixes
---------

- : Fix missing new lines in output.


Contributor-facing changes
--------------------------

- : Consolidate all repo info in cappdata.py.

- : Re-write main menu in Python.

- : Remove 38 redundant scripts.

xfrepos 0.7 (2021-12-16)
========================

Contributor-facing changes
--------------------------

- : Improved error handling.

xfrepos 0.6 (2021-02-17)
========================

Bug fixes
---------

- : Fix relative path issues


Contributor-facing changes
--------------------------

- : Mirror to GitLab.


New features
------------

- : Add build, clean, and clone scripts

- : Implement initial menu-driven functionality

xfrepos 0.0.1 (2019-06-22)
==========================

Miscellaneous internal changes
------------------------------

- : Initial commit
