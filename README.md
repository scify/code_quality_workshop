# Overview

## What we need?

1. We need to make sure our code is maintainable and readable at all times.
2. We need to catch code smells as soon as possible.
3. We need a common style of writting for better in between team readability.

## How?

By enforcing:

1. Linters
2. Formatters


## Linting


### What is a Linter

A linter can:
- Catch code smells
- Find code that is not compliant to a certain style guideline (such as PEP8)

### PEP8

PEP8 is a very impactful style guide for python.

Example:

```
x=5 -> no
x =5 -> no
x = 5 -?ye
```

### Proposed Linter

ruff (https://github.com/astral-sh/ruff)

From the command line:

```
ruff check --select=E,T201 .
ruff check --select=ALL .
```

### Rule examples

- pep8-naming (N) https://docs.astral.sh/ruff/rules/#pep8-naming-n
- flake8-print (T20) https://docs.astral.sh/ruff/rules/#flake8-print-t20
- flake8-bandit (S) https://docs.astral.sh/ruff/rules/#flake8-bandit-s


## Formatting


### What is a Formatter?

Formats source code automatically.

Examples:
- Replace tabs with 4 spaces
- Split a too long line

It accomplises consistency in the code base and among programmers.

### Proposed Formatters


black (https://github.com/psf/black)
isort (https://pycqa.github.io/isort/)





#### Isort

Sorts and groups our Imports.

Example (source: https://pycqa.github.io/isort/):

Before isort:
```
from my_lib import Object

import os

from my_lib import Object3

from my_lib import Object2

import sys

from third_party import lib15, lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8, lib9, lib10, lib11, lib12, lib13, lib14

import sys

from __future__ import absolute_import

from third_party import lib3

print("Hey")
print("yo")
```

After isort:

```
from __future__ import absolute_import

import os
import sys

from third_party import (lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8,
                         lib9, lib10, lib11, lib12, lib13, lib14, lib15)

from my_lib import Object, Object2, Object3

print("Hey")
print("yo")
```

#### Black formatter

- Is opinionated (limited configuration options)
- Has integration with InteliJ, VSCode
- industry standard

##### Is Black safe to use?

Yes. [..] Black strives to ensure that after formatting the AST is checked with limited special cases where the code is allowed to differ. If issues are found, an error is raised and the file is left untouched.[..]
(source: https://black.readthedocs.io/en/stable/faq.html#is-black-safe-to-use)


##### Running black

Show the changes that will be made:
```
black . --diff
```

run black formatter:
```
black .
```


## Where can we enforce those?

- On commit
- On push/merge


### Enforcing on commit

pre-commit (https://pre-commit.com/) is a tool to easily manage git hooks. With pre-commit we can install git hooks for all the tools
discussed so far.

That way, every time we commit all these tools will run and will reject our commit if they don't pass.

#### Usage

First we create a configuration file that will hold pre-commit configurations.

Example:
```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
    -   id: black
```

Now every time we commit the hooks will run.

#### pre-commit CLI

We can run hooks without commiting from the cli. This can easily bundle all our tools together!

```
pre-commit run --all-files
```

We can also specify a hook to skip when we want to commit:
```
SKIP=flake8 git commit -m "foo"
```


Note: Ruff's lint hook should be placed after other formatting tools, such as Ruff's format hook, Black, or isort.

### Enforcing on Push/Merge

Github Actions

We can enforce certain actions to run when either a push is made, a pull request is created etc.

That is what we would call a very very basic CI!

#### What does this CI currently do?

1. Enforces that code quality is always maintained properly on our main/production branch.
2. Easily tests linting on multiple python versions




### Other

for typos:
typos (https://github.com/crate-ci/typos)
