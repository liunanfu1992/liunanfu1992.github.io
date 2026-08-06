#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")"

if ! command -v bundle >/dev/null 2>&1; then
  echo "Bundler is not installed. Install it with: gem install bundler"
  exit 1
fi

# Keep project gems inside this repository instead of installing them globally.
bundle config set --local path vendor/bundle >/dev/null

# Load only the plugins declared in _config.yml. Requiring the whole
# github-pages bundle locally makes the metadata plugin call the GitHub API.
export JEKYLL_NO_BUNDLER_REQUIRE="${JEKYLL_NO_BUNDLER_REQUIRE:-true}"

# Jekyll 3 emits Ruby 3.4 compatibility warnings that can fail to render when
# the project path contains non-ASCII characters.
export RUBYOPT="${RUBYOPT:--W0}"

dependency_marker=".bundle/preview-ready"
if [[ ! -f "$dependency_marker" || Gemfile -nt "$dependency_marker" || Gemfile.lock -nt "$dependency_marker" ]]; then
  echo "Installing project dependencies..."
  bundle install
  touch "$dependency_marker"
fi

host="${JEKYLL_HOST:-127.0.0.1}"
port="${JEKYLL_PORT:-4000}"
livereload_port="${JEKYLL_LIVERELOAD_PORT:-35730}"

echo "Starting local preview at http://${host}:${port}"
exec bundle exec jekyll serve \
  --livereload \
  --livereload-port "$livereload_port" \
  --host "$host" \
  --port "$port"
