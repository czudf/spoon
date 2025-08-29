#!/bin/bash

set -eux -o pipefail

bump_scheme="${1:-patch}"

current_version="$(uvx hatch version)"
: ">>> Current version: $current_version"

# bump to a new version
uvx hatch version "$bump_scheme"
new_version="$(uvx hatch version)"
: ">>> New version: $new_version"

# commit changes
git commit -am "Release $new_version"
git tag "v$new_version"
GIT_PAGER=cat git log --pretty="format:%s" -3
git push origin main --tags
