# basic-sentiment-mcp-server

## Prerequisites

ℹ️ NOTE: This setup is only tested on macOS.

Install Homebrew using [these instructions](https://brew.sh/)

### Python

Any version at or above Python 3.10 should work. Install it like so:

```shell
brew install python
```

Also install the Python package manager `uv` using the [official instructions](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer).

### npx

We'll need `npx` as well. We can get it by installing the Node package manager `npm`.

Install the `npm` version manager `nvm` using [these instructions](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating).

Then install Node.js and `npm`. We'll go with Node version 22 "Jod" (LTS).

```shell
nvm install lts/jod
```

That should give you Node.js, `npm`, and `npx` all at once. You can verify the `npx` installation by running:

```shell
npx --version
```

## Install dependencies

At the root of the project directory, run the following:

```shell
uv sync
```

## Run and test the server

The MCP SDK is part of the project dependencies, so we can use the [MCP Inspector utility](https://modelcontextprotocol.io/docs/tools/inspector).

In the root of the project directory directory, run:

```shell
uv run mcp dev server.py
```

It will output a message like:

```shell
MCP Inspector is up and running at http://127.0.0.1:{somePort}
```

Go ahead and open that URL in your browser to view the MCP Inspector.

For the `Transport Type`, select `STDIO`. Click `Connect` and if that works, you will the inspector view populate.
