class DevspecLite < Formula
  desc "Compact, resumable spec-driven workflow templates for AI coding agents"
  homepage "https://github.com/speclabs/devspec-lite"
  url "https://github.com/speclabs/devspec-lite/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "REPLACE_AT_RELEASE"
  license "Apache-2.0"

  depends_on "python@3.10"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/devspec-lite", "--help"
  end
end
