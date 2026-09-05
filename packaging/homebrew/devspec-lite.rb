class DevspecLite < Formula
  include Language::Python::Virtualenv

  desc "Compact, resumable spec-driven workflow templates for AI coding agents"
  homepage "https://github.com/speclabs/devspec-lite"
  url "https://github.com/speclabs/devspec-lite/archive/refs/tags/vREPLACE_WITH_VERSION.tar.gz"
  sha256 "REPLACE_WITH_RELEASE_SHA256"
  license "Apache-2.0"

  depends_on "python@3.10"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/devspec --version")
  end
end