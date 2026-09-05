# Release packaging

The package version has one source: `src/devspec_lite/__init__.py`. `pyproject.toml` reads that value dynamically. Every tag release verifies that `vX.Y.Z` matches it before creating any distributable artifact.

## Release outputs

- Python: a wheel, source distribution, and `devspec-lite-python-package-checksums.txt`; tag releases publish the package to PyPI through the configured trusted publisher and attach the artifacts to the GitHub release.
- WinGet: a portable `devspec.exe`, its SHA-256 file, and versioned WinGet manifests with the release URL and SHA-256 inserted. The workflow attaches them to the GitHub release; submit the generated manifests to `winget-pkgs` separately.
- Homebrew: a tap-ready formula and source-tarball SHA-256 file. Copy the generated `Formula/devspec-lite.rb` into the `speclabs/homebrew-devspec-lite` tap repository and publish it there.

No workflow changes an external registry or tap directly. Configure the PyPI trusted publisher for `.github/workflows/python-package-publish.yml` before the first tag release.