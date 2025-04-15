-- ~/.config/nvim/lua/plugins/init.lua

return {
  -- Import all the default LazyVim plugins
  { import = "lazyvim.plugins" },

  -- Import official LazyVim extras
  { import = "lazyvim.plugins.extras.ui.mini-starter" },
  { import = "lazyvim.plugins.extras.lang.json" },
  { import = "lazyvim.plugins.extras.lang.python" },
  { import = "lazyvim.plugins.extras.lang.yaml" },
  { import = "lazyvim.plugins.extras.lang.docker" },
  { import = "lazyvim.plugins.extras.formatting.prettier" },
  { import = "lazyvim.plugins.extras.formatting.black" },
  { import = "lazyvim.plugins.extras.linting.eslint" },
  { import = "lazyvim.plugins.extras.coding.copilot" },
  { import = "lazyvim.plugins.extras.dap.core" },
  { import = "lazyvim.plugins.extras.dap.python" },
  { import = "lazyvim.plugins.extras.util.telescope" },

  -- Re-declare todo-comments to eagerly load it and telescope extension
  {
    "folke/todo-comments.nvim",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "nvim-telescope/telescope.nvim",
    },
    config = function()
      require("todo-comments").setup()
      require("telescope").load_extension("todo-comments")
    end,
    lazy = false,
  },

  -- Mason: Ensure additional dev tools are installed
  {
    "williamboman/mason.nvim",
    opts = {
      ensure_installed = {
        "stylua",
        "shellcheck",
        "shfmt",
        "flake8",
        "prettier",
        "black",
        "eslint_d",
        "debugpy",
      },
    },
  },
}
