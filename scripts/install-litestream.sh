#!/usr/bin/env bash
# Bash "strict mode"
set -euo pipefail
IFS=$'\n\t'

# Install Litestream: https://litestream.io/install/debian/
version="v0.3.9"
platform=$(arch)
if [[ $platform == "aarch64" ]]; then
    # Inside of docker on M1 that architecture comes out as `aarch64` while locally is `arm64`.
    platform="arm64"
elif [[ $platform == "x86_64" ]]; then
    # On Github Actions (and my old MacBook) the architecture is `x86_64`.
    # However, there is no specific build of Litestream for that architecture.
    # I don't know why, but using the `amd64` version there works, while it causes the installation to err out when using it on `arm64`.
    platform="amd64"
fi
package="litestream-$version-linux-$platform.deb"
echo "Installing Litestream..."
url="https://github.com/benbjohnson/litestream/releases/download/$version/$package"
echo $url
wget $url
dpkg -i $package
