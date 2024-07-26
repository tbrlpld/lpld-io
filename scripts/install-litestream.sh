#!/usr/bin/env bash
# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

version="v0.3.9"
platform=$(arch)
if [[ $platform == "aarch64" ]]; then
    # Inside of docker on M1 that architecture comes out as aarch64 while locally is arm64
    platform="arm64"
fi
package="litestream-$version-linux-$platform.deb"
echo "Installing Litestream..."
url="https://github.com/benbjohnson/litestream/releases/download/$version/$package"
echo $url
wget $url
dpkg -i $package
