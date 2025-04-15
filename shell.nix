{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "lazyvim-dev-shell";

  buildInputs = with pkgs; [
    # Core tools
    neovim
    git
    curl
    wget
    unzip
    ripgrep
    fd

    # Language support
    lua
    lua-language-server
    stylua

    nodejs
    nodePackages.prettier
    nodePackages.eslint

    python3
    python3Packages.pip

    rustc
    cargo
    rust-analyzer
  ];

  shellHook = ''
    echo "🚀 Welcome to your LazyVim dev shell!"
    export EDITOR=nvim

    # Install LazyVim if not already present
    if [ ! -d "$HOME/.config/nvim" ]; then
      echo "📦 Installing LazyVim in ~/.config/nvim..."
      git clone https://github.com/LazyVim/starter ~/.config/nvim
      echo "✅ LazyVim cloned! Launch Neovim to complete plugin install."
    else
      echo "✅ LazyVim already set up. Launch with: nvim"
    fi
  '';
}

